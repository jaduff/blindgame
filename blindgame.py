#game load and main gameplay loop
import pyttsx3 #library used for speech support
engine = pyttsx3.init() #initialise the speech library

from room import loadRooms

gameStatus = 1 #status 1 for game to run, Status 0 to quit game
visionImpaired = 0
heaingImapired = 0

rooms = loadRooms()
room = {}


def output(output):
    if (visionImpaired == 1):
        engine.say(output)
        engine.runAndWait()
    else:
        print(output)


def startGame():
    #get room from save file. If no save, start at beginning
    newGame = 1
    if (newGame == 1):
        room = rooms.get(1)
    return(room.get("commands").get("arrive"))

output(startGame())

while (gameStatus == 1):
    cmd = input()
    if (cmd.lower() == "quit"):
        gameStatus = 0
