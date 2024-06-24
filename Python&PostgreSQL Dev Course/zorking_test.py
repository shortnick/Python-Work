"""instantiate room with specific methods and pull in a CSV from outside
use CSV for descriptions, text art, included items
use Room to say which exits, IDs
"""

from pathlib import Path
import sys
import logging
import csv


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)],
)

class Room:
    def __init__(self, *args):
        for (name, rooms_id, exits) in args:
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
                    logging.debug(holder)
                    if '%' not in x:
                        holder.append(x)
                    elif '%' in x:
                        logging.debug("% found")
                        for y in holder:
                            data.append(y)
                        holder = []
                    logging.debug(x)

                logging.debug("data -")
                logging.debug(len(data))
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



entry = Room(("entry", 0, [1]))


