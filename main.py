from fastapi import FastAPI, File, UploadFile, HTTPException
from langchain_community.document_loaders import PyPDFLoader
from pydantic import BaseModel
# from planner import Planner
from start_process import StartProcess
start_intial_process = StartProcess()
from typing import List
app = FastAPI()
import shutil
import os
from tempfile import NamedTemporaryFile
class Query(BaseModel):
    query: str

@app.post("/process")
async def process_query(query: Query):
    """
    A description of the entire function, its parameters, and its return types.
    """
    try:
        result = await start_intial_process.start_process(query.query)
        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail="Operation not supported or failed.")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error.")

    
