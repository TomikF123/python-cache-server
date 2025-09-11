from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import redis
import httpx



def start_server(port:int,origin:str):
    app = FastAPI()

    @app.get("/")
    async def hello():
        return {"msg": "hi"}
    uvicorn.run(app, host="127.0.0.1", port=8000)

def connect_to_reddis_db(port:int,origin:str):
    r = redis.Redis(host=origin,port=port,decode_responses=True)
async def check_if_in_cache():
    ...
async def cache_something():
    ...
def fetch_from_upstream(url):
    """Fetch data from upstream server"""
    response = httpx.get(url=url)
    return response


if __name__ == "__main__":
    r = fetch_from_upstream("https://www.google.com")
    print(r.headers)