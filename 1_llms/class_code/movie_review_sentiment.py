from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

prompt = """
    I want you to tell me if the following movie review is positive or negative.

    Review: This film shouldn't work at all. It doesn't have much of a story and the whole 
    dial up internet thing is incredibly dated. However Hanks and Ryan sell it beautifully.
    
"""
# The final response should be in the following format:
# thought: analyze the review to determine if it's positive or negative
# sentiment: "positive" or "negative"

response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )

print(response.choices[0].message.content)

# # Test each model multiple times
# for attempt in range(10):
#     print(f"---------ATTEMPT {attempt}---------")
#     for model in models:
#         try:
#             response = client.chat.completions.create(
#                 model=model,
#                 messages=[{"role": "user", "content": prompt}],
#                 temperature=0.7
#             )
#             result = f"{model.upper()}\n{response.choices[0].message.content}\n_________________________\n"
#             print(result)
#         except Exception as e:
#             print(f"Error with {model}: {str(e)}")

