# User defined functions

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")
    
    greet("Mosh", "Hamedani")
    greet("John","Smith")
    
    #Types of functions
    #1- Perform a task
    #2- Return a value
    
    def greet(name):
        print(f"Hi {name}")
        
        def get_greeting(name):
            return f"Hi {name}"
        
        message = get_greeting("Mosh")
        file = open("context.txt", "w")
        file.write(message)
        
        def increment(number, by=1):
            return number +by
        print(increment(2))
        
        def multiply(*numbers):
            total = 1
            for number in numbers:
                total *= number
                return total
            print(multiply(2,3,4,5))
                        
        
    



        
