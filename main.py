from datetime import datetime
import re

InMemoryDB = []
date_input = input()
plate = input()

class Action:
    def __init__(self, date: datetime, plate):
        self.date = date
        self.plate = plate

    def print(self):
        print("[" + self.date.strftime("%Y-%m-%d") + "] " + self.plate)
    def to_db(self):
        return {"date":self.date.strftime("%Y-%m-%d"), "plate": self.plate}

try:
    date = datetime.strptime(date_input, "%Y-%m-%d")
except ValueError:
    print("error: date")
    exit()

plate_pattern = r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$'
if not re.match(plate_pattern, plate):
    print("error: plate")
    exit()

a = Action(date, plate)
a.print()
InMemoryDB.append(a.to_db())
print("DB :",InMemoryDB)