things i gotta do 

1. **Choose stack**

* HTTP client: `httpx` (async)
* Server: FastAPI
* Cache: Redis (`redis.asyncio`)
* Env: `ORIGIN`, `REDIS_URL`

2. **Cache policy (MVP)**

* Only cache **GET** + **200 OK**
* Respect `Cache-Control: s-maxage | max-age`
* Fall back to `Expires` (HTTP date)
* Ignore `private`, `no-store` (for MVP you may **skip caching** if present)
* Subtract `Age` if present
* No heuristics in MVP (add later)

3. **Keys & TTL**

* Cache key = hash of method+URL + a couple of Vary-like request headers (`Accept`, `Accept-Encoding`)
* Store two keys: `:body` (bytes) and `:meta` (JSON: headers you’ll replay + stored\_at + ttl)
* Set both with `ex=ttl`

4. **Proxy flow**

* On GET:

  * try Redis → hit? return cached
  * miss → fetch with httpx → compute TTL → if cacheable store → return
* Non-GET → just forward (no caching)

5. **Run & test**

* Start Redis
* Run FastAPI (uvicorn)
* Hit the proxy a few times and watch hit/miss
