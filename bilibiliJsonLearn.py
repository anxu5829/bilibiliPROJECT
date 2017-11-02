import os
import json

os.chdir("C:\\Users\\22560\\PycharmProjects\\bilibiliPROJECT")


f = open("indy.json")

jsonFile = json.load(f)

f.close()

jsonFile['indy movies'][0]