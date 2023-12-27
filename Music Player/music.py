from playsound import playsound
from pygame import mixer
import os

playlist = []

def addSong ():
    print("\n\nList of songs: ")
    directory = os.getcwd() + '/Music Player/'
    for file in os.listdir(directory):
        if (file.endswith(".wav")):
            print("- " + file.split(".")[0])

    song = input("\nEnter the song name you would like to add to the playlist: ")
    song = song + ".wav"
    
    if (os.path.exists(directory + song)):
        playlist.append(song)
        print("\nCurrent playlist: ")
        print(playlist)
    else:
        print("Song does not exist!")



if __name__ == '__main__':
    addSong()