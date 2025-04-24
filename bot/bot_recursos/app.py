from flask import Flask, render_template

import threading

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
