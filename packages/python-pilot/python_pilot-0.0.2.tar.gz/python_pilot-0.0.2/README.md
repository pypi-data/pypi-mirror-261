# PyPilot
A python terminal copilot.</br>
Use PyPilot as a regular python terminal and whenever you need the copilot assistance just write it as a comment.</br>
Don't forget to set the API KEY (supports only OPENAI for now).

## Installation
```
pip install pypilot
```

## Usage
```bash
pypilot --api-key sk-....
```
or
```bash
OPENAI_API_KEY=sk-... pypilot
```

## Examples
```
Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
============
PyPilot 0.0.2 - Python terminal with llm agent
- Use comments (#) to communicate with the agent.
- The agent is aware to the terminal history and locals.
- Type reset(), clear(), history(), ulocals(), dump() or set_api_key() for custom commands.
- When prompt to approve, any key will approve, ctrl+c will cancel.

>>> # hi
LLM[tokens:~430]>
Hello! How can I help you with Python today?
>>> # show me how to create a simple HTTP server with no external deps
LLM[tokens:~484]>
```python
import http.server
import socketserver

# Define the request handler class
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, World!")  # Response message

# Create an HTTP server with the defined handler
with socketserver.TCPServer(("", 8000), MyHttpRequestHandler) as httpd:
    print("Server started at http://localhost:8000")
    httpd.serve_forever()
```
EXECUTE?>
Server started at http://localhost:8000
```

# TODO
- add a way to use history only with headers of functions...
- add command lien support with ! mark
- handle missing imports in runtime
    - install and always remove when closing the app
    - docker containers
- add a selector step that decide what context the next llm prompt should have:
    - history: code executed (w/wo expressions), errors, llm requests
    - locals: vars, functions, modules
 (full terminal history, locals only) and if the output should be code or chat