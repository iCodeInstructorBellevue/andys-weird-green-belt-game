my_dictionary = {
    "Apple": "Red crunchy fruit",
    "Banana": "Yellow peely fruit",
    "Grape": "Small juicy fruit",
    "Strawberry": "Red sweet fruit",
    "Watermelon": "Big watery fruit"
}

my_dictionary["Pear"] = "Funny apple"

del my_dictionary["Pear"]

my_dictionary.clear()

student_grades = {
    "Alex": 89,
    "Brandon": 45,
    "Carly": 74,
    "Darren": 67,
    "Ethan": 99,
    "Frank": 95
}

for name in student_grades.keys():
    continue
    print(name)

for grade in student_grades.values():
    continue
    print(grade)

for name, grade in student_grades.items():
    continue
    print(f"{name} got a {grade} on the test!")

my_dict1 = {
    "mydict2": {"Apple": "Fruit"}
}

print(my_dict1)
print(my_dict1["mydict2"])
print(my_dict1["mydict2"]["Apple"])


student_info = {
    "Alex": {
        "Age": 7,
        "Grade": 87
    },
    "Brandon": {
        
    },
    "Carly": {

    },
    "Darren": {

    },
    "Ethan": {

    },
    "Frank": {

    }
}