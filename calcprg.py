#python calculator

"""operator = input("Enter an operator(+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(result)
    
elif operator == "-":
    result = num1-num2
    print(result)
    
elif operator == "*":
    result = num1*num2
    print(result)
    
elif operator == "/":
    result = num1/num2
    print(result)"""



import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0, -1):
    print(x)
    time.sleep(1)
    
    print()
    
