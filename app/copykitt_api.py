from fastapi import FastAPI, HTTPException
from copykitt import generate_branding_snippet, generate_keyword_snippet
from magnum import Magnum

MAX_LENGTH = 32
app = FastAPI()
handler = Magnum(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/generate_snippet")
async def generate_snippet_api(subject: str):
    return {"branding_snippet": generate_branding_snippet(subject)}

@app.get("/generate_keywords")
async def generate_keywords_api(subject: str):
    return {"branding_keywords": generate_keyword_snippet(subject)}

@app.get("/generate_snippet_and_keywords")
async def generate_snippet_and_keywords_api(subject: str):
    validate_length(subject)
    return {
        "snippet": generate_branding_snippet(subject),
        "keywords": generate_keyword_snippet(subject)
    }

def validate_length(text):
    if len(text) > MAX_LENGTH:
        raise HTTPException(status_code=400, detail=f"Subject length must be less than {MAX_LENGTH} characters")