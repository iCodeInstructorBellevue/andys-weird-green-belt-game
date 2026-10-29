class Dog:
    name = "Default Dog name or something"
    color = "Invisible"
    age = -1
    size = -1

    def __init__(self, name, age, color, size):
        self.name = name
        self.age = age
        self.color = color
        self.size = size

    # Instance method
    def bark(self):
        print(self.name + " says Woof!")

    def bite(self, person_name):
        print(self.name + " bit " + person_name + " and " + person_name + " died :(")

    # String representation method
    def __str__(self):
        return self.name + " is " + self.age + " years old."