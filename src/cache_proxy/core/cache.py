import httpx
from asyncio import Task
from httpx import Response
import asyncio
class Cache:
    def __init__(self):
        self.storage = {}
        self.client = httpx.AsyncClient(follow_redirects=True)

    async def get(self, url) -> tuple[str,httpx.Response]:
        if url in self.storage:
            return "HIT", self.storage[url]

        return "MISS", await self.set(url)

    async def set(self, url):
        try:
            r = await self.client.get(url)
        except Exception as e:
            print(f"Request error for {url}: {e}")
            raise

        self.storage[url] = r
        return r

    def clear(self):
        self.storage = {}




cache = Cache()

if __name__ == "__main__":
    
    async def test():
        #print(cache.get("https://google.com"))
        cor1 = cache.get("https://google.com")
        cor2 = cache.get("https://google.com")
        results = await asyncio.gather(cor1,cor2)
        hit:tuple[str,Response] = await cache.get("https://google.com")

        print(results[0])  # First result: ("MISS", response)
        print(results[1:7])  # Second result: ("HIT", response) - from cache
        print(hit[1].text[:500])
    asyncio.run(test())

    # cache.get("https://github.com")
