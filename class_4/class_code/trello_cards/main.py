from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List
from structured_output import *
from trello_card_api import TrelloHelper

class TrelloCard(BaseModel):
    """
    Represents a Trello card with its core properties
    """
    name: str = Field(description="Title of the card")
    desc: str = Field(description="Holds details about the card")
    labels: List[str] = Field(description="Labels attached to the card")
    
# Initialize model and parser
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
structured_model = model.with_structured_output(TrelloCard)

# Create prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful assistant that converts text descriptions into structured Trello cards. 
    Create a well-organized card with appropriate title, description, and labels."""),
    ("human", "Please convert this task description into a Trello card: {task_description}")
])

# Create chain using the | operator
chain = prompt | structured_model

# Example usage
task_description = """
Need to update the company website by next Friday. 
This includes:
- Updating team member profiles
- Adding new product features
- Fixing broken links
Please assign this to Sarah and Mark from the web team.
Label this as high priority and website maintenance.
"""

trello_card = chain.invoke({"task_description": task_description})
print(f"Trello card: {trello_card}")
print(f"Object type: {type(trello_card)}")

trello_helper = TrelloHelper()
trello_helper.create_card(trello_card.name, trello_card.desc, trello_card.labels)

