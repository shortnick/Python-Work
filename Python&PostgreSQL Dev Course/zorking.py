from pprint import pprint

spare_rooms = [
    ["entry", 0, [1, 2, 3, 4], "Exits at 1, 2, 3, 4", "It's a room with 4 doors", ["It echoes faintly in here",
                                                                                   "Nothing to see here"]],
    ["vestibule", 1, [0, 2], "Exits to entry and front room", "It's a bare hallway", ["The tiles are scuffed and dirty.",
                            "Move along"]],
    ["parlor", 2, [0, 1, 3], "Exits to the entry, the vestibule, and the den",
     "There's some sad, saggily upholstered furniture", "don't look too close"]
]

rooms_all = []


class Room:
    def __init__(self, *args):
        for name, rooms_id, exits, exits_text, descrip, detail in args:
            self.name = name
            self.rooms_id = rooms_id
            self.exits = exits
            self.exits_text = exits_text
            self.descrip = descrip
            self.detail = detail
            # add these later
            # self.items = [] things you can pick up
            # self.interacts = [] interactive components
            # self.specials = [] room specific functions

    def exit_check(self, door_selection):
        if door_selection in self.exits:
            return True

    def look_detail(self):
        return self.detail[0]


def menu():
    here = rooms_all[0]

    choice = input("options: look - see the room, \n"
                   "exits - see the exits from the room, \n"
                   "go to 9 - use the numbered exit, \n"
                   "quit - leave the program, \n "
                   "please make a selection - - ")

    while choice != "quit":
        print("Room {}, choice {}".format(here.name, choice[0:4]))
        if choice == "exits":
            print(here.exits_text)
        elif choice[0:2] == "go":
            door = int(choice[-1])
            if here.exit_check(door):
                here = rooms_all[door]
        elif choice[0:5] == "looks":
            print("\n ", here.descrip, "\n ")
        elif choice[4:5] == "@":
            print("\n ", here.look_detail(), "\n ")
        else:
            print("Hmm. Try again.")

        choice = input("options: \n"
                       "looks - see the room, \n"
                       "look@ - see a random detail, \n"
                       "exits - see the exits from the room, \n"
                       "go to 9 - use the numbered exit, \n"
                       "quit - leave the program, \n "
                       "please make a selection - - ")


# call the rooms in the list into being
# run menu
# go between rooms
for x in spare_rooms:
    y = Room(x)
    # print(y.look(), y.exits)
    # pprint(vars(y))
    rooms_all.append(y)

# pprint(vars(rooms_all[0]))
# print(2 in rooms_all[0].exits)
# print(rooms_all[0].exits)
# exit_check(rooms_all[0],2)
menu()
