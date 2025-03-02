# 10) Write a function that iterates through a range of numbers (e.g., 1 to 100) and sums up all the numbers divisible by 3. Return the total sum.
def sum_3 (range1) :
    arr1 = []
    for i  in range1 :
        if i % 3 == 0 : 
            arr1.append(i)
    print(sum(arr1))
sum_3(range(1,10))