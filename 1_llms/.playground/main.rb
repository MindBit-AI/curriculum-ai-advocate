#/usr/bin/env /Users/byronmackay/Dev/AI/file_ingestion_app/docker_ai_file_ingestion/.venv/bin/python /Users/byronmackay/.cursor/extensions/ms-python.debugpy-2024.8.0-darwin-arm64/bundled/libs/debugpy/adapter/../../debugpy/launcher 64038 -- /Users/byronmackay/Dev/AI/file_ingestion_app/docker_ai_file_ingestion/app/evaluation/category_cag_dataset_generator.py  ruby

# Your Ruby code here

require 'openai'
require 'dotenv'

# Load environment variables from .env file
Dotenv.load

# Set up your OpenAI API key
client = OpenAI::Client.new(access_token: ENV['OPENAI_API_KEY'])

def analyze_sentiment(client, review)
  response = client.chat(
    parameters: {
      model: "gpt-4-turbo-preview", # Note: Changed from "gpt-4o-mini" as it's not a valid model name
      messages: [
        { role: "user", content: "You are a sentiment analysis expert. Analyze the sentiment of the following movie review and respond with either 'Positive', 'Negative', or 'Neutral'. #{review}" }
      ],
      temperature: 0.7
    }
  )
  response.dig("choices", 0, "message", "content").strip
end

# Example movie review
movie_review = """
The latest superhero blockbuster was a rollercoaster of emotions. 
The special effects were mind-blowing and the action sequences kept me on the edge of my seat. 
However, the plot felt a bit predictable at times, and some character development was lacking. 
Overall, it was an entertaining experience, but not as groundbreaking as I had hoped.
"""

# Analyze the sentiment
sentiment = analyze_sentiment(client, movie_review)

puts "Movie Review:\n#{movie_review}\n"
puts "Sentiment: #{sentiment}"
