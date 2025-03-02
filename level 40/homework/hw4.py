# 5) Default Arguments: Define a function that takes a name as input and prints a greeting. If no name is provided, it should use "Guest" as the default.
def greeting (name) :
    if name == "":
        print("hello Guest")
    else:
        print("hello",name)
greeting("")
greeting("Gabrieli")