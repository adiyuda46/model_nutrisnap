from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>xxx Welcome to the Greeting API</h1>"

@app.route('/greet', methods=['GET'])
def greet_get():
    name = request.args.get('name')
    if name:
        return jsonify({"message": f"Hi, {name}!"})
    else:
        return jsonify({"error": "Please specify a name in the 'name' query parameter."}), 400

@app.route('/greet', methods=['POST'])
def greet_post():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON."}), 400
    
    name = data.get('name')
    if name:
        return jsonify({"message": f"Hi, {name}!"})
    else:
        return jsonify({"error": "Please specify a name in the 'name' field of the JSON body."}), 400

if __name__ == '__main__':
    app.run(debug=True)
