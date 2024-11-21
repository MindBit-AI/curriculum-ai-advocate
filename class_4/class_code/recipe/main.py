from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_community.document_loaders import TextLoader
from structured_output import RecipeDoc
from pydantic import BaseModel, Field
from typing import List

class Recipe(BaseModel):
    """
    Use this model when working with complete cooking recipes.
    """
    title: str = Field(title="title", description="Name of the recipe")
    ingredients: List[str] = Field(title="ingredients", description="List of ingredients needed for the recipe")
    instructions: List[str] = Field(title="instructions", description="Step-by-step instructions to prepare the recipe")

# Initialize model and parser
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
structured_model = model.with_structured_output(Recipe)

# Create prompt template with chaining syntax
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that converts recipe text into structured data. Please convert the following recipes into a structured format."),
    ("human", "Recipe text: {recipe_text}")
])

# Create chain using the | operator
chain = prompt | structured_model

# Load and process recipe
if __name__ == "__main__":
    loader = TextLoader("class_4/class_code/recipe/syrup.txt")
    doc = loader.load()
    recipe_text = doc[0].page_content
    structured_recipe = chain.invoke({"recipe_text": recipe_text})
