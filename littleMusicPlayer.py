from tkinter import *
from pygame import mixer
import os

p = Tk()
p.overrideredirect(True)
p.geometry("58x30+0+0")
p.configure(background='grey')
p.attributes("-topmost", True)
onPause = True

directory = "adress to your music directory"

listOfSongs= []
songIndex = 0

file = "test.mp3"
mixer.init()

def fileChooser():
    os.chdir(directory)
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listOfSongs.append(files)
    mixer.music.load(directory+"/"+listOfSongs[songIndex])

fileChooser()
print(listOfSongs)
mixer.music.play()
mixer.music.pause()

def onPlayButtonClick():
    global onPause
    global songIndex
    if onPause:
        mixer.music.unpause()
        onPause = False
    else:
        mixer.music.pause()
        onPause = True
def onPreButtonClick():
    global songIndex
    if songIndex == 0:
        songIndex = len(listOfSongs) - 1
    else:
        songIndex = songIndex - 1
    mixer.music.load(directory + "/" + listOfSongs[songIndex])
    mixer.music.play()
def onNextButtonClick():
    global songIndex
    if songIndex == len(listOfSongs)-1:
        songIndex = 0
    else:
        songIndex = songIndex + 1
    mixer.music.load(directory + "/" + listOfSongs[songIndex])
    mixer.music.play()

previousButton = Button(p, text="<", command=onPreButtonClick)
previousButton.pack(padx=1, pady=2, side=LEFT)
playButton = Button(p, text="|", command=onPlayButtonClick)
playButton.pack(padx=1, pady=2, side= LEFT)
nextButton = Button(p, text=">", command=onNextButtonClick)
nextButton.pack(padx=1, pady=2, side= LEFT)

p.mainloop()
