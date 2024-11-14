from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.json
    num1 = data.get('num1')
    num2 = data.get('num2')
    if num1 is None or num2 is None:
        return jsonify({"error": "Please provide num1 and num2 in the request."}), 400
    
    try:
        result = float(num1) + float(num2)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide numeric values."}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
