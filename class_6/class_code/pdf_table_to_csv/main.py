import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from typing import Dict
import traceback
import PyPDF2
from io import BytesIO

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse('static/index.html')

@app.post("/extract-table")
async def extract_table(file: UploadFile = File(...)) -> Dict[str, str]:
    try:
        import tempfile

        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            content = await file.read()
            tmp_file.write(content)
            tmp_file.flush()
            # Convert PDF to image
            bytes = split_pdf_to_bytes(tmp_file.name)

            # Prepare the message for the LLM
            messages = [
                HumanMessage(content=[
                    {"type": "text", "text": "Convert the following PDF page image into a CSV. CSV should come between the tags <CSV> and </CSV>:"},
                    {"type": "document", "document": {
                        "name": "PDF Page Image",
                        "format": "pdf",
                        "source": {
                            "bytes": bytes[0]
                        }
                    }}
                ]),
            ]

            # Initialize ChatOpenAI and get response
            chat = ChatAnthropic(
                model="claude-3-5-haiku-20241022",
                extra_headers={
                    "anthropic-beta": "pdfs-2024-09-25",
                }
            )
            response = chat.invoke(messages)
            
            # Extract the CSV string from the response
            csv_string = response.content
            csv_string = csv_string.split("<CSV>")[-1].split("</CSV>")[0]
            
            os.unlink(tmp_file.name)
        
        return {"csv_data": csv_string}
    
    except Exception as e:
        error_message = f"Error: {str(e)}\n{traceback.format_exc()}"
        print(error_message)  # This will show up in Vercel logs
        raise HTTPException(status_code=500, detail=str(e))

def split_pdf_to_bytes(pdf_path):
    """Splits a PDF into pages and returns a list of byte strings for each page."""
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        page_bytes_list = []

        for page in pdf_reader.pages:

            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(page)

            with open('temp.pdf', 'wb') as temp_file:
                pdf_writer.write(temp_file)

            with open('temp.pdf', 'rb') as temp_file:
                page_bytes = temp_file.read()
                page_bytes_list.append(page_bytes)

    return page_bytes_list

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
