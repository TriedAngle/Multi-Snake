from flask import Flask, render_template
import socket
from threading import Thread
import pickle


app = Flask(__name__)

@app.route("/")
def index():
    render_template("server/templates/index.html")


class Server:
    def __init__(self):
        self.threads = []
        self.games = []
    def createGame(self, player0Ip, player0Port, player0Sock, player1Ip, player1Port, player1Sock):
        game = {
            "player-0-ip":player0Ip,
            "player-0-port":player0Port,
            "player-0-sock":player0Sock,
            "player-0-dir":"",
            "player-1-ip":player1Ip,
            "player-1-port":player1Port,
            "player-1-sock":player1Sock,
            "player-1-dir":"",
            "game-thread":""
        }

# This thread sends all the available games on the
# Server to everyone that connects to it.
class thumbThread(Thread):
    def __init__(self, ip, port):
        Thread.__init__(self)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((ip, port))
        self.games = []
    def run(self):
        self.s.listen(5)
        while True:
            c, (cIp, cPort) = self.s.accept()
            c.send(pickle.dumps(self.games))

# This thread takes a User's socket as an input and
# receives the direction from him
class userRecvThread(Thread):
    def __init__(self, sock):
        Thread.__init__(self)
        self.dir = []
        self.sock = sock
    def run(self):
        while True:
            self.dir = self.sock.recv(128)

class gameThread(Thread):
    def __init__(self, userSock="", mapname="", username="", gamename="", thumbnailname="", locked=False):
        Thread.__init__(self)
        self.username = username
        self.mapname = mapname
        self.gamename = gamename
        self.userSock = userSock
        with open(thumbnailname, "rb") as f:
            self.thumbnail = f.read()
        self.locked = locked

    def run(self):
        while True:
            pass
