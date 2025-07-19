
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def fetch_site():
    target_url = request.args.get('getweb')
    if not target_url:
        return jsonify({"error": "Missing 'getweb' parameter"}), 400
    try:
        resp = requests.get(target_url)
        return resp.text, resp.status_code, {'Content-Type': resp.headers.get('Content-Type', 'text/html')}
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
