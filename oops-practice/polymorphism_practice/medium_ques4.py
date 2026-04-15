# File Handling Simulation
#What to do:
#Create classes PDF, Word, Excel.
#Each has method open() with different messages.

class PDF:
    def open(self):
        print("Opening PDF file")

class Word:
    def open(self):
        print("Opening Word file")

class Excel:
    def open(self):
        print("Opening Excel file")

files = [PDF(), Word(), Excel()]

for f in files:
    f.open()