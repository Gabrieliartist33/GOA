# 7) Write a function that takes a list of numbers and checks whether each number is even or odd using a loop and conditional statements. Print "Even" for even numbers and "Odd" for odd numbers.
def even_or_odd (arr) :
    for i in arr:
        if i % 2 == 0 :
            print("even")
        else:
            print("odd")
even_or_odd([56,67,80,63])