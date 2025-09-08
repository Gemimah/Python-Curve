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

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")
    



