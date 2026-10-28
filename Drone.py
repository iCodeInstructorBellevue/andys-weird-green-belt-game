from easytello import tello

my_drone = tello.Tello()

# # my_drone.takeoff()
# # my_drone.ccw(360)
# # my_drone.forward(100)
# # my_drone.right(100)
# # my_drone.cw(180)
# # my_drone.right(100)
# # my_drone.forward(100)
# # my_drone.land()


# my_drone.takeoff()
# my_drone.forward(50)
# my_drone.cw(90)
# my_drone.forward(50)
# for i in range(4):
#     my_drone.cw(90)
#     my_drone.forward(100)
# my_drone.cw(90)
# my_drone.forward(50)
# my_drone.cw(90)
# my_drone.forward(50)
# my_drone.land()

for i in range(2):
    my_drone.takeoff()
    my_drone.sleep(2)
    my_drone.right(150)
    my_drone.land()