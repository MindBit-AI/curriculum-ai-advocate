import os
from dotenv import load_dotenv
from openai import OpenAI
from langsmith.wrappers import wrap_openai
from langsmith import traceable

class OpenAIProvider:
    def __init__(self, model_id: str = "gpt-4o-mini-0125"):
        self.model_id = model_id
        # Initialize the OpenAI API client
        self.client = self._initialize_client()

    def _initialize_client(self):
        # Load environment variables from .env file
        load_dotenv()
        
        # Get the API key from environment variables
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables or .env file")
        
        # Create and return the OpenAI client
        return wrap_openai(OpenAI(api_key=api_key))

    @traceable 
    def invoke(self, messages = []) -> str:
        # Send the prompt to the OpenAI API and return the response
        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=messages
        )
        
        # Extract and return the generated text
        return response.choices[0].message

if __name__ == "__main__":
    provider = OpenAIProvider()
    messages = [
        {"role": "user", "content": "How are you?"}
    ]
    response_message = provider.invoke(messages)
    print(f"Prompt: {messages}\nResponse: {response_message.content}")
