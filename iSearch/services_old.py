
# File: service.py

from fastapi import FastAPI

# That is the file where NeuralSearcher is stored
from neural_searcher import NeuralSearcher
# from qdrant_client import fu
from pydantic import BaseModel
from text_searcher import extract_sentence_index

app = FastAPI()

# Create an instance of the neural searcher
neural_searcher = NeuralSearcher(collection_name='startups1')

class search_item(BaseModel):
    query_id: int
    query: str

@app.post("/search")
async def getInformation(req_info : search_item):
    # req_info = await req_info.json()
    return {
        "status": 200,
        "input_data": req_info,
        "semantic_result": neural_searcher.search(text=req_info.query)

    }


@app.get("/api/search")
def search_collection(q: str):
    return {
        "semantic_result": neural_searcher.search(text=q)
    }

@app.post("/api/fulltextsearch")
def full_text_search(req_info : search_item):
    return {
        "status": 200,
        "input_data": req_info,
        "exact_match_result":  extract_sentence_index(req_info.query)

    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8999)