from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List

class Recipe(BaseModel):
    """
    Use this model when working with complete cooking recipes.
    """
    title: str = Field(description="Name of the recipe")
    ingredients: List[str] = Field(description="List of ingredients needed for the recipe")
    instructions: List[str] = Field(description="Step-by-step instructions to prepare the recipe")

def get_recipe_structure(recipe_text: str) -> Recipe:
    """
    Convert recipe text into structured data using OpenAI's JSON mode.
    
    Args:
        recipe_text (str): The text of the recipe to parse
        api_key (str): Your OpenAI API key
        
    Returns:
        Recipe: A structured Recipe object
    """
    client = OpenAI()
    
    response = client.responses.parse(
        model="gpt-4o-mini",
        input=[
            {
                "role": "system",
                "content": "You are a helpful assistant that converts recipe text into structured data. Please convert the following recipes into a structured format."
            },
            {
                "role": "user",
                "content": f"Recipe text: {recipe_text}"
            }
        ],
        text_format=Recipe
    )
    
    # Get the recipe object directly from the response
    recipe = response.output_parsed 
    return recipe

# Example usage
if __name__ == "__main__":
    # Read recipe text from file
    recipe_text = """
        Cheesy Macaroni and Cheese

        16 oz macaroni pasta (any shape pasta you like)
        1/2 C unsalted butter
        1 tsp salt
        1/2 tsp pepper
        1/2 C flour 
        3 1/2 C milk, warmed
        1/4 C chicken broth
        1/2 lb Velveeta cheese, cubed
        1/2 lb cheddar, cubed

        Topping:
        1/2 C panko bread crumbs or Ritz crackers
        1 Tbl parsley
        2 Tbl butter, melted

        Heat 350' oven. Grease 9x13 glass dish ( 8x8 or round casserole, if making half the recipe).
        Cook pasta for about 2-3 minutes less than called for, drain, set aside.
        In a saucepan, melt 1/2 C butter, salt pepper, once melted add flour, stir until smooth. Let cook for 1 minute. Add milk, chicken broth, bring to a boil, whisking. Add cheeses and stir until melted. Pour over cooked pasta and add to greased dish.

        Combine the panko, parsley and melted butter in a small bowl. Sprinkle panko topping over macaroni, bake uncovered 30 minutes.
    """
    # with open("recipe_text_files/mac_and_cheese_recipe.txt", "r") as file:
        # recipe_text = file.read()
    
    # Get structured recipe
    recipe = get_recipe_structure(recipe_text)
    
    # Print results
    print(f"Title: {recipe.title}")
    print("\nIngredients:")
    for ingredient in recipe.ingredients:
        print(f"- {ingredient}")
    print("\nInstructions:")
    for i, instruction in enumerate(recipe.instructions, 1):
        print(f"{i}. {instruction}") 