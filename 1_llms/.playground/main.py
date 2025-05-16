from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set up your OpenAI API key

def analyze_sentiment(review):
    response = client.chat.completions.create(model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": f"You are a sentiment analysis expert. Analyze the sentiment of the following movie review and respond with either 'Positive', 'Negative', or 'Neutral'. {review}"}
    ])
    return response.choices[0].message.content.strip()

# Example movie review
movie_review = """
The latest superhero blockbuster was a rollercoaster of emotions. 
The special effects were mind-blowing and the action sequences kept me on the edge of my seat. 
However, the plot felt a bit predictable at times, and some character development was lacking. 
Overall, it was an entertaining experience, but not as groundbreaking as I had hoped.
"""

# Analyze the sentiment
sentiment = analyze_sentiment(movie_review)

print(f"Movie Review:\n{movie_review}\n")
print(f"Sentiment: {sentiment}")