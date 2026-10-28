import random

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# vowels = ["a", "e", "i", "o", "u"]
# stuff = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "qu", "r", "s", "t", "v", "w", "x", "y", "z"]

def getRandomWord():
    word = ""
    word_len = random.randint(1, 20)

    # state = "notvowel"

    for i in range(word_len):
        # # not vowel
        # if state == "notvowel":
        #     word += stuff[random.randint(0, len(stuff) - 1)]
        #     state = "vowel"
        # # vowels
        # elif state == "vowel":
        #     word += vowels[random.randint(0, len(vowels) - 1)]
        #     state = "notvowel"
        word += alphabet[random.randint(0, len(alphabet) - 1)]
        
    return word
    # print(word)