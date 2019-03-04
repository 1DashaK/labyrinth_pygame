from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return render_template('load.html')
    elif request.method == 'POST':
        f = request.files['file']
        levels = [f for f in os.listdir('maps')]
        num = len(levels)
        return render_template('new_load.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
