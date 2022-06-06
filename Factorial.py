number = int(input("Please enter a number: "))
factorial = 1

if number<0:
    print("Factorial for negative numbers does not exist!")
elif number==0:
    print("0! = 1")
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print(str(number)+"! = " + str(factorial))