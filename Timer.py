import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0,-1):
    seconds = x % 60
    minutes= int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    
    print("TIME'S UP!")
    
    # nested loops = A loop within another loop (outer,inner)
    rows = int(input("Enter number of rows: "))
    columns = int
    for x in range(3):
        for x in range(1,10):
            print(y, end="")
            print()
        