from flask import Flask
from src.logger import logging

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info("Testing")
    return "Welcome to A new Project"


if __name__ == "__main__":
    app.run(debug=True)
