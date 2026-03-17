from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    target_url = request.args.get('url') or 'https://google.com'
    
    resp = requests.get(target_url, stream=True, timeout=30)
    
    headers = {}
    for key, value in resp.headers.items():
        if key.lower() not in ['content-encoding', 'transfer-encoding', 'content-length']:
            headers[key] = value
            
    return Response(resp.content, status=resp.status_code, headers=headers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
