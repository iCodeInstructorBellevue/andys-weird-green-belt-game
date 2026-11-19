import time
import random
import word_maker
import funny_looking_thing

# TODO: custom dialogue for enemies
#       power ups ?
#       graphing out attacks
#       different enemy types
#       online pvp
#       integrate https://jevtypesafeai.com/jev/local into this somehow ???

UNKNOWN = -1
COMMON = 0
OKAY = 1
RARE = 2
EPIC = 3
def getRarityName(rarity):
    if rarity == COMMON:
        return "Common"
    elif rarity == OKAY:
        return "Okay"
    elif rarity == RARE:
        return "Rare"
    elif rarity == EPIC:
        return "Epic"
    else:
        return "Unknown"

class Item:
    name = ""
    icon = ""
    id = 0
    rarity = UNKNOWN

    def __init__ (self, name, icon, id):
        self.name = name
        self.icon = icon
        self.id = id

MONEY = Item("Money", "$", 0)
MYSTERY = Item("Mystery", "?", 1)
BOMB = Item("Bomb", "*", 2)
STICK = Item("Stick", "|", 3)
ITEM_TEMPLATES = [MONEY, MYSTERY, BOMB, STICK]
RARITIES       = [COMMON, OKAY, RARE, EPIC]
RARITY_WEIGHTS = [50,     30,   15,   5] # adds up to 100
def getRandomItem():
    chosen_item_template = random.choice(ITEM_TEMPLATES)
    cloned_item = Item(chosen_item_template.name, chosen_item_template.icon, chosen_item_template.id)
    cloned_item.rarity = random.choices(RARITIES, RARITY_WEIGHTS, k=1)[0]
    return cloned_item

MONEY_BRIBE_CHANCES = [20, 15, 10, 5]
# TODO: fix usage of affectWithItem() down there somewhere
# TODO: do bomb
def affectWithItem(enemies, enemy, player, item):
    if item.name == MONEY.name:
        if random.randint(1, MONEY_BRIBE_CHANCES[item.rarity]) == 1:
            enemy.health = 0
            print("Enemy " + enemy.name + " got bribed and left")
    elif item.name == MYSTERY.name:
        pass
    elif item.name == BOMB.name:
        pass
    elif item.name == STICK.name:
        enemy.health -= 3 * (item.rarity + 1)
    else:
        print("Nothing happened.")

class Player:
    health = 0
    bag = []

    def __init__ (self):
        self.health = 100

    def attack (self, enemy):
        max_dmg = 20
        target_time = 10
        start_time = time.time()
        input("Press enter after "	+ str(target_time) + " seconds: ")
        passed_time = time.time() - start_time
        print("something")

        # david's cursed formula
        #my_damage = 3.33 / ((1/max_dmg/3.333) + abs(passed_time - target_time))
        my_damage = max(0, max_dmg - (passed_time - target_time) ** 2)
        enemy.health -= my_damage
        print("I did " + str(my_damage) + " points of damage to " + enemy.name)

class Enemy:
    name = ""
    avatar = ""
    health = 0

    def __init__ (self):
        self.name = word_maker.getRandomWord()
        self.avatar = funny_looking_thing.getImage()
        self.health = random.randint(10, 50)

    def attack (self, player):
        if self.health > 0:
            enemy_damage = random.randint(5, 25)
            player.health -= enemy_damage
            print("Enemy " + self.name + " did " + str(enemy_damage) + " points of damage")

    


turns_count = 0
# my_health = 100
player = Player()

enemies = {}
enemy_count = random.randint(3, 7)
for i in range(enemy_count):
    cur_enemy = Enemy()
    enemies[cur_enemy.name] = cur_enemy
enemies_name_list = enemies.keys()
enemies_data_list = enemies.values()

print("Enemies:")
for cur_enemy in enemies.values():
    print("Enemy name: " + cur_enemy.name + ", Enemy health: " + str(cur_enemy.health))
print("")

def isAnyEnemyAlive():
    for cur_enemy in enemies.values():
        if cur_enemy.health > 0:
            return True
    return False

while player.health > 0 and isAnyEnemyAlive():
    # find a random enemy to attack us
    attacking_enemy = None
    random_num = random.randint(0, len(enemies) - 1)
    for i, cur_enemy in enumerate(enemies.values()):
        if i == random_num:
            attacking_enemy = cur_enemy

    print(attacking_enemy.avatar)

    chosen_action = input("Choose an action: (attack, lookbag): ")
    if chosen_action == "attack":
        player.attack(attacking_enemy)
    elif chosen_action == "lookbag":
        print("ITEMS:")
        for cur_item in player.bag:
            print("  " + cur_item.icon + " " + getRarityName(cur_item.rarity) + " " + cur_item.name)
       
        is_valid_chosen_item_name = False
        while not is_valid_chosen_item_name:
             chosen_item_name = input("Choose an item (type `exit` to not choose): ")
             if chosen_item_name == "exit":
                 print("You didn't choose anything")
                 break
             for cur_item in player.bag:
                if getRarityName(cur_item.rarity) + " " + cur_item.name == chosen_item_name:
                    attacking_enemy.affectWithItem(cur_item)
                    player.affectWithItem(cur_item)
                    player.bag.remove(cur_item)
                    is_valid_chosen_item_name = True
    else:
        print("You chose to do something dumb so you just took damage :/")

    
    attacking_enemy.attack(player)

    print("I have " + str(player.health) + " health")
    print("Enemy " + attacking_enemy.name + " has " + str(attacking_enemy.health) + " health")

    if attacking_enemy.health <= 0:
        enemies.pop(attacking_enemy.name)
        dropped_item = getRandomItem()
        # dropped_item = random.choice(ITEMS)
        player.bag.append(dropped_item)
        print("Enemy " + attacking_enemy.name + " dropped a " + getRarityName(dropped_item.rarity) + " " + dropped_item.name)

    #input("")

    turns_count += 1

print("Surviving Enemies:")
for cur_enemy in enemies.values():
    print("Enemy: " + cur_enemy.name + ", Health: " + str(cur_enemy.health))
print("")

if player.health <= 0:
    print("You died. You suck.")
else:
    print("YOU WON !!!!")
print("Turns passed: " + str(turns_count))