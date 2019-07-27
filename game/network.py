import socket
from threading import Thread
from game.config import getConfig, createConfig
import pickle
import os

def createImageFromPickle(img, name):
    with open(name, "wb") as f:
        f.write(img)

def state_menuRecvThumbnails():
    # First, we retrieve the Server ip and thumbnail port
    cfg = getConfig()
    server_ip = cfg["gameserver-ip"]
    server_thumb_port = cfg["gameserver-thumbnails-port"]

    # Second, we create a socket and try to connect to the Server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect((server_ip, server_thumb_port))
            break
        except:
            pass

    # Now, we receive all the Thumbnails and Info from the Server
    data = pickle.loads(s.recv(512 ** 4))

    # They will be saved as [{"thumbnail":..., "mapname":...,
    # "gamename":..., "username":..., "locked":...}]
    return data, s

class NetworkManager(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.states = {
            "idle":"",
            "menuRecvThumbnails":self.gameStateGetThumbs,
            "menuRecvMap":self.gameStateGetMap,
            "game":""
        }
        self.state = "idle"
        self.loadedThumbnails = False
        self.gamenames = []
        self.usernames = []
        self.mapnames = []
        self.thumbsocket = None
        self.selectedGame = 0
        self.gotMap = False

    def run(self):
        while True:
            self.states[self.state]()

    def gameStateIdle(self):
        pass

    def gameStateGetThumbs(self):
        self.loadedThumbnails = False
        data, s = state_menuRecvThumbnails()
        self.thumbsocket = s
        for i in range(len(data)):
            thumb = data[i]["thumbnail"]
            createImageFromPickle(thumb, "tmp_thumb_menu{}.png".format(i))
            self.gamenames.append(data[i]["gamename"])
            self.usernames.append(data[i]["username"])
            self.mapnames.append(data[i]["mapname"])
        self.loadedThumbnails = True
        self.state = "idle"

    def gameStateGetMap(self):
        self.gotMap = False
        if not os.path.exists("assets/map/{}/".format(self.mapnames[self.selectedGame])):
            self.thumbsocket.send(str(self.selectedGame).encode())
            data = pickle.loads(self.thumbsocket.recv(512 ** 4))
            createImageFromPickle(data["map"], "assets/maps/{}/map.png".format(self.mapnames[self.selectedGame]))
            createImageFromPickle(data["map-settings"], "assets/maps/{}/map-settings.png".format(self.mapnames[self.selectedGame]))
            createConfig(data["config"], "assets/maps/{}/config.cfg".format(self.mapnames[self.selectedGame]))
        self.gotMap = True