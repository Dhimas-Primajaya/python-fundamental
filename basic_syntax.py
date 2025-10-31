"""
All basic programming languages syntax include:
1. Sequential: Sequential steps
2. Branching: Jump steps if  condition is true(fulfilled)
3. Looping: loop same steps until the condition is true(fulfilled)
"""

# Sequential
print('Mom said, "Go to the shop"')
print('Budi Answered, "Ok, what should I do in the shop?"')
print('Mom Answered, "Go buy a bottle of milk, and if there are eggs, buy 6 eggs"')
print('Then Budi went to the shop and started buying\n')

# Branching
money = 43
milk_bottle_count = 150
eggs_count = 750
milk_price = 25
eggs_price = 18
total = eggs_price + milk_price
# print(total)

print(f"Milk bottle count = {milk_bottle_count}")
print(f"Eggs count = {eggs_count}")
print(f"Milk price = ${milk_price}")
print(f"Eggs price = ${eggs_price}\n")

if milk_bottle_count > 0 and money >= milk_price:
    print("Budi checked up his money and it's enough to buy it")
    print(f"Money count = ${money}\n")
    if eggs_count > 0 and money >= total:
        print("Budi Buying a bottle of milk and 6 eggs\n")
    else:
        print("Budi Buys a bottle of milk\n")
else:
    print("Budi didn't buy a bottle of milk\n")

print("Budi went to home")
print("He handed over the shopping result to his mom")