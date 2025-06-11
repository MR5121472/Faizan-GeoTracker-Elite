from banner import banner
import threading
import os

def start_server():
    os.system("python server.py")

def start_ngrok():
    os.system("python ngrok.py")

banner()
threading.Thread(target=start_server).start()
threading.Thread(target=start_ngrok).start()
