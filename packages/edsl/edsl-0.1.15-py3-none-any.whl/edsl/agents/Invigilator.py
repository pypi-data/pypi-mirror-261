from abc import ABC, abstractmethod
import asyncio
import json
from typing import Coroutine, Dict, Any
from collections import UserDict

from edsl.exceptions import AgentRespondedWithBadJSONError
from edsl.prompts.Prompt import Prompt
from edsl.utilities.decorators import sync_wrapper, jupyter_nb_handler
from edsl.prompts.registry import get_classes
from edsl.exceptions import QuestionScenarioRenderError

from edsl.data_transfer_models import AgentResponseDict
from edsl.exceptions.agents import FailedTaskException


class InvigilatorBase(ABC):
    """An invigiator (someone who administers an exam) is a class that is responsible for administering a question to an agent."""

    def __init__(
        self, agent, question, scenario, model, memory_plan, current_answers: dict
    ):
        self.agent = agent
        self.question = question
        self.scenario = scenario
        self.model = model
        self.memory_plan = memory_plan
        self.current_answers = current_answers

    def get_failed_task_result(self):
        return AgentResponseDict(
            answer=None,
            comment="Failed to get response",
            question_name=self.question.question_name,
            prompts=self.get_prompts(),
        )

    def get_prompts(self) -> Dict[str, Prompt]:
        return {
            "user_prompt": Prompt("NA").text,
            "system_prompt": Prompt("NA").text,
        }

    @classmethod
    def example(cls):
        """Returns an example invigilator."""
        from edsl.agents.Agent import Agent
        from edsl.questions import QuestionMultipleChoice
        from edsl.scenarios.Scenario import Scenario
        from edsl.language_models import LanguageModel

        from edsl.enums import LanguageModelType, InferenceServiceType

        class TestLanguageModelGood(LanguageModel):
            _model_ = LanguageModelType.TEST.value
            _parameters_ = {"temperature": 0.5}
            _inference_service_ = InferenceServiceType.TEST.value

            async def async_execute_model_call(
                self, user_prompt: str, system_prompt: str
            ) -> dict[str, Any]:
                await asyncio.sleep(0.1)
                return {"message": """{"answer": "SPAM!"}"""}

            def parse_response(self, raw_response: dict[str, Any]) -> str:
                return raw_response["message"]

        model = TestLanguageModelGood()
        agent = Agent.example()
        question = QuestionMultipleChoice.example()
        scenario = Scenario.example()
        #        model = LanguageModel.example()
        memory_plan = None
        current_answers = None
        return cls(
            agent=agent,
            question=question,
            scenario=scenario,
            model=model,
            memory_plan=memory_plan,
            current_answers=current_answers,
        )

    @abstractmethod
    async def async_answer_question(self):
        "This is the async method that actually answers the question."
        pass

    @jupyter_nb_handler
    def answer_question(self) -> Coroutine:
        async def main():
            results = await asyncio.gather(self.async_answer_question())
            return results[0]  # Since there's only one task, return its result

        return main()

    def create_memory_prompt(self, question_name):
        """Creates a memory for the agent."""
        return self.memory_plan.get_memory_prompt_fragment(
            question_name, self.current_answers
        )


class InvigilatorAI(InvigilatorBase):
    """An invigilator that uses an AI model to answer questions."""

    async def async_answer_question(self, failed=False) -> AgentResponseDict:
        data = {
            "agent": self.agent,
            "question": self.question,
            "scenario": self.scenario,
        }
        # This calls the self.async_get_response method w/ the prompts
        # The raw response is a dictionary.
        raw_response = await self.async_get_response(**self.get_prompts())
        assert "raw_model_response" in raw_response
        response = self._format_raw_response(
            **(
                data
                | {
                    "raw_response": raw_response,
                    "raw_model_response": raw_response["raw_model_response"],
                }
            )
        )
        return response

    async def async_get_response(self, user_prompt: Prompt, system_prompt: Prompt):
        """Calls the LLM and gets a response. Used in the `answer_question` method."""
        try:
            response = await self.model.async_get_response(
                user_prompt.text, system_prompt.text
            )
        except json.JSONDecodeError as e:
            raise AgentRespondedWithBadJSONError(
                f"Returned bad JSON: {e}"
                f"Prompt: {user_prompt}"
                f"System Prompt: {system_prompt}"
            )

        return response

    def _format_raw_response(
        self, agent, question, scenario, raw_response, raw_model_response
    ) -> AgentResponseDict:
        response = question.validate_answer(raw_response)
        comment = response.get("comment", "")
        answer_code = response["answer"]
        answer = question.translate_answer_code_to_answer(answer_code, scenario)
        raw_model_response = raw_model_response
        data = {
            "answer": answer,
            "comment": comment,
            "question_name": question.question_name,
            "prompts": {k: v.to_dict() for k, v in self.get_prompts().items()},
            "cached_response": raw_response["cached_response"],
            "usage": raw_response.get("usage", {}),
            "raw_model_response": raw_model_response,
        }
        return AgentResponseDict(**data)

    get_response = sync_wrapper(async_get_response)

    def construct_system_prompt(self) -> Prompt:
        """Constructs the system prompt for the LLM call."""
        applicable_prompts = get_classes(
            component_type="agent_instructions",
            model=self.model.model,
        )
        if len(applicable_prompts) == 0:
            raise Exception("No applicable prompts found")

        agent_instructions = applicable_prompts[0](text=self.agent.instruction)

        if not hasattr(self.agent, "agent_persona"):
            applicable_prompts = get_classes(
                component_type="agent_persona",
                model=self.model.model,
            )
            persona_prompt_template = applicable_prompts[0]()
        else:
            persona_prompt_template = self.agent.agent_persona

        if undefined := persona_prompt_template.undefined_template_variables(
            self.agent.traits
            | {"traits": self.agent.traits}
            | {"codebook": self.agent.codebook}
            | {"traits": self.agent.traits}
        ):
            raise QuestionScenarioRenderError(
                f"Agent persona still has variables that were not rendered: {undefined}"
            )

        persona_prompt = persona_prompt_template.render(
            self.agent.traits | {"traits": self.agent.traits},
            codebook=self.agent.codebook,
            traits=self.agent.traits,
        )

        if persona_prompt.has_variables:
            raise QuestionScenarioRenderError(
                "Agent persona still has variables that were not rendered."
            )

        return (
            agent_instructions
            + " " * int(len(persona_prompt.text) > 0)
            + persona_prompt
        )

    def get_question_instructions(self) -> Prompt:
        """Gets the instructions for the question."""
        applicable_prompts = get_classes(
            component_type="question_instructions",
            question_type=self.question.question_type,
            model=self.model.model,
        )
        ## Get the question instructions and renders with the scenario & question.data
        question_prompt = applicable_prompts[0]()

        undefined_template_variables = question_prompt.undefined_template_variables(
            self.question.data | self.scenario
        )
        if undefined_template_variables:
            print(undefined_template_variables)
            raise QuestionScenarioRenderError(
                "Question instructions still has variables"
            )

        return question_prompt.render(self.question.data | self.scenario)

    def construct_user_prompt(self) -> Prompt:
        """Gets the user prompt for the LLM call."""
        user_prompt = self.get_question_instructions()
        if self.memory_plan is not None:
            user_prompt += self.create_memory_prompt(self.question.question_name)
        return user_prompt

    def get_prompts(self) -> Dict[str, Prompt]:
        """Gets the prompts for the LLM call."""
        system_prompt = self.construct_system_prompt()
        user_prompt = self.construct_user_prompt()
        return {
            "user_prompt": user_prompt,
            "system_prompt": system_prompt,
        }

    answer_question = sync_wrapper(async_answer_question)


class InvigilatorDebug(InvigilatorBase):
    async def async_answer_question(self) -> AgentResponseDict:
        results = self.question.simulate_answer(human_readable=True)
        results["prompts"] = self.get_prompts()
        results["question_name"] = self.question.question_name
        results["comment"] = "Debug comment"
        return AgentResponseDict(**results)

    def get_prompts(self) -> Dict[str, Prompt]:
        return {
            "user_prompt": Prompt("NA").text,
            "system_prompt": Prompt("NA").text,
        }


class InvigilatorHuman(InvigilatorBase):
    async def async_answer_question(self) -> AgentResponseDict:
        data = {
            "comment": "This is a real survey response from a human.",
            "answer": None,
            "prompts": self.get_prompts(),
            "question_name": self.question.question_name,
        }
        try:
            answer = self.agent.answer_question_directly(self.question, self.scenario)
            return AgentResponseDict(**(data | {"answer": answer}))
        except Exception as e:
            agent_response_dict = AgentResponseDict(
                **(data | {"answer": None, "comment": str(e)})
            )
            raise FailedTaskException(
                f"Failed to get response. The exception is {str(e)}",
                agent_response_dict,
            ) from e


class InvigilatorFunctional(InvigilatorBase):
    async def async_answer_question(self) -> AgentResponseDict:
        func = self.question.answer_question_directly
        data = {
            "comment": "Functional.",
            "prompts": self.get_prompts(),
            "question_name": self.question.question_name,
        }
        try:
            answer = func(scenario=self.scenario, agent_traits=self.agent.traits)
            return AgentResponseDict(**(data | {"answer": answer}))
        except Exception as e:
            agent_response_dict = AgentResponseDict(
                **(data | {"answer": None, "comment": str(e)})
            )
            raise FailedTaskException(
                f"Failed to get response. The exception is {str(e)}",
                agent_response_dict,
            ) from e

    def get_prompts(self) -> Dict[str, Prompt]:
        return {
            "user_prompt": Prompt("NA").text,
            "system_prompt": Prompt("NA").text,
        }


if __name__ == "__main__":
    from edsl.enums import LanguageModelType

    from edsl.agents.Agent import Agent

    a = Agent(
        instruction="You are a happy-go lucky agent.",
        traits={"feeling": "happy", "age": "Young at heart"},
        codebook={"feeling": "Feelings right now", "age": "Age in years"},
        trait_presentation_template="",
    )

    class MockModel:
        model = LanguageModelType.GPT_4.value

    class MockQuestion:
        question_type = "free_text"
        question_text = "How are you feeling?"
        question_name = "feelings_question"
        data = {
            "question_name": "feelings",
            "question_text": "How are you feeling?",
            "question_type": "feelings_question",
        }

    i = InvigilatorAI(
        agent=a,
        question=MockQuestion(),
        scenario={},
        model=MockModel(),
        memory_plan=None,
        current_answers=None,
    )
    print(i.get_prompts()["system_prompt"])
    assert i.get_prompts()["system_prompt"].text == "You are a happy-go lucky agent."

    ###############
    ## Render one
    ###############

    a = Agent(
        instruction="You are a happy-go lucky agent.",
        traits={"feeling": "happy", "age": "Young at heart"},
        codebook={"feeling": "Feelings right now", "age": "Age in years"},
        trait_presentation_template="You are feeling {{ feeling }}.",
    )

    i = InvigilatorAI(
        agent=a,
        question=MockQuestion(),
        scenario={},
        model=MockModel(),
        memory_plan=None,
        current_answers=None,
    )
    print(i.get_prompts()["system_prompt"])

    assert (
        i.get_prompts()["system_prompt"].text
        == "You are a happy-go lucky agent. You are feeling happy."
    )
    try:
        assert i.get_prompts()["system_prompt"].unused_traits(a.traits) == ["age"]
    except AssertionError:
        unused_traits = i.get_prompts()["system_prompt"].unused_traits(a.traits)
        print(f"System prompt: {i.get_prompts()['system_prompt']}")
        print(f"Agent traits: {a.traits}")
        print(f"Unused_traits: {unused_traits}")
        # breakpoint()

    ###############
    ## Render one
    ###############

    a = Agent(
        instruction="You are a happy-go lucky agent.",
        traits={"feeling": "happy", "age": "Young at heart"},
        codebook={"feeling": "Feelings right now", "age": "Age in years"},
        trait_presentation_template="You are feeling {{ feeling }}. You eat lots of {{ food }}.",
    )

    i = InvigilatorAI(
        agent=a,
        question=MockQuestion(),
        scenario={},
        model=MockModel(),
        memory_plan=None,
        current_answers=None,
    )
    print(i.get_prompts()["system_prompt"])

    ## Should raise a QuestionScenarioRenderError
    assert (
        i.get_prompts()["system_prompt"].text
        == "You are a happy-go lucky agent. You are feeling happy."
    )
