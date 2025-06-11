from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/log', methods=['POST'])
def log():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logger.txt", "a") as file:
        file.write(f"[{now}] IP: {ip} | UA: {ua}\n")

    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
