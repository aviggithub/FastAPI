"""
fast api Example
@author: Avinash G
"""
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
 
class Item(BaseModel):
    pname: str
    price: Optional[int] = None
    description: Optional[str] = None
    tax: Optional[float] = None
    data : list
 
app = FastAPI()

origins = ["*"] # list path of domains

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "ok"}

@app.get("/getdata/")
async def getdata():
    return {"status": "ok"}
 
@app.post("/postdata/")
async def createdata(datai: Item, status_code = 200):
    data_dict = datai.dict()
    print(data_dict)
    print("data_list:-", datai.data)
    if datai.tax:
        price_with_tax = datai.price + datai.tax
        data_dict.update({"price_with_tax": price_with_tax})
    return data_dict
    
if __name__ == "__main__":
    kwargs = {"host": "0.0.0.0", "port": 8000}
    kwargs.update({"debug": False, "reload": True})
    uvicorn.run("app:app", **kwargs)