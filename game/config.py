import configparser
import os

def getConfig():
    # If no config file exists, create a default one.
    if not os.path.exists("config.cfg"):
        cp = configparser.ConfigParser()
        cp["SETTINGS"] = {
            "gameserver-ip":"0.0.0.0",
            "gameserver-port":"10000",
            "gameserver-thumbnails-port":"10001",
        }
        with open("config.cfg", "w") as file:
            cp.write(file)

    # Read the config File and return it.
    cp = configparser.ConfigParser()
    cp.read("config.cfg")
    return cp

def createConfig(cfg, name):
    cp = configparser.ConfigParser()
    cp = cfg
    with open(name, "w") as file:
        cp.write(file)

# This creates the default config if the file is run
# manually and if no config exists
if __name__ == "__main__":
    getConfig()