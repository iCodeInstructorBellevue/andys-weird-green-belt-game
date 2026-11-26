import time

pressed_count = 0
limit_seconds = 5
start_time = time.time()
while time.time() - start_time < limit_seconds:
    input()
    if time.time() - start_time < limit_seconds:
        pressed_count += 1
print("Pressed " + str(pressed_count) + " times in " + str(limit_seconds) + " seconds")