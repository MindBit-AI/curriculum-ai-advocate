from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List
from pprint import pprint

class Recipe(BaseModel):
    """
    Use this model when working with complete cooking recipes.
    """
    title: str = Field(description="Name of the recipe")
    ingredients: List[str] = Field(description="List of ingredients needed for the recipe")
    instructions: List[str] = Field(description="Step-by-step instructions to prepare the recipe")

# Initialize model and parser
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
structured_model = model.with_structured_output(Recipe)

# Create prompt template with chaining syntax
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that converts recipe text into structured data. Please convert the following recipes into a structured format."),
    ("human", "Recipe text: {recipe_text}")
])

# Gather recipe text
with open("recipe_text_files/mac_and_cheese_recipe.txt", "r") as file:
    recipe_text = file.read()

# Create chain using the | operator
chain = prompt | structured_model
response = chain.invoke({"recipe_text": recipe_text})
pprint(response)

print(response.title)
print(response.ingredients[0])
print(response.instructions[0])