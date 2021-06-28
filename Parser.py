import os
from aetypes import end

'''
parser class
'''


class Parser:
    def __init__(self):
        pass

    def find_file(self, folder, filename):
        print("entering function " + self.find_file.__name__)
        for root, dirs, files in os.walk(folder):
            if filename in files:
                print("\tfile found: " + os.path.join(root, filename))
                print("exiting function " + self.find_file.__name__)
                # exit()
                return True
            else:
                print("."),  # print in the same line
        print("\n\tError: " + folder + '/' + filename + " not found")
        print("exiting function " + self.find_file.__name__)
        return False

    def print_file_content(self, folder, filename):
        print("\nentering function " + self.print_file_content.__name__)
        if self.find_file(folder, filename) is True:
            file_path = folder + '/' + filename
            with open(file_path, 'r') as f:
                print("success: opening file. Now printing the file content")
                print(f.read())
                print("completed printing the file content")
        print("exiting function {0}".format(self.print_file_content.__name__))

    def parse_text(self, folder, filename, text):
        print("\nentering function " + self.parse_text.__name__ + "<" + folder + ',' + filename + ",'" + text + "'>")
        if self.find_file(folder, filename) is True:
            file_path = folder + '/' + filename
            with open(file_path) as f:
                if text in f.read():
                    print("Found text " + text)
        print("exiting function " + self.parse_text.__name__)


# creating object of parser
parse = Parser()

# use case 1: find file in a folder
parse.find_file("/users/Master/Downloads", "file1.doc")

# use case 2: print file content if file is found
parse.print_file_content("/users/Master/Downloads", "file2.doc")

# use case 3: parse the text in the file
parse.parse_text("/users/Master/Downloads", "file2.doc", "Build")
