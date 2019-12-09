#functions (or classes) for rooms

#probably better to switch to uuid - blind friendly?
def loadRooms():
    rooms = {"1": {"commands":{
                    "arrive": {"type": "text",
                                "text": "You slowly open your eyes, despite a throbbing headache",
                                "valid": "all"},
                    "help": {"type": "text",
                                "text": "For gamplay hints, type help, follwed by the enter key",
                                "valid": "once"},
                    "east": {"type": "exit",
                            "room": 2,
                            "valid" : "all"},
                    "feel": {"type": "text",
                            "text": "You feel around you. You are on a cold, concrete floor, surrounded by metal shelves. There is a door to the east.",
                            "valid": "all"},
                    "feel shelf": {"type": "alias",
                                    "command": "feel shelves"},
                    "feel shelves": {"type": "text",
                                    "text": "you feel around the shelves, and find a dowel pole.",
                                    "valid": "all"},
                    "get pole": {"type": "get",
                                "text": "You pick up the pole",
                                "item": "dowel_powel", #replace with uuid
                                "valid": "once"}
                    }

                }
    }
    return rooms