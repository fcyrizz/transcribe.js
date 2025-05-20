from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add the required Cross-Origin headers
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        
        # Optional: Add other CORS headers if needed
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        
        super().end_headers()

def run(server_class=HTTPServer, handler_class=CORSRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    print(f"Serving files with Cross-Origin headers:")
    print(f"  Cross-Origin-Embedder-Policy: require-corp")
    print(f"  Cross-Origin-Opener-Policy: same-origin")
    httpd.serve_forever()

if __name__ == '__main__':
    run()