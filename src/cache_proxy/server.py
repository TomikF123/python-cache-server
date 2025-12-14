import uvicorn
from cache_proxy.config import settings
from typing import Optional
server_instance:uvicorn.Server = None
def start_server(port: int, origin: str) -> None:
    """Start the caching proxy server."""
    # Update global settings
    settings.port = port
    settings.origin = origin
    global server_instance
    # Start the server
    from cache_proxy.main import app
    config = uvicorn.Config(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )
    server_instance = uvicorn.Server(config)
    server_instance.run()

def stop_server()->None:
    global server_instance
    if server_instance:
        
        server_instance.should_exit = True