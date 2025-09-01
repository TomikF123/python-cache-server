import time
import requests
import threading
import asyncio
import aiohttp

URLS = ["https://httpbin.org/delay/2" for _ in range(10)]
# httpbin.org/delay/2 responds after 2 seconds (simulates slow API)

# --- Single-thread (sequential) ---
def fetch(url):
    return requests.get(url).status_code

def run_sequential():
    start = time.time()
    for url in URLS:
        fetch(url)
    print("Sequential took:", time.time() - start, "seconds")

# --- Multithreading ---
def run_threads():
    start = time.time()
    threads = []
    for url in URLS:
        t = threading.Thread(target=fetch, args=(url,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("Threads took:", time.time() - start, "seconds")

# --- Asyncio + aiohttp ---
async def fetch_async(session, url):
    async with session.get(url) as resp:
        return resp.status

async def run_async():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, url) for url in URLS]
        await asyncio.gather(*tasks)
    print("Async took:", time.time() - start, "seconds")

if __name__ == "__main__":
    run_sequential()       # ~10 seconds (5 × 2s)
    run_threads()          # ~2–3 seconds
    asyncio.run(run_async())  # ~2–3 seconds
