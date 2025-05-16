import sys
import os
from typing import List, Callable, Dict, Any

# Add the app directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from openai_provider import OpenAIProvider
from langsmith.client import Client, convert_prompt_to_openai_format

class PromptOptimizer:
    def __init__(self, model_id: str = "gpt-4o-mini", optimizer_model_id: str = "gpt-4o-mini"):
        self.llm = OpenAIProvider(model_id=model_id)
        self.optimizer_llm = OpenAIProvider(model_id=optimizer_model_id)
        self.langsmith = Client()  # Initialize LangSmith client

    def optimize(self, dataset_name: str, prompt_name: str, evaluate_func: Callable, retries: int = 3):
        # Get dataset from LangSmith
        # dataset = self.langsmith.read_dataset(dataset_name)
        examples = list(self.langsmith.list_examples(dataset_name=dataset_name))

        best_prompt = None
        best_grade = 0

        for example in examples:
            updated_prompt = None
            history = []
            system_prompt = self._compile_system_prompt(
                prompt_name=prompt_name
            )
            formatted_prompt = system_prompt.invoke({"review":example.inputs["Review"]})
            openai_payload = convert_prompt_to_openai_format(formatted_prompt)

            for i in range(retries + 1):   
                # generate the prompt 

                output = self.llm.invoke(openai_payload["messages"])
                grade = evaluate_func(output.content, example.outputs)

                prompt = updated_prompt or formatted_prompt
                history_item = {"input": prompt, "output": output, "grade": grade}
                history.append(history_item)

                print(f"{prompt_name} - Example {examples.index(example) + 1}, Iteration {i + 1}, Grade: {grade}")

                if grade > best_grade:
                    best_grade = grade
                    best_prompt = prompt

                if i < retries:
                    updated_prompt = self._rewrite_prompt(example, history)

        print(f"Best {prompt_name} prompt:\n{best_prompt}")
        print(f"Best grade: {best_grade}")

        return best_prompt, best_grade

    def _compile_system_prompt(self, prompt_name: str, metadata: Dict[str, Any] = {}) -> str:
        # Get prompt from LangSmith hub
        prompt = self.langsmith.pull_prompt(prompt_name)
        return prompt

    def _rewrite_prompt(self, example: Any, history: List[dict]) -> str:
        messages=[
            {
                "role": "system", 
                "content": """
                    You are a senior prompt engineer who is amazing at writing better prompts for LLMs.
                            
                    Your job is to rewrite a prompt so it improves the score. The score is a comparison of the output's values with the expected outputs.
                    
                    The scores minimum score is 0 and it's maximum score is 1.

                    The final response should be in the following format:

                    THOUGHT: <a thought about how you can edit the prompt to improve the score>
                    EDITED PROMPT: <the new system prompt>

                    Here is the history of the prompt so far (the input is what you will update):
        
                    {self._convert_to_string(history)}

                    The expected output is: {example.outputs}

                    Only provide a new system prompt. No changes to the human message or example.
                """
            },
            {
                "role": "user",
                "content": f"{example}"
            }
        ]

        return self.optimizer_llm.invoke(messages) 

    @staticmethod
    def _convert_to_string(history: List[dict]) -> str:
        result = ""
        for i, attempt in enumerate(history):
            result += f"Attempt {i+1}\n"
            input_str = attempt["input"]
            output_str = attempt["output"]
            grade_str = str(attempt["grade"])
            result += f"Input: {input_str}\nOutput: {output_str}\nScore: {grade_str}\n\n"
        return result

# Example usage:
if __name__ == "__main__":

    def evaluate_values(output: str, expected_output: str) -> float:
        if expected_output['Sentiment'] == output:
            return 1
        return 0

    optimizer = PromptOptimizer()
    best_prompt, best_grade = optimizer.optimize(
        dataset_name="movie-review-sentiment", 
        prompt_name="movie-review", 
        evaluate_func=evaluate_values
    )
    print(f'Best prompt: {best_prompt}')
    print(f'Best grade: {best_grade}')
