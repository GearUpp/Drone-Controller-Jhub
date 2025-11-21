import re

grid_size = 11
global file_location, current_loc

text1 = './Route001.txt'
text03 = './Route003.txt'

'''
Will use text files above stored locally for testing,
They look something like this, initial two values are starting position, 
then subsiquentyly the direction of travel in N E W S directions.
3
12
S
S
W
S

'''

X = 0
Y = 0

def fileinput():
    while True:
        global file_location
        file_location = input("Enter the full path to the route file (or type STOP to exit): ")
        if re.search("(.txt)",fileinput ):
            file_formating() # Will run after a path with .txt is provided
            exit
        elif file_location.lower().strip() == "stop":
            print("Exiting Drone simulation.")
            exit

fileinput()



def file_formating():
    print("Running Formatter")


    