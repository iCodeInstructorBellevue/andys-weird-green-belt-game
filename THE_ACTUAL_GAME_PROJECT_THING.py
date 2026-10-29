import random
import word_maker
import funny_looking_thing

# TODO: timer based attacking
#       custom dialogue for enemies
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
        my_damage = random.randint(5, 20)
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
    # enemies[word_maker.getRandomWord()] = random.randint(10, 50)
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
    

    player.attack(attacking_enemy)
    attacking_enemy.attack(player)
    # my_damage = random.randint(5, 20)
    # enemy_damage = random.randint(5, 25)
    # print("I did " + str(my_damage) + " points of damage to " + attacking_enemy_name)
    # print("Enemy " + attacking_enemy_name + " did " + str(enemy_damage) + " points of damage")

    # my_health -= enemy_damage
    # enemies[attacking_enemy_name] -= my_damage

    # TODO: replace all of the missing vars here with the proper class property names
    print("I have " + str(player.health) + " health")
    print("Enemy " + attacking_enemy_name + " has " + str(enemies[attacking_enemy_name]) + " health")

    # TODO: access .health here instead of comparing directly
    if enemies[attacking_enemy_name] <= 0:
        enemies.pop(attacking_enemy_name)

    input("")

    turns_count += 1

print("Surviving Enemies:")
for enemy_name, enemy_health in enemies.items():
    print("Enemy: " + enemy_name + ", Health: " + str(enemy_health))
print("")

if player.health <= 0:
    print("You died. You suck.")
else:
    print("YOU WON !!!!")
print("Turns passed: " + str(turns_count))