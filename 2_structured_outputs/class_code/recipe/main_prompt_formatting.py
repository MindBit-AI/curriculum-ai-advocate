from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import TextLoader
import json
import pprint

# Initialize model and parser
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Create prompt template with chaining syntax
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful assistant that converts recipe text into structured data. Please convert the following recipes into a structured json format using the following structure:
        Each recipe should have the following items:
        a title
        a list of ingredients
        a list of instructions
        """),
    ("human", "Recipe text: {recipe_text}")
])

loader = TextLoader("./recipe_text_files/mac_and_cheese_recipe.txt")
doc = loader.load()
recipe_text = doc[0].page_content

# Create chain using the | operator
response = model.invoke(prompt.format(recipe_text=recipe_text))
# Remove ```json and ``` from the response content
formatted_response = response.content.replace("```json", "").replace("```", "").strip()
structured_data = json.loads(formatted_response)
pprint.pprint(structured_data)