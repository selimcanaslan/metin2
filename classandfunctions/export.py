import os
from file_create_message import file_created


def export(self):
    file_exists = os.path.isfile("log.txt")
    print(file_exists)
    if file_exists:
        item1_full = self.item_combo.currentText() + " " + self.won_line_1.text()
        file = open("log.txt", "w")
        file.write("This is line %d\r\n" % item1_full)
    else:
        file = open("log.txt", "w+")
        file.write("This is line\r\n")
        file_created()
