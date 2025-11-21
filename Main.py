import re

grid_size = 11
global file_location, current_lococation

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

x = 0
y = 0

def fileinput():   # Initial function to read user input and decide next step
    while True:
        global file_location
        file_location = input("Enter the full path to the route file (or type STOP to exit): ")
        if re.search("(.txt)",str(fileinput) ):
            formatting() # Will run after a path with .txt is provided
            exit
        elif file_location.lower().strip() == "stop":
            print("Exiting Drone simulation.")
            exit



def formatting():
    global x,y, current_lococation
    try:
        with open(file_location, 'r') as file:
            row = [row for row in file if row]
            x = int(row[0])
            y = int(row[1])
            current_lococation = set()
            print("Starting coordinates are:", x , " -  ", y)
        moving(x,y,row)
    except:
        print("failed to format and create x / y inital location")



def moving(x_initial,y_initial,rows):
    print("Running Formatter")
    global current_lococation,file_location, x,y
    try:

           for direction in rows[2:]:
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
                   
                   print(f"drone lost at Co-ordinates: ({x}, {y})")
                   break
               else:
                   current_lococation.add((x, y))
           print(x_initial, " ", y_initial)
           print(rows)
           grid_generator(x_initial,y_initial,rows)
           fileinput()
    except:
        print("Faile to process file")

print(current_lococation)
print(file_location)

def grid_generator(x_initial,y_initial,rows): #once rows and initial position is calculated, a grid can be generated
    print("Printing Grid")
    error = False
    coords = [()]
    for rows in range(grid_size):
        print(rows)


fileinput()  # Once all functions are loaded, loop of functions can begin
