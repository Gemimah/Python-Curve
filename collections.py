#list: ordered and changebable ,duplicates are OK[]
#set: unordered and immutable duplicates are not allowed{}
#tuple:ordered and unchangeable ,duplicates are OK ()

#shopping cart program

foods = []
prices = []
total = 0

while true:
    food = input("Enter the food to buy(q to quit): ")
    if food ==  "q":
        break
    else :
        price = input("Enter the price of a {food}: $")
        foods.append(food)
        prices.append(prices)