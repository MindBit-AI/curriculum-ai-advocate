from fastapi import FastAPI, UploadFile
from main import process_recipe

app = FastAPI()

@app.post("/process-recipe")
async def process_recipe_endpoint(file: UploadFile):
    # Read the contents of the uploaded file
    content = await file.read()
    recipe_text = content.decode('utf-8')
    
    # Process the recipe using imported function
    result = process_recipe(recipe_text)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
