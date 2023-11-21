import itertools

x=[
    ["entry", 0, [1, 2, 3, 4], "Exits at 1, 2, 3, 4", "It's a room with 4 doors", "Nothing to see here"],
    ["vestibule", 1, [0, 2], "Exits to entry and front room", "It's a bare hallway", "Move along"],
    ["parlor", 2, [0, 1, 3], "Exits to the entry, the vestibule, and the den",
     "There's some sad, saggily upholstered furniture", "don't look too close"]
]

def func(*args):
    print(len(args))

#print(len(x[0][2]))

class Room:
    def __init__(self, *args):
        for name, id, exits, exit_text, descrip, detail in args:
            self.name = name
            self.id = id
            self.exits = exits
            self.exit_text = exit_text
            self.descrip = descrip
            self.detail = detail




testing = Room(x[0])
print(testing.name, testing.id, testing.detail)