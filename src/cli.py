import argparse
import sys
import uvicorn
from cache_proxy.config import settings
import cache_proxy.server as server


# cli.py
def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    
    # Start server
    start_parser = subparsers.add_parser('start')
    start_parser.add_argument('--port', type=int, required=True)
    start_parser.add_argument('--origin', type=str, required=True)
    
    # Clear cache (via API call)
    clear_parser = subparsers.add_parser('clear-cache')
    clear_parser.add_argument('--port', type=int, default=3000)
    
    # Stats
    stats_parser = subparsers.add_parser('shutdown')
    stats_parser.add_argument('--port', type=int, default=3000)
    
    args = parser.parse_args()
    
    if args.command == 'start':
        server.start_server(args.port, args.origin)
    
    elif args.command == 'clear-cache':
        # Call the management API
        import requests
        response = requests.post(f"http://localhost:{args.port}/admin/clear_cache")
        print(response.json())
    
    elif args.command == 'shutdown':
        import requests
        response = requests.post(f"http://localhost:{args.port}/admin/shutdown")
        print(response.json())