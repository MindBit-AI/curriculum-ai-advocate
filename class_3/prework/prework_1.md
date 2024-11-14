# Setting up LangSmith

Here are instructions for setting up a LangSmith account, similar in style and format to the Pinecone setup instructions you provided:

## Setting Up a LangSmith Account

1. Go to the [LangSmith website](https://www.langsmith.com/) and click on the "Sign Up" button.

2. Choose your preferred sign-up method, such as using your email address, Google account, or GitHub account. If prompted, verify your email address.

3. You should now see a page with instructions on setting up an API key. Follow those instructions. 

    - Here are extra instructions on saving your environment variables:
        <details>
        <summary>On Mac:</summary>

        Open your .bash_profile file with a text editor: open ~/.bash_profile.
        
        Add the lines:
        
            export LANGCHAIN_TRACING_V2=true
            export LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
            export LANGCHAIN_API_KEY="{your key}"
            export LANGCHAIN_PROJECT="{your-langsmith-project-name}"
        
        Save the file and close it.

        </details>
        <details>
        <summary>On Windows:</summary>

        Go to "Control Panel" > "System and Security" > "System"
        
        Click "Advanced system settings"
        
        Select the "Advanced" tab and click "Environment Variables"
        
        Under "User variables", click "New"
        
        Enter the following variables:

            Variable name: "LANGCHAIN_TRACING_V2", Value: "true"
            Variable name: "LANGCHAIN_ENDPOINT", Value: "https://api.smith.langchain.com"
            Variable name: "LANGCHAIN_API_KEY", Value: "{your key}"
            Variable name: "LANGCHAIN_PROJECT", Value: "{your-langsmith-project-name}"

        Click "OK" to save

        </details>

4. Run the example code they provide you, or run any code that runs an LLM through the LangChain library (you can also run [test_file.py](./test_file.py) located within today's prework).

5. After running your code, LangSmith's webpage should automatically update and take you to the trace that was just made. A trace is a record of your LLM interaction. Click on the trace to explore more about it.

That's it! You've successfully set up a LangSmith account. Reach out on Discord if you have any questions. 