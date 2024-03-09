import os, sys
import configparser


_BASE_PATH = sys.path[0]
config = configparser.ConfigParser()
try:
    config.read(os.path.join(_BASE_PATH, "config.ini"), encoding="utf-8")
except FileNotFoundError:
    print("Can't find the config.ini under the entry directory")
