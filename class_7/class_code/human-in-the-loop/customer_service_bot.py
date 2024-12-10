from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from langsmith import Client
from langsmith import traceable
from langsmith.wrappers import wrap_openai
import openai

# Initialize clients
openai_client = wrap_openai(openai.Client())
langsmith_client = Client()

# System prompt for the customer service bot
SYSTEM_PROMPT = """You are an expert customer service representative. Your task is to:
1. Analyze the customer's message
2. Create a clear, step-by-step internal plan to resolve their issue
3. Format the response as a numbered list of actions

Guidelines:
- Keep steps clear and concise
- Include any necessary escalation steps
- If more information is needed from the customer service team, list those questions first
- Focus on actionable steps that can be taken to resolve the issue

Example format:
1. Action step one
2. Action step two
3. Action step three"""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("user", "{customer_message}")
])

@traceable(name="customer_service_planner")
def generate_service_plan(customer_message: str) -> dict:
    """Generate a customer service plan for the given customer message."""
    
    # Create chat model
    chat = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )
    
    # Format prompt with customer message
    messages = prompt.format_messages(customer_message=customer_message)
    
    # Generate response
    response = chat.invoke(messages)
    
    return {
        "customer_message": customer_message,
        "service_plan": response.content
    }

def save_feedback_to_dataset(run_id: str, customer_message: str, corrected_plan: str):
    """Save corrected output to LangSmith dataset for future training."""
    
    # Create dataset if it doesn't exist
    try:
        dataset = langsmith_client.create_dataset(
            "customer_service_plans",
            description="Corrected customer service plans for training"
        )
        print(f"Created new dataset")
    except Exception as e:
        print(f"Error creating dataset: {str(e)}")
        try:
            dataset = langsmith_client.read_dataset(dataset_name="customer_service_plans")
            print(f"Found existing dataset with ID: {dataset.id}")
        except Exception as e:
            print(f"Error reading dataset: {str(e)}")
            raise

    # Create feedback with correction
    feedback = langsmith_client.create_feedback(
        run_id,
        key="corrected_plan",
        score=1.0,
        correction=corrected_plan
    )
    
    # Add feedback to dataset
    langsmith_client.create_example(
        inputs={"customer_message": customer_message},
        outputs={"service_plan": corrected_plan},
        dataset_id=dataset.id
    )

# Example usage
if __name__ == "__main__":
    # Example customer message
    customer_message = "I ordered a laptop from your online store 5 days ago, but I still haven't received any shipping confirmation. Order #12345."
    
    # Generate service plan
    result = generate_service_plan(customer_message)
    
    print("\nCustomer Message:")
    print(result["customer_message"])
    print("\nProposed Service Plan:")
    print(result["service_plan"])
    
    # Example of saving feedback
    corrected_plan = """1. Verify customer's order #12345 in the system
2. Check order status and shipping information
3. If order is processed but not shipped, expedite shipping
4. Send customer updated tracking information via email
5. Offer compensation for delayed shipping (10% discount on next purchase)
6. Follow up in 24 hours to ensure customer received shipping confirmation"""
    
    # Get the run ID from the traced execution
    run_id = result.get("__run", {}).get("id")
    if run_id:
        save_feedback_to_dataset(run_id, corrected_plan) 