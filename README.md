# basicServer
 
A lightweight HTTP server built from scratch in Python using raw TCP sockets — no frameworks, no `http.server` module, no abstractions. Built for a Computer Networks course to demonstrate how HTTP actually works at the transport layer.
 
## What It Does
 
- Opens a TCP socket bound to `127.0.0.1:8040`
- Listens for incoming client connections (up to 5 queued)
- Manually parses the raw HTTP request to extract the method, path, and headers
- Serves `index.html` in response to a `GET /` request
- Constructs and sends a valid HTTP/1.1 response by hand, including status line and headers
- Loops continuously to handle successive client connections
## Why It Matters
 
Most web developers interact with HTTP through frameworks like Flask, Express, or Django — tools that hide the underlying protocol entirely. This project strips all of that away. Every byte of the request and response is handled manually, which means understanding:
 
- How TCP connections are established and torn down
- How HTTP requests are structured (request line, headers, body)
- How a server constructs a valid HTTP response
- What `SO_REUSEADDR` does and why it matters during development
## How to Run
 
**Requirements:** Python 3.x
 
1. Clone the repository
   ```bash
   git clone https://github.com/SpeerGabe/basicServer.git
   cd basicServer/http-server/http-server
   ```
 
2. Start the server
   ```bash
   python server.py
   ```
 
3. Open your browser and navigate to `http://127.0.0.1:8040`
The server will print incoming HTTP request headers to the terminal so you can see the raw request your browser sends.
 
## Project Structure
 
```
http-server/
└── http-server/
    ├── server.py     # Core server logic — socket setup, request parsing, response handling
    └── index.html    # Static page served on GET /
```
 
## Technical Details
 
| Property | Value |
|---|---|
| Protocol | HTTP/1.1 |
| Transport | TCP (IPv4) |
| Address | 127.0.0.1:8040 |
| Language | Python 3 |
| Dependencies | None (stdlib only) |
 
## Course Context
 
Built for CSCI Computer Networks at UT Martin. The goal was to understand the HTTP request/response cycle by implementing it at the socket level rather than relying on higher-level libraries.
 
