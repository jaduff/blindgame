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

def changeRoom(room):
    #logic to change room
    return None

def action(room, _action):
    action = room.get("commands").get(_action)
    atype = action.get("type").lower()
    if (action.get("type") == "alias"):
        action = room.get("commands").get(_action.get("command"))
    if (action.get("valid") == "first"):
        #change valid to none in savefile
        pass
    elif (action.get("valid") == "none"):
        return None
    if (atype == "text"):
        output(action.get("text"))
    elif (atype == "exit"):
        changeRoom(action.get("room"))
    elif (atype == "get"):
        output(action.get("text"))
        #get object to inventory somehow
    else:
        return(action)




def startGame():
    #get room from save file. If no save, start at beginning
    newGame = 1
    #attempt load of save file, if fail assume new game. Otherwise load?
    if (newGame == 1):
        room = rooms.get("1")
    action(room, "arrive")
    action(room, "help")

startGame()

while (gameStatus == 1):
    cmd = input()
    if (cmd.lower() == "quit"):
        gameStatus = 0
    else:
        if (room.get("commands").get(cmd).get("type") == "alias"):
            action(room, cmd)
        