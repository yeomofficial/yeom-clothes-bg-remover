from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove, new_session

app = FastAPI()

# Allow requests from any origin (needed for Hoppscotch + your future frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

session = new_session("u2netp")

@app.get("/")
def home():
    return {"status": "Background remover is running", "model": "u2netp"}

@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    input_data = await file.read()
    output_data = remove(input_data, session=session)
    return Response(content=output_data, media_type="image/png")
