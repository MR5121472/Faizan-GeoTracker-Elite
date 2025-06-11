import os
import time

def start_ngrok():
    os.system("killall ngrok")
    os.system("termux-open-url https://github.com/inconshreveable/ngrok")
    os.system("./ngrok http 5000 > /dev/null &")
    time.sleep(3)
    os.system("curl -s http://127.0.0.1:4040/api/tunnels | grep -o 'https://[0-9a-z]*\\.ngrok.io'")
