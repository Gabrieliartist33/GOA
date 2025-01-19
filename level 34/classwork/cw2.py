# შექმენით ფუნქცია სახელად sum_or_multiply, რომელსაც ექნება 2 პარამეტრი - num1 და num2. # თუ num1 მეტია 50-ზე, დაბეჭდეთ Num1 გამრავლებული num2-ზე, სხვა შემთხვევაში დაბეჭდეთ num1 + num2. ფუნქცია გამოიძახეთ 3-ჯერ, განსვავებული არგუმენტებით
def sum_or_multiply(num1, num2):
    if num1 > 50:
        print(num1*num2)
    else:
        print(num1+num2) 
print(2*3)
print(43+23)
print(5+7)