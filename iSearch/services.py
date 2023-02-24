
# File: service.py

from fastapi import FastAPI

# That is the file where NeuralSearcher is stored
from neural_searcher import NeuralSearcher
# from qdrant_client import fu
from pydantic import BaseModel
from text_searcher import extract_sentence_index
from table_qa import table_predict
import traceback

app = FastAPI()

# Create an instance of the neural searcher
neural_searcher = NeuralSearcher(collection_name='MSF_iSearch_Collection')

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

@app.post("/exactsearch")
def full_text_search(req_info : search_item):
    return {
        "status": 200,
        "input_data": req_info,
        "exact_match_result":  extract_sentence_index(req_info.query)

    }
class table_item(BaseModel):
    query_id: int
    question: str
    csv_url:str

@app.post("/tableQA")
async def predict( body: table_item):
    query = body.question
    # csv_url =  table_predict( body.csv_url,query)
    try:
        prediction = table_predict( body.csv_url,query)
    except:
        print("Exception > ", traceback.format_exc())
        return {"status": 500}


    return {"prediction": prediction, "status": 200}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8999)