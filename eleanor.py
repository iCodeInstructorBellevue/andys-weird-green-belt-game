from easytello import tello 
from time import sleep

my_drone = tello.Tello()

for x in range(1):
    my_drone.takeoff()
    sleep(1)
    my_drone.forward(257)
    sleep(1)
    my_drone.land()