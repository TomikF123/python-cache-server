

import argparse
import server
parser = argparse.ArgumentParser()


def main():
    parser = argparse.ArgumentParser(description="Caching Proxy Server")
    subparsers = parser.add_subparsers(dest='command')

    start_parser = subparsers.add_parser('start', help='Start the caching proxy server')
    start_parser.add_argument('--port', type=int, required=True, help='Port number')
    start_parser.add_argument('--origin', type=str, required=True, help='Origin URL')

    clear_parser = subparsers.add_parser('clear-cache', help='Clear the cache')

    args = parser.parse_args()
    print(args.port,args.origin)
   # server.start_server()
    if args.command == 'start':
        print("Starting Server with port: "+str(args.port)+" at origin: "+str(args.origin))
        server.start_server(port=args.port, origin=args.origin)

if __name__ == "__main__":
    main()