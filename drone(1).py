from easytello import tello

my_drone = tello.Tello()

for i in range(2):
    my_drone.takeoff()
    my_drone.left(260)
    my_drone.land()

number = 1
if number < 9:
    print("ok")
    print("um")
print("asias")

if number < 19:
    print("erm")

if number < 8:
    print("oh")
elif number < 19:
    print("sausai")
elif number < 48:
    print("uewuiewuiew")
else:
    print("uh")
    print("guh")