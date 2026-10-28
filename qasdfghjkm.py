import random
import word_maker

# TODO: timer based attacking
#       custom dialogue for enemies
#       classes for player + enemy
#       power ups ?
#       chance of multiple enemies attacking at once ?
#       graphing out attacks
#       online pvp
#       integrate https://jevtypesafeai.com/jev/local into this somehow ???


turns_count = 0
my_health = 100

enemies = {}
enemy_count = random.randint(3, 7)
for i in range(enemy_count):
    enemies[word_maker.getRandomWord()] = random.randint(10, 50)
enemies_name_list = enemies.keys()
enemies_data_list = enemies.values()

print("Enemies:")
for enemy_name, enemy_health in enemies.items():
    print("Enemy: " + enemy_name + ", Health: " + str(enemy_health))
print("")

def isAnyEnemyAlive():
    for enemy_name, enemy_health in enemies.items():
        if enemy_health > 0:
            return True
    return False

while my_health > 0 and isAnyEnemyAlive():
    # find a random enemy to attack us
    attacking_enemy_name = None
    attacking_enemy_health = None
    random_num = random.randint(0, len(enemies) - 1)    
    for i, cur_pair in enumerate(enemies.items()):
        if i == random_num:
            attacking_enemy_name, attacking_enemy_health = cur_pair
    

    my_damage = random.randint(5, 20)
    enemy_damage = random.randint(5, 25)
    print("I did " + str(my_damage) + " points of damage to " + attacking_enemy_name)
    print("Enemy " + attacking_enemy_name + " did " + str(enemy_damage) + " points of damage")

    my_health -= enemy_damage
    enemies[attacking_enemy_name] -= my_damage
    print("I have " + str(my_health) + " health")
    print("Enemy " + attacking_enemy_name + " has " + str(enemies[attacking_enemy_name]) + " health")

    if enemies[attacking_enemy_name] <= 0:
        enemies.pop(attacking_enemy_name)

    input("")

    turns_count += 1

print("Surviving Enemies:")
for enemy_name, enemy_health in enemies.items():
    print("Enemy: " + enemy_name + ", Health: " + str(enemy_health))
print("")

if my_health <= 0:
    print("You died. You suck.")
else:
    print("YOU WON !!!!")
print("Turns passed: " + str(turns_count))