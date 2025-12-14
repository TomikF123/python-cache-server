from fastapi import FastAPI,Request,Response
from httpx import Response as HttpxResponse
import httpx
from cache_proxy.core.cache import cache
from cache_proxy.config import settings
import asyncio
from urllib.parse import urljoin
class ProxyService:
    def __init__(self) -> None:
        # settings.origin = settings.origin
        # assert settings.origin !=''
        pass
    async def handle_request(self,request:Request,path: str)->Response:
        method = request.method
        assert settings.origin != ''
        target_url = urljoin(settings.origin,path)
    
        if method =="GET":
            #print("kokot",target_url,method,settings.origin)
           # print(settings.origin,settings.port)
            if not path.startswith("/"):
                path = f"/{path}"
            status,response = await cache.get(url=target_url)
            return self._convert_to_fastapi_response(cache_status=status,httpx_response=response)
        
    def _convert_to_fastapi_response(self, cache_status:str, httpx_response: HttpxResponse) -> Response:
            # Copy headers but remove encoding-related ones
        headers = dict(httpx_response.headers)
        
        # Remove headers that would cause double-decoding
        headers.pop('content-encoding', None)
        headers.pop('Content-Encoding', None)
        
        # Also remove transfer-encoding if present
        headers.pop('transfer-encoding', None)
        headers.pop('Transfer-Encoding', None)
        headers["X-cache"]=cache_status
        # Update content-length since we decoded the content
        headers['content-length'] = str(len(httpx_response.content))
        return Response(
        content=httpx_response.content,
        status_code=httpx_response.status_code,
        headers=headers,
        media_type=httpx_response.headers.get("content-type")
    )

# proxy = ProxyService()


if __name__ =="__main__":
    pass