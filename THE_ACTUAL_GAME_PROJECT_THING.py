import time
import random
import word_maker
import funny_looking_thing

# TODO: custom dialogue for enemies
#       classes for player + enemy
#       power ups ?
#       graphing out attacks
#       different enemy types
#       online pvp
#       integrate https://jevtypesafeai.com/jev/local into this somehow ???

class Player:
    health = 0

    def __init__ (self):
        self.health = 100

    def attack (self, enemy):
        max_dmg = 20
        target_time = 10
        start_time = time.time()
        input("Press enter after " + str(target_time) + " seconds: ")
        passed_time = time.time() - start_time

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

    player.attack(attacking_enemy)
    attacking_enemy.attack(player)

    print("I have " + str(player.health) + " health")
    print("Enemy " + attacking_enemy.name + " has " + str(attacking_enemy.health) + " health")

    if attacking_enemy.health <= 0:
        enemies.pop(attacking_enemy.name)

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