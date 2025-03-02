# 9) Define a function that takes a list of integers and returns a new list containing only the positive numbers. Use a loop and a conditional statement.
def positiv_nums(arr) :
    arr2 = []
    for i in arr :
        if i > 0 :
            arr2.append(i)
    print(arr2)
positiv_nums([23,-20,50])
