my_thingy_dictionary_whatever = {"apple": "a fruit or computer thing", 
                                 "computer": "thing that does thing",
                                 "table": "a flat thing that yoy can stand on ??",
                                 67: "hmmmmmmmmmmmmmmmmmmmmmmmm"}
print(my_thingy_dictionary_whatever["table"])
my_thingy_dictionary_whatever["table"] = "sample text"
print(my_thingy_dictionary_whatever["table"])
print(my_thingy_dictionary_whatever[67])

print("")

my_fake_dictionary = [["apple", "a fruit or computer thing"],
                      ["computer", "thing that does thing"],
                      ["table", "a flat thing that yoy can stand on ??"],
                      [67, "hmmmmmmmmmmmmmmmmmmmmmmm"]]
for word_pair in my_fake_dictionary:
    if word_pair[0] == "table":
        print(word_pair[1])

# my_thingy_dictionary_whatever["table"] = "sample text"
# print(my_thingy_dictionary_whatever["table"])
# print(my_thingy_dictionary_whatever[67])