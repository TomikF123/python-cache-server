from fastapi import FastAPI, Request,Response
from cache_proxy.config import settings
import asyncio
import datetime
from cache_proxy.core.proxy import ProxyService
from cache_proxy.core.cache import cache
from cache_proxy.server import stop_server
app = FastAPI(title="caching proxy server or somthing")

proxy = ProxyService()
@app.get("/")
async def health_check():
    """Health check endpoint - shows proxy status."""
    assert settings.origin != '' 
    return {
        "status": "running",
        "origin": settings.origin,
        "cached_items": len(cache.storage),
        "time":str(datetime.datetime.now())
    }

@app.get("/slow")
async def slow():
    await asyncio.sleep(5)  # simulates a slow I/O operation
    return {"status": "done",
            "time":str(datetime.datetime.now())
            }
@app.post("/admin/clear_cache")
async def clear_cahce():
    cache.clear()
    return await health_check()
@app.post("/admin/shutdown")
async def shut_down():
    async def _shutfown():
        await asyncio.sleep(0.1)
        stop_server()
    asyncio.create_task(_shutfown())
    return {"status":"shutting down"}

@app.api_route("/{path:path}",methods=["GET","POST","PUT","DELETE","PATCH"])
async def proxy_request(request:Request,path: str):
    assert settings.origin != ''
    return await proxy.handle_request(request=request,path=path)

# @app.get(f"/idk")
# async def