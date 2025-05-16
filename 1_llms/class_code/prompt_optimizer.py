from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langsmith import Client
from typing import Callable, List

class SimplePromptOptimizer:
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.llm = ChatOpenAI(model_name=model_name, temperature=0, tags=["prompt-tester"])
        self.optimizer_llm = ChatOpenAI(model_name=model_name, temperature=0, tags=["prompt-optimizer"])
        self.langsmith = Client()

    def optimize(self, dataset_name: str, prompt_name: str, evaluate_func: Callable, max_iterations: int = 3) -> tuple:
        # Get the initial prompt
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You determine if movie reviews are either positive or negative."),
            ("user", "{review}")
        ])
        
        # Get examples from dataset
        examples = list(self.langsmith.list_examples(dataset_name=dataset_name))
        
        best_prompt = prompt
        best_score = 0
        
        # Optimization loop
        for iteration in range(max_iterations):
            current_score = 0
            
            # Test current prompt on all examples
            for example in examples:
                # Format the prompt with the example input
                formatted_prompt = prompt.format(review=example.inputs["Review"])
                
                # Get response from LLM
                response = self.llm.invoke(formatted_prompt)
                
                # Evaluate response
                score = evaluate_func(response.content, example.outputs)
                current_score += score
            
            avg_score = current_score / len(examples)
            print(f"Iteration {iteration + 1}, Average Score: {avg_score}")
            
            # Update best prompt if current score is better
            if avg_score > best_score:
                best_score = avg_score
                best_prompt = prompt
            
            # If perfect score or last iteration, break
            if avg_score == 1.0 or iteration == max_iterations - 1:
                break
                
            # Generate improved prompt
            prompt = self._improve_prompt(prompt, examples, avg_score)
        
        return best_prompt, best_score

    def _improve_prompt(self, current_prompt: ChatPromptTemplate, examples: List, current_score: float) -> ChatPromptTemplate:
        # Prompt template for improving the prompt
        improvement_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an expert prompt engineer. Your task is to improve a prompt template to get better results.
                         Analyze the current prompt and examples, then suggest an improved version that will lead to better performance.
                         Keep the same basic structure but enhance the instructions and constraints."""),
            ("user", """Current prompt template: {current_prompt}
                       Current performance score: {score}
                       Example inputs and outputs: {examples}
                       
                       Please provide an improved version of the prompt template that will lead to better results.
                       Only return the new prompt template, nothing else.""")
        ])
        
        # Get improvement suggestion
        response = self.optimizer_llm.invoke(
            improvement_prompt.format(
                current_prompt=current_prompt.messages[0].prompt.template,
                score=current_score,
                examples=str(examples[:2])  # Only show first 2 examples to keep context window manageable
            )
        )
        
        # Create new prompt template with the improved version
        return ChatPromptTemplate.from_messages([
            ("system", response.content),
            ("human", "{review}")
        ])

# Example usage:
if __name__ == "__main__":
    def evaluate_sentiment(output: str, expected: dict) -> float:
        return 1.0 if expected["Sentiment"].lower() in output.strip().lower() else 0.0
    
    optimizer = SimplePromptOptimizer()
    best_prompt, best_score = optimizer.optimize(
        dataset_name="movie_reviews_challenging",
        prompt_name="movie-review",
        evaluate_func=evaluate_sentiment
    )
    
    print(f"\nBest Score: {best_score}")
    print(f"\nBest Prompt:\n{best_prompt}")
