# import time
# import asyncio
# import sys

# async def printPassedTime(start_time):
#     while True:
#         print(str(time.time() - start_time))
#         await asyncio.sleep(0.1)

# async def asyncInput():
#     cur_loop = asyncio.get_running_loop()
#     return (await cur_loop.run_in_executor(None, sys.stdin.readline)).strip()

# async def main():
#     cur_time = time.time()
#     bg_thingy = asyncio.create_task(printPassedTime(cur_time))
#     await asyncInput()
#     bg_thingy.cancel()
#     passed_time = time.time() - cur_time
#     print(str(passed_time))
#     if passed_time > 5 and passed_time < 6:
#         print("u win")
#     else:
#         print("u lose")
# asyncio.run(main())

# -------------------------------------------------

import time

cur_time = time.time()
input()
passed_time = time.time() - cur_time
print(str(passed_time))

if passed_time > 5 and passed_time < 6:
    print("u win")
else:
    print("u lose")