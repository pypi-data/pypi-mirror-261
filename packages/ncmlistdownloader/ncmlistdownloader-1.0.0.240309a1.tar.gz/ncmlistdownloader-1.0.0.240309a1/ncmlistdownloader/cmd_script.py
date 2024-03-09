'''
ncmlistdownloader/cmd_script.py
Core.Ver.1.0.0.240309a1
Author: CooooldWind_
'''
import time
import pprint
import multiprocessing
import ncmlistdownloader as nld

def main():
    print("163ListDownloader CMD Ver.")
    print("Core.Ver.1.0.0.240309a1 / Made by CooooldWind_")
    print("Warning: It's an Alpha Version.")
    multiprocessing.freeze_support()
    p = nld.Playlist()
    id = str(input("ID/Url: "))
    d = str(input("Dir: "))
    fnf = str(input("Filename format: "))
    p.get_resource(id)
    print("Playlist info-reading succeed.")
    for i in p.tracks:
        print("Downloading:" + str(i.id['id']))
        i.get_resource()
        print("Music info-reading succeed.")
        i.initialize(0, fnf, d)
        print("Initialized.")
        # ap = multiprocessing.Process(target = i.start_single())
        # ap.start()
        i.start_single()
        print("Succeed.")