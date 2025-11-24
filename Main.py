import re
grid_size = 12
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

x = 1
y = 1

def fileinput():   # Initial function to read user input and decide next step
    global file_location, rows

    while True:
        try:
            file_location = str(input("Enter the full path to the route file (or type STOP to exit): "))
            #file_location = text1             #For testing purpose
            if re.search(r".txt",str(file_location)):       
                rows = open(file_location, "r").read().splitlines()
                formatting() # Will run after a path with .txt is provided

            elif file_location.lower().strip() == "stop":
                print("Exiting Drone simulation.")
                break
        except:
            print("Wrong File name / direcotry, try again")
    exit   



def formatting():   # Will create a starting place from rows list. and confirm its in range of grid + continue to moving fun
    global x,y, current_lococation,file_location,rows

    try:
        x = int(rows.pop(0))
        y = int(rows.pop(0))

        current_lococation = set()
        current_lococation.add((x, y))


        if y > grid_size or x > grid_size or y <= 0 or x <= 0:
            print("Starting coordinates are:  X:", x , " -   Y: ", y  , ". Are not possible and out of range of grid")
            fileinput()
        else:
            print("Starting coordinates are:  X:", x , " -   Y: ", y)
        moving(x,y,rows)

    except:
        print("failed to format and create x / y inital location")



'''         ^
        N = x + 1 
 < W = x - 1    E = x + 1 >
        S = y - 1
            ↓
'''

def moving(starting_x,starting_y,rows):  # Will add up all the directions into 

    global current_lococation,file_location, x,y
    try:
        print(current_lococation)
        for i in rows:
            i = str(i.upper())
            if i == "N":
                y += 1
            elif i == "E":
                x -= 1
            elif i == "S":
                y -= 1
            elif i == "W":
                x += 1
            else:
                print(i , " not used")
            if y > grid_size or x > grid_size or y <= 0 or x <= 0:
                print()
                print("******** Drone out of bounds Co-ordinates:", x, " - ", y, " ********")
                print()

                current_lococation.add((x, y))
                grid_generator(starting_x,starting_y,rows,current_lococation)
            else:
                current_lococation.add((x, y))
        grid_generator(starting_x,starting_y,rows,current_lococation)
    except:
        print("Faile to process file")




def grid_generator(x_initial,y_initial,rows_list,current_lococation): #once rows and initial position is calculated, a grid can be generated
    print("  Y  :")
    print("Rows :----:----:----;----:----:----:----:----:----:----:----:----:")
    for rows in reversed(range(grid_size)):

        print("  {:02d} :".format(rows + 1) , end="")   # Fix top part
        for col in range(grid_size):
            if (col + 1,rows + 1) in current_lococation: 
                print(" >< :", end="")
            else:
                print("    :", end="")
        print("\n","----:----:----:----:----:----:----:----:----:----:----:----:----:")

    print("Column  1 :  2 :  3 :  4 :  5 :  6 :  7 :  8 :  9 : 10 : 11 : 12 :  X  :")
    fileinput()



fileinput()  # Once all functions are loaded, loop of functions can begin
#          .txt
