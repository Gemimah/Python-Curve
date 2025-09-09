print("Hello World")
print("*" * 10)

# indicating a comment
#\'
#\\
course = "python programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[:3])
print(course)

first = "Mosh"
last="Hamedani"
full=f"{len(first)} {2+2}"
print(full)
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("pro"))
print(course.replace("p","j"))
print("pro" in course)
print("swift" not in course)

print(10+3)
print(10-3)
print(10*3)

temperature = 15
if temperature >30:
    print("It's warm")
    print("Drink water")
elif temperature >20:
    print("It's nice")
else:
    print("It's cold")
    print("Done")
    
    age = 22
    if age>=18:
        message = " Eligible"
        
    else:
        message = "Not Eligible"
        
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
    
    # age should be between 18 and 65
    

if 18 <= age < 65:
    print("Eligible")

# using if, elif
if 10 == 10:
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
    
    for number in range(3):
        print("Attempt mumberp.y+ 1r +1, "),
        successful = False
        for number in range(3):
            print("Attempt")
            if successful:
                print("successful")
                break
            
            else:
                print("Attempted 3 times and failed")
                for x in range(5):#outer loop
                    for y in range(3):#Inner loop
                        print(f"({x},{y})")
                        
                        #using loops
                        
                        for number in range(1,10,2):
                            print("Attempt", number ,number  *".")
                            
                            #iterables
                    print(type(5))
                    print(type(range(5)))
                    
                    for x in range(5):
                        
                        for item in shopping_cart:
                            print(item)
                            
                            #while loops
                            
                            number = 100
                            while number > 0:
                                print(number)
                                number //=2
                                
                                #infinite loops
                                
                                while True:
                                    command = input(">")
                                    print("ECHO", command)
                                    if command.lower() == "quit":
                                        break
                                
                               
                        
                        
            

        
    



