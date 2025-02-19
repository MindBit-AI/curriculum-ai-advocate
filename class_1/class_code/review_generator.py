from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI()

def generate_response(review):
    """Generate a friendly response to a customer review"""
    try:
        # Create the prompt for OpenAI
        # messages = [
        #     {
        #         "role": "system", 
        #         "content": """You are a friendly customer service representative at a car dealership. 
        #                       Keep responses professional, empathetic, and under 100 words."""
        #     },
        #     {
        #         "role": "user", 
        #         "content": f"Generate a response to this review: {review}"
        #     }
        # ]
        messages = [
            { 
            "role": "system",
            "content": "Extract the event information."
            },
            {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday. What did Charlie do?"
            }
            ]


        # Get response from OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {str(e)}"

def main():
    # Sample reviews
    reviews = [
        "Great service! Tom in sales was very helpful and got me a great deal on my new SUV.",
        "Waited for 2 hours for an oil change. Terrible service.",
        "The dealership was clean and professional, but the prices were a bit high."
    ]

    # Generate responses for each review
    for i, review in enumerate(reviews, 1):
        print(f"\nReview {i}: {review}")
        print(f"Response {i}: {generate_response(review)}")
        print("-" * 50)

if __name__ == "__main__":
    main()
