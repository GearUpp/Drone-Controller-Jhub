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

X = 0
Y = 0

def fileinput():
    while True:
        global file_location
        file_location = input("Enter the full path to the route file (or type STOP to exit): ")
        if re.search("(.txt)",str(fileinput) ):
            file_formating() # Will run after a path with .txt is provided
            exit
        elif file_location.lower().strip() == "stop":
            print("Exiting Drone simulation.")
            exit

fileinput()



def file_formating():
    print("Running Formatter")
    global current_lococation,x,y,file_location
    try:
       with open(file_location, 'r') as file:
           row = [row for row in file if row.strip()]
           x = int(row[0])
           y = int(row[1])
           current_lococation = set()
           print(f" Starting coordinates are: ({x}, {y})")

           for direction in lines[2:]:
               direction = direction.upper()
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
                   curentLocation.add((x, y))
           fileinput()
    except:
        print("Faile to process file")

print(current_lococation)
print(file_location)



fileinput()
