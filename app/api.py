from fastapi import FastAPI, HTTPException
from typing import List
from slot_filing import slot_filing
from elastic_query import search

app = FastAPI()

@app.get("/search/", response_model=List[dict])
async def get_results(sentence: str):
    try:
        slots = slot_filing(sentence)
        results = search(slots)
        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
