from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Initialize the database connection - NOTE: Make sure to run this from the curriculum_ai_advocate root, or change the db path relative to where you started
db = SQLDatabase.from_uri("sqlite:///class_5/class_code/sql_agent/test.db")

# Create the SQL agent
agent_executor = create_sql_agent(
    llm=ChatOpenAI(temperature=0, model="gpt-4o-mini"),
    db=db,
    verbose=True,
    agent_type="openai-tools",
)

# Query for most expensive products
response = agent_executor.invoke(
    "What are the top 5 most expensive products in the database? Show their names and prices."
)

print(response["output"])
