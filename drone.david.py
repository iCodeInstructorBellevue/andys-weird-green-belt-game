from easytello import tello
from time import sleep #in a bed lol
my_drone = tello.Tello()

def flyToTable(table_to_table_whatever_distance_uh):
    my_drone.takeoff()
    sleep(3)      #stops code for 3 seconds
    my_drone.forward(table_to_table_whatever_distance_uh)
    my_drone.down(20)
    my_drone.land()

def flyOverAFewTables(do_how_many_times, how_far_apart):
    for i in range(do_how_many_times):
        flyToTable(how_far_apart)

# for x in range(2):      #repeating it 2 times
#     doThing(260)

flyToTable(100)
flyToTable(150)
flyToTable(90)
flyToTable(170)

flyOverAFewTables(5, 200)

flyToTable(70)
flyToTable(50)
flyToTable(300)

flyOverAFewTables(5, 100)