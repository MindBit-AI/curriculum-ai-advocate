const OpenAI = require('openai');
require('dotenv').config();

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

async function analyzeSentiment(review) {
  const response = await client.chat.completions.create({
    model: "gpt-4-turbo-preview",
    messages: [
      {
        role: "user",
        content: `You are a sentiment analysis expert. Analyze the sentiment of the following movie review and respond with either 'Positive', 'Negative', or 'Neutral'. ${review}`
      }
    ]
  });

  return response.choices[0].message.content.trim();
}

// Example movie review
const movieReview = `
The latest superhero blockbuster was a rollercoaster of emotions. 
The special effects were mind-blowing and the action sequences kept me on the edge of my seat. 
However, the plot felt a bit predictable at times, and some character development was lacking. 
Overall, it was an entertaining experience, but not as groundbreaking as I had hoped.
`;

// Analyze the sentiment
(async () => {
  try {
    const sentiment = await analyzeSentiment(movieReview);
    console.log(`Movie Review:\n${movieReview}\n`);
    console.log(`Sentiment: ${sentiment}`);
  } catch (error) {
    console.error('Error:', error);
  }
})();

