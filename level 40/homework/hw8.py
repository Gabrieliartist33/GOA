# 8) Find the Maximum: Create a function that takes a list of numbers and uses a loop to find and return the maximum number.
def max_num(arr) :
    max_value = arr[0]
    for i in arr :
      if i > max_value :
         max_value = i
    print(max_value)
max_num([56,78,89,13,24])