#Typecasting = the process of converting a variable from one data type to another
# str(), int(),float(),bool()

name = "Gemimah"
age = 25
gpa= 3.2
is_student = True

print(type(is_student))

gpa = int(gpa)

age = str(age)
print(type(age))
name = bool(name)
print(name)

#input() = A function that prompts the user to enter data and returns the entered data as a string

name = input("What is your name?: ")

age = input("How old is you?: ")
age = int(age)
age = age +1
print(f"Hello {name}")
print("HAPPY BIRTHDAY !")
print(f"You are {age} years old")

# Area of a rectangle

length =float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area is:{area} cm")

# Shopping Cart Program

item = input("What item would you like: ")
price = input("What is the price?: ")
quantity = input("How many would you like?: ")

total= price*quantity
print(total)

