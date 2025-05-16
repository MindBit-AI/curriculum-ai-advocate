## Prompt Strategies

Prompt engineering was once thought of as a future career option. It's not, at least not by itself. As an AI engineer, you'll be dealing with plenty of prompts and figuring out what is the best way to structure what you're asking. Let's look at a few prompt strategies that are commonly forgotten.

1. Break down your prompts
Models are at their best when they are focused on one thing. Instead of asking in one prompt for "extract the pertentant data then add it to a CSV and then summarize the results", break it into two (or maybe three) prompts. The more you ask, the worse the LLM will perform in any one of the tasks.

6. Latency
Latency on any *single* model call is usually ok, but clients get in trouble when they stack many calls together. I'm a big advocate for breaking down prompts into different parts, but within reason. Use async whenever possible. If you don't roll your own framework, LangGraph helps with this.

7. Guardrails
How do you know your model isn't going haywire? In general you should be ok, but can you trust users? Usually a simple validation check w/ gpt-4o-mini or flash will solve for this. If you're worried about it, don't output what the model says to the user unless it's validated.

8. Evals
The reason these are so hard is because the ground truth dataset is a pain to maintain. People are lazy. However, it's worth the work. Have your team (or just you) sit down for a Saturday afternoon, grab your beverage of choice, and label 100 data points. This will be what you'll test your RAG against. Ideally, each step in your RAG should have an eval.

9. Cost
Not a ton to do here other than 1) reduce your prompt size (get picky on your context you pass) 2) take advantage of batch APIs latency-independent queries and 3) use prompt caching. Though OpenAI/Anthropic boast 50/90% reduction in query, expect about -15% costs in practice.
