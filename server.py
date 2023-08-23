from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

CANVAS_URL = "https://canvas.instructure.com/api/v1"

@app.route('/assignments', methods=['GET'])
def get_assignments():
    api_key = request.args.get('api_key')
    api_id = request.args.get('api_id')
    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(f"{CANVAS_URL}/courses/{api_id}/assignments", headers=headers)
    
    if response.status_code != 200:
        return jsonify(error="Failed to fetch assignments"), 400

    assignments = [{"name": a["name"], "due_at": a["due_at"]} for a in response.json()]
    return jsonify(assignments)

if __name__ == '__main__':
    app.run(debug=True)
