from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route("/")
def proxy():
    url = request.args.get("url")
    if not url:
        return "Add ?url=https://example.com to access any site"
    
    try:
        r = requests.get(url, stream=True, timeout=30)
        headers = {k: v for k, v in r.headers.items() 
                  if k.lower() not in ["content-encoding", "transfer-encoding", "content-length"]}
        return Response(r.content, status=r.status_code, headers=headers)
    except:
        return "Site failed to load", 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
