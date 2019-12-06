#functions (or classes) for rooms

def loadRooms():
    rooms = {"1": {"commands":{
                    "arrive": {"type": "text",
                                "text": "You slowly open your eyes, despite a throbbing headache",
                                "valid": "all"}
                                ,
                    "east": {"type": "exit",
                            "room": 2,
                            "valid" : "all"}
                    }
                }
    }
    return rooms