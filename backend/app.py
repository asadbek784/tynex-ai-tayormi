from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/agents/run', methods=['POST'])
def run_agent():
    data = request.json
    return jsonify({'status': 'success', 'response': f'Tayormi, {data.get("task", "")} bajarildi!'})

if __name__ == '__main__':
    app.run(debug=True)