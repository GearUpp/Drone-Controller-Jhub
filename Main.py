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
    global file_location
    while True:
        file_location = str(input("Enter the full path to the route file (or type STOP to exit): "))
        if re.search(r".txt",str(file_location)):
            print("Passed")
            formatting() # Will run after a path with .txt is provided
        elif file_location.lower().strip() == "stop":
            print("Exiting Drone simulation.")
            break
    exit   



def formatting():
    global x,y, current_lococation,file_location
    try:
        with open(file_location, 'r') as file:
            row = [row for row in file if row]
            x = int(row[0])
            y = int(row[1])
            current_lococation = set()
            print("Starting coordinates are:  X:", x , " -   Y: ", y)
        moving(x,y,row)
    except:
        print("failed to format and create x / y inital location")



def moving(x_initial,y_initial,rows):  # Will Calculate and create the
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
           print(x)
           print(y)
           grid_generator(x_initial,y_initial,rows)
    except:
        print("Faile to process file")




def grid_generator(x_initial,y_initial,rows): #once rows and initial position is calculated, a grid can be generated
    print("Printing Grid")
    error = False
    coords = []
    for col in range(grid_size):
        for rows in reversed(range(grid_size)):
            


fileinput()  # Once all functions are loaded, loop of functions can begin
