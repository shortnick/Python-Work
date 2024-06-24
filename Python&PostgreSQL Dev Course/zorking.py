"""
see also:   https://blog.trinket.io/python-text-adventure/
            https://www.makeuseof.com/python-text-adventure-game-create/

Things to do:
- add logging and userout functions
- create text files for each room, which feed into the class generator
    make template for Room csv
    read in as CSV, with a specific symbol separating items in *args
- modify Room class to take a CSV as instantiation, including a grabber func to add room specific methods
    CSV https://realpython.com/python-csv/#parsing-csv-files-with-pythons-built-in-csv-library
- fix door->room/exit usage in menu, maybe tied to ID?
    number exits in the description "1 - a splintery wooden door, 2 - a heavy iron grate"
    keep a dictionary in self.exits = {1:"den", 2:"hall", 3:"salon"}, use the dictionary name to grab rooms by name from
    rooms_all?
- expand/refine the look around/get detail functions of Room objects
    list of things that can be looked at, tied to specific noun or adjective, can be simple text or Item
    check Item list from Room first, then Item list in backpack, return description
    if no, check Room details dictionary keys for keywords, return dict value for matching hit
    else "Can't see that thing. Try again. Be clear and specific."
- figure out how to add room-specific functions
- store room functions (and item list?) under separate files?
- write Item class, with carry/stationary element
- write Character class, keep backpack, has basic qualities functions (eg hypothermia)
    backpack needs a list all things func
- make rooms so they add items, but not items that are in the backpack
    all specifically lookable things are Items?
- figure out how to call ascii art with the room text
- add ascii art to each room: https://www.asciiart.eu/image-to-ascii
- methods for Use_Item or Use_Item_On
"""

from pathlib import Path
import sys
import logging
import csv

rooms_all = []

backpack = []

def useroutput():
    print()

spare_rooms = [
    ["entry", 0, [1, 2, 3, 4], "Exits at 1, 2, 3, 4", "It's a room with 4 doors", ["It echoes faintly in here",
                                                                                   "Nothing to see here"],
    """    
    null
    """],
    ["vestibule", 1, [0, 2], "Exits to entry and front room", "It's a bare hallway", ["The tiles are scuffed and dirty.",
                            "Move along"],"null"],
    ["parlor", 2, [0, 1, 3], "Exits to the entry, the vestibule, and the den",
     "There's some sad, saggily upholstered furniture", "don't look too close","null"]
]



class Item:
    def __init__(self, *args):
        for item_id, name, carry, desc in args:
            "ID is for game use, name is for users, carry is T/F for being able to take, desc is for description"
            self.id = item_id
            self.name = name
            self.carry = carry
            self.desc = desc

    def item_describe(self):
        return self.name

    def take_item(self):
        if self.carry==False:
            backpack.append(self)
            print("{} added to backpack.".format(self.name))
        else:
            print("Hmmm. That's not going in the backpack.")


class Room:
    def __init__(self, *args):
        for name, rooms_id, exits in args:
            "name is string, ID is numeric, exits is list of numbers"
            self.name = name
            self.rooms_id = rooms_id
            self.exits = exits
            logging.info("Room class-{} construction".format(name))

        base_path = str(Path(__file__).parent)
        csv_path = base_path+"\\"+str(name)+".txt"
        logging.debug("Room constructor for {} opened {}".format(name, csv_path))

        data = []
        with open(csv_path) as csv_file:
            csv_reader = csv.reader(csv_file)
            holder=[]
            for x in csv_reader:
                if '%' not in x:
                    holder.append(x)
                elif '%' in x:
                    for y in holder:
                        data.append(y)
                    holder = []
                logging.debug(x)

            logging.debug("data -")
            logging.debug(data)
        self.items = data[0]
        "need item constructor here?"
        self.exits_text = data[1]
        self.descrip = data[2]
        self.details = data[3]
        self.ascii_art = data[4]
        logging.debug("Room constructor-{} finished".format(name))


    def exit_check(self, door_selection):
        if door_selection in self.exits:
            return True

    def item_check(self, thing):
        if thing in self.items:
            return True

    def look_detail(self):
        return self.details[0]


def menu():
    here = rooms_all[0]
    print(here.ascii)
    print(here.descrip, "\n")
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

        print("\n",here.descrip,"\n")

        choice = input("options: \n"
                       "looks - see the room, \n"
                       "look@ - see a random detail, \n"
                       "exits - see the exits from the room, \n"
                       "go to 9 - use the numbered exit, \n"
                       "quit - leave the program, \n "
                       "please make a selection - - ")


# call the rooms in the list into being
entry = Room(("entry", 0, [1]))
vestibule = Room(("vestibule", 1, [0,2,3,4]))
parlor = Room(("parlor", 2, [1,4]))
kitchen = Room(("kitchen", 3, [1,5]))
study = Room(("study", 4, [1,2]))

# run menu
# go between rooms


# pprint(vars(rooms_all[0]))
# print(2 in rooms_all[0].exits)
# print(rooms_all[0].exits)
# exit_check(rooms_all[0],2)
menu()
