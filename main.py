from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove, new_session

app = FastAPI()

# Load the clothing-optimized model once when the service starts
session = new_session("u2netp")

@app.get("/")
def home():
    return {"status": "Background remover is running", "model": "u2netp"}
@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    input_data = await file.read()
    output_data = remove(input_data, session=session)
    return Response(content=output_data, media_type="image/png")
