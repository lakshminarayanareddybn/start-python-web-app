from flask import Flask, request, jsonify

app = Flask(__name__)

# Addition API
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return jsonify({'result': result})

# Subtraction API
@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 - num2
    return jsonify({'result': result})

# Multiplication API
@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 * num2
    return jsonify({'result': result})

# Division API
@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    if num2 == 0:
        return jsonify({'error': 'Division by zero is not allowed.'}), 400
    result = num1 / num2
    return jsonify({'result': result})

# Table API
@app.route('/table', methods=['POST'])
def table():
    data = request.get_json()
    num = data['num1']
    if num <= 0:
        return jsonify({'error': 'Table for zero or less is not allowed.'}), 400

    table_list = []
    for i in range(1,11):
        table_list.append(num * i)
    return jsonify({'result': table_list})

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8083, debug=True)
