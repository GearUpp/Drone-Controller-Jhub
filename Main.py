import re
grid_size = 11
global file_location, current_lococation,rows

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
rows = open(text1, "r").read().splitlines()
print(rows)

x = 0
y = 0

def fileinput():   # Initial function to read user input and decide next step
    global file_location, rows
    while True:
        file_location = str(input("Enter the full path to the route file (or type STOP to exit): "))
        if re.search(r".txt",str(file_location)):       # change later to file_location
            rows = open(file_location, "r").read().splitlines()
            formatting() # Will run after a path with .txt is provided
        elif file_location.lower().strip() == "stop":
            print("Exiting Drone simulation.")
            break
    exit   



def formatting():
    global x,y, current_lococation,file_location
    try:
        with open(file_location, 'r') as file:
            row = row in file
            print(row)
            print(row)
            x = int(row.pop([0]))
            print(row)
            y = int(row.pop([0]))
            current_lococation = set()
            print("ok")
            print("Starting coordinates are:  X:", x , " -   Y: ", y)
        print(row.count("W"))
        print("ok")
        moving(x,y,row)
    except:
        print("failed to format and create x / y inital location")



def moving(x_initial,y_initial,rows):  # Will Calculate and create the
    print("Running Formatter")
    global current_lococation,file_location, x,y
    try:
        for direction in rows:
            if direction == "N":
                y += 1
            elif direction == "S":
                y -= 1
            elif direction == "E":
                x += 1
            elif direction == "W":
                x -= 1
            else:
                print(direction , " not used")
            if not (0 <= y < grid_size and 0 <= x < grid_size):
                print("drone lost at Co-ordinates:", x, " - ", y)
            else:
                current_lococation.add((x, y))
            grid_generator(x_initial,y_initial,rows)
    except:
        print("Faile to process file")




def grid_generator(x_initial,y_initial,rows): #once rows and initial position is calculated, a grid can be generated
    print("Printing Grid")
    error = False
    coords = []
    for col in range(grid_size):
        for rows in reversed(range(grid_size)):
            print()





fileinput()  # Once all functions are loaded, loop of functions can begin
