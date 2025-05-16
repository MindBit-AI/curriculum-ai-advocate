# LLMs

## Introduction
As AI advocates, we play a crucial role in identifying opportunities for artificial intelligence (AI) to drive 
business value and lead its adoption within our organizations. This course is designed to help you develop the 
necessary skills and knowledge to effectively utilize Large Language Models (LLMs), which are the foundational tool 
in generative AI applications. Through this lesson, you will learn how LLMs work, how to craft effective prompts 
that produce high-quality outputs, and how to use structured outputs to extract specific data from these models. By 
mastering these skills, you'll be able to identify valuable use cases for LLMs in your organization and effectively 
communicate the benefits of AI adoption to your team and stakeholders.

## Core Competencies
- Understanding the goal of this course and what they'll be learning 
- Know what an AI advocate is and how one helps their business
- A practical understanding of how LLMs work
- Aware of the various types of LLM messages
- Can effectivly use context in prompts
- Realize the value of context to the LLM
- Extract LLM information with structured outputs


### The student must demonstrate...
* Demonstrate an understanding of the role and value of AI advocates in their organization, including identifying AI 
use cases, leading adoption, and championing initiatives.
* Create a mind map or chart that illustrates the technical skills required to become an AI advocate, including 
highlighting projects and use cases covered in the course.
* Explain how LLMs work at a high level
* Identify a specific use case for LLMs in their organization
* Provide examples of simple prompting strategies
* Create effective prompts that utilize context to produce the best outputs from LLMs.
* Identify who owns the context and demonstrate how to bring them onto the project.
* Explain the value of structured outputs in working with LLMs, including using APIs or prompts that follow 
structure instructions.

## Class Sections

1. **Whole Task: What We'll be Doing**
   
   - **Core Competency:** 
        - Understanding the goal of this course and what they'll be learning 
        - Know what an AI advocate is and how one helps their business
   
   - **Relevance:** 
        You're in this course to become an AI advocate. What does an AI advocate do? What is their role and what value do they bring? How do I influence my team/department/team when it comes to AI? Many other questions may exist, and this section will show you what that's like at a 10,000 ft level. 
   
   - **Procedure:**
      1. SOW Example (Who task)
            - Explain the project
            - Highlight the three things a project needs: Expert, context, and evaluations
      1. What technical skills do you need to know?
            - Highlight projects and use cases that we'll be covering 
            - show course topic overview (map)
      1. Becoming an AI advocate
            - Advocates...
                - identify AI use cases and leads adoption
                - are thought leader for AI in the company
                - champion AI initiatives
                - Adding "AI" to your job title can be particularly impactful here
            - Show topic overview and higlight how each box has soft skills associated with these. We'll address these as we go.

   - **Code:**
        Whole task project

1. **Cursor**

    - **Core Competency:** 
        - Knowing how to use Cursor in this class and in your work
   
   - **Relevance:** 
        You will have questions about your code, so why not have an incredible tool handy to help you along? Cursor's built in LLM tools are incredible for coding, archietcting, and asking questions. These tools are also readily accessible and easy to use. 
   
   - **Procedure:**
      1. Accessing the LLM in Cursor
            - 2 ways: inline and chat
                - Inline: Highlight your code and ask it to do something.
                - Chat: Add more context to your questions and get great answers  
            - Context adding:
                - @ symbol
                - Add files, websites, and index any document you want
            - Terminal chat
                - Underrated, you can chat directly in your terminal. If there's a command you can't remember, just say what you want and the command will be produced for you
            Main hotkeys to remember: Cmd+L, cmd+K, @
            - code suggestions
      2. Ship it!
            - Use this, get familiar with its features, and then promote this to your teams. 
            - The value add is immediate. 
            - AI Advocacy can start here.
    - **Code:**
        - Markdown Generator

1. **LLMs**
   
   - **Core Competency:** 
        - A practical understanding of how LLMs work
   
   - **Relevance:** 
        LLMS are the foundational tool in generative AI apps. Using LLMs effectively goes beyond simple prompting, but to understand how it works, it helps to know the principles behind how LLMs work. These principles also make it easier to identify LLM use cases back at the office.
   
   - **Procedure:**
      1. High level overview of how LLMs work
            - training
            - tokens
            - generation
      2. Ship it!
            - Identifying a use case is as simple as finding a task where humans read first, then produces something as a result
                - file ingestion
                - responding to reviews
                - code generation
                - even as simple as extracting dates (what are LLMs bad at vs good at; don't use AI when you can do the same thing easier using something else)

    - **Code:**
        - Review writer

1. **Prompts**
   
   - **Core Competency:** 
        - Can effectivly use context in prompts
        - Give the LLM more context than you think
        - Apply prompt omptimizing tactics
   
   - **Relevance:** 
   Prompting strategies help the LLM produce the best outputs. Some of these strategies like zero/few shot may seem trivial today, but understanding why they work will higlight. More complex strategies like chain of thought have opened new opportunities to what LLMs are capable of. Regardless of the strategy, they all follow one critical LLM principle: tokens are predicting based on the prompt and what has already been generated. 
   
   - **Procedure:**
        1. Quick example of zero/one/few shot prompts
            - highlight that I rarely use zero, I often use one, and occasionally I use few shot prompts.
        2. Show how context impacts the results
            - proprietary data is what makes your AI apps powerful
            - genearlly better to add more context than is needed
        2. Have the LLM rewrite your prompt
            - The LLM will include what it thinks is most important, which is what you want
        3. Ship it!
            - A good prompt likely needs context. Identify who owns the context and bring them onto the project.

   - **Code:**
        - File Ingestion - Category Selector
        - Prompt Optimzer

1. **Structured outputs**
   
   - **Core Competency:** 
        - Realize the value of structured outputs
   
   - **Relevance:** 
    Nearly all LLMs these days follow structure instructions really well, and this is good; we can pull specific data out if it's structured correctly. We'll cover APIs that are specific for structured output, but you don't need them. In fact, many prompts I've seen that need structure often have the structure as part of their prompt.
   
   - **Procedure:**
      1. Chain of Thought
            - structure and effectiveness
            - The principle that LLMs predict the next token by when was given and what was already produced is highlighted strongly by this prompting idea. We can leverage this to produce better outputs in our apps
      2. Ship it!
            - Use structure to extract specific pieces of information.

   - **Code:** movie review sentiment analysis


### Code Examples (to be used in class and provided to students)
- File Ingestion - Category Selector (how context changes outputs)
- movie review sentiment analysis
- Prompt optimizer


**Byron's scratchpad (extra notes):**

2. How to start influencing your team as an AI advocate.
    - explain what is possible with AI
    - educate your team on relevant AI topics
    - teach others on how to think about AI projects
3. Leading AI project development 
- AI projects are different than other software engineering projects
- datasets and evaluations (to measure output and success)
- expertise on the process we're automating at hand is required (you're not necessarily the expert)
- feedback systems and continual maintanance
    - human in the loop
    - llm feedback
    - prompt optimization
- Knowing when to use AI and when not to

Examples
- File Ingestion - Category Selector
- Few shot
- Context is King
- Movie reviews
- Model variation
- Prompts change based on the LLM
- Prompt Optimizer
- LLMs creating their own prompts
 No newline at end of file
