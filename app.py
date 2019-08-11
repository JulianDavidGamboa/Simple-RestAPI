from flask import Flask

app = Flask(__name__)

from products import products


@app.route('/ping')
def ping():
    return 'Pong!'


if __name__ == '__main__':
    app.run(debug=True, port=4000)
