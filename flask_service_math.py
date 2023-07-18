from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    """
    index
    """
    return "This is Home Page"

@app.route('/math', methods=['POST'])
def add_entry():
    """
    add_entry
    """
    print("p0")
    request_json = request.get_json()
    print(request_json)
    operation = request_json.get('operation')
    values = request_json.get('values')
    sum1 = 0
    if operation is not None and values is not None:
        print("operation:", operation)
        if(operation == "+"):
            if len(values) > 0:
                for item in values:
                    sum1 += item
        
    return str(sum1)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8083, debug=True)