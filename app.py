from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "This is Home Page"

@app.route("/hello")
def hello():
    return "This is hello, world page"
# static

# @app.route("/Ajay")
# def welcome():
#     return "Welcome Ajay, what is your order"

# @app.route("/C B Shukla")
# def greet():
#     return "Welcome C B Shulka ji, what is your plan for today"

# dynamic

# @app.route('/<name>')
# def namaskara(name):
#     return f'welcome {name}. What would you like to order.'

# # route param

# @app.route('/post/<id>')
# def show_post(id):
#     return f'Post ID is: {id}'

# @app.route('/product/<name>')
# def get_prodcut(name):
#     return 'Product is  :' + name

# @app.route('/sale/<transaction_id>')
# def get_sale(transaction_id = 0):
#     return 'The trasaction is ' + str(transaction_id)

# # multiple param
# @app.route('/create/<first_name>/<last_name>')
# def create(first_name=None, last_name=None):
#     return 'Hello ' + first_name + last_name

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8083, debug=True)