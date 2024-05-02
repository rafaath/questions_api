from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TextItem(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Reverse API!"}

@app.post("/reverse/")
def reverse_text(item: TextItem):
    reversed_text = ' '.join(word[::-1] for word in item.text.split())
    return {
        "original_text": item.text,
        "reversed_text": reversed_text
    }
