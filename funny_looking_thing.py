import random

def getImage():
    imageStr = ""
    for i in range(6):
        for j in range(6):
            if random.randint(0, 1) == 0:
                imageStr += "██"
            else:
                imageStr += "  "
        imageStr += "\n"
    return imageStr

# print(getImage())