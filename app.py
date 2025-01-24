from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    my_name = os.getenv('MY_NAME', 'robot')
    return f'<h1>{my_name}</h1>'


if __name__ == "__main__":
    app.run(debug=True)
