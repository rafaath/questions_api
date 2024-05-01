# api/reverse.py

from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send a response to GET requests
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Welcome to the Reverse API!".encode())

    def do_POST(self):
        # Read the request body
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # Process the input text (assume JSON input)
        try:
            data = json.loads(post_data)
            input_text = data.get('text', '')
            # Reverse each word
            reversed_text = ' '.join(word[::-1] for word in input_text.split())
            
            # Create response
            response = {
                "original_text": input_text,
                "reversed_text": reversed_text
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        except Exception as e:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"error": str(e)}
            self.wfile.write(json.dumps(response).encode())
