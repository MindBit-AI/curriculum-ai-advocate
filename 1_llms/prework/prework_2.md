# Prework 2: Creating our first AI Application in Python

We will create a simple AI application to ensure your set up is correct.

1. Create a new folder called `mindbit_starter_app` and open it in Cursor.
2. We'll first setup a virtual environment so any packages we install are scoped to this project. Inside Cursor, open the terminal panel either selecting the terminal icon in the top right of the Cursor window or hitting cmd/cntl+J. 
    In the terminal, create a virtual environment folder:
    ```bash
    uv venv
    ```
    Our dependencies will live in this folder. We need to activate the virtual environment before we install anything.

    Mac:
    ```bash
    source .venv/bin/activate
    ```

    Windows:
    ```bash
    venv/bin/activate
    ```

    With our virtual environment activated, we can now install the OpenAI library:
    ```bash
    uv pip install openai
    ```

3. Create a new file called `main.py`. In that file, paste the following code:

    ```python
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
    ```

4. Now run the file by running this command in the terminal:

    ```
    python main.py
    ```

5. Instead of reading what this code does here, let's have Cursor do it.

    Open the AI panel by either hitting cmd/cntl+L or clicking the AI panel icon in the top right (next to the terminal icon).

    In the AI panel's chat window, you can ask anything about the open file. Ask Cursor to explain any part of the code (or all of it!) until you understand how the code works.

    We'll go over more about writing AI applications and using Cursor in class. You are now done with today's prework.