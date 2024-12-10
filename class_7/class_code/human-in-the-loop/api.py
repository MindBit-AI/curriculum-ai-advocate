from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from customer_service_bot import generate_service_plan, save_feedback_to_dataset
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI(
    title="Customer Service Bot API",
    description="API for generating and managing customer service plans"
)

class CustomerMessage(BaseModel):
    message: str

class FeedbackRequest(BaseModel):
    run_id: str
    customer_message: str
    corrected_plan: str

@app.post("/generate-plan")
async def create_service_plan(request: CustomerMessage):
    try:
        result = generate_service_plan(request.message)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/save-feedback")
async def save_feedback(request: FeedbackRequest):
    try:
        save_feedback_to_dataset(request.run_id, request.customer_message, request.corrected_plan)
        return {"status": "success", "message": "Feedback saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8001, reload=True) 