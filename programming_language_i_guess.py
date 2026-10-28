import turtle

turtdraw_file = open("thingy.turtdraw", "rt")
file_stuff = turtdraw_file.read()

list_of_lines = file_stuff.split("\n")
t = turtle.Turtle()

for cur_line in list_of_lines:
    words = cur_line.split()
    command = words[0]
    if command == "size":
        t.pensize(int(words[1]))
    elif command == "forward":
        t.forward(int(words[1]))
    elif command == "right":
        t.right(int(words[1]))
    elif command == "color":
        t.color(words[1])
    elif command == "back":
        t.back(int(words[1]))
    elif command == "left":
        t.left(int(words[1]))
    elif command == "goto":
        t.goto(int(words[1]), int(words[2]))
    elif command == "penup":
        t.penup()
    elif command == "pendown":
        t.pendown()
    else:
        print("ERROR, unrecognized command: " + command)
    

turtle.done()
turtdraw_file.close()




# TODO: make this thing work (translate the turtdraw script into Turtle commands)
#       `pensize` `forward`, `back`, `left`, `right`, `goto`, `color`, `size`, `penup`, `pendown`
