from flask import Flask, request, send_file, jsonify
from processing import remove_white_background

app = Flask(__name__)


@app.route('/process', methods=['POST'])
def process():
    pass
