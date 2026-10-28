import random

# for i in range(50):
#     #random_thingy = random.randint(1, 10)
#     random_thingy = int(random.random() * 10) + 1
#     print(random_thingy)

words = ["what", "is", "me", "table", "paper", "car", "human", "and", "of", "the", 
         "water", "large", "small", "under", "right", "?", ".", "please", "where", 
         "I", "cone", "add", "at", "code", "am", "fire", "upset", "book", "wet", 
         "dry", "grass", "orange", "watermelon", "six", "seven", "one", "zero", 
         "two", "three", "four", "five", "eight", "nine", "original", "child", 
         "baby", "potato", "flying", "random", "space", "where", "was", "Mexico", 
         "next", "antidisestablishmentarianism"]

nouns = ["orange", "watermelon", "plane", "car", "dog", "cat", "lion", "tiger", "Ishaan", "Jerry", "David", "Freda", "Andy", "grass", "smoke", "nugget", "spell", "card", "magic", "horse", "hippo", "potato", "human", "popcorn", "note", "city", "blaster", "son", "daughter", "fence", "wall", "chicken", "bird", "keyboard", "laptop", "computers", "pot", "bucket", "hat", "man", "woman", "men", "women", "table", "poster", "floor", "cup", "tree", "fern"]
verbs = ["adds", "subtracts", "divides", "multiplies", "projects", "runs", "lies", "casts", "spells", "walks", "says", "steals", "is", "hoists", "types", "tears", "sits", "speaks", "talks", "learns", "drives", "pushes", "lifts", "blinks", "writes", "wraps", "holds", "watches", "wears", "thinks"]
adjectives = ["cool", "hot", "tall", "wet", "stolen", "dry", "merry", "cold", "warm", "freezing", "flat", "bumpy", "natural", "scary", "invisible", "visible", "angry", "sad", "dead", "lazy", "working", "blind", "red", "green", "blue", "dark", "bright", "square", "unfortunate", "funny", "heavy", "light", "round"]
articles = ["a", "an", "the"]
conjunctions = ["for", "and", "nor", "but", "or", "yet", "so"]
interjections = ["shh", "wow", "ouch", "yuck", "yay", "hey", "mhm", "look", "what"]
prepositions = ["at", "in", "on", "with", "for", "to", "into"]
subject_pronouns = ["he", "she", "they", "it", "I"]
object_pronouns = ["me", "you", "him", "her", "them", "it"]
posessive_pronouns = ["my", "your", "his", "her", "their", "its"]
punctuation = [".", ",", "!", "?"]


sentence = ""

state = "adj"
noun_counter = 0

for i in range(35):
    #sentence += words[random.randint(0, len(words) - 1)]
    if noun_counter == 2:
        state = "conjunct"
        noun_counter = 0
        
    if state == "noun":
        sentence += nouns[random.randint(0, len(nouns) - 1)]
        state = "verb"
        noun_counter += 1
    elif state == "verb":
        sentence += verbs[random.randint(0, len(verbs) - 1)]
        state = "adj"
    elif state == "adj":
        sentence += adjectives[random.randint(0, len(adjectives) - 1)]
        state = "noun"
    elif state == "conjunct":
        sentence += conjunctions[random.randint(0, len(conjunctions) - 1)]
        state = "adj"
    else:
        pass
    sentence += " "

print(sentence)