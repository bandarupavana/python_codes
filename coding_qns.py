#rapido,uber:
#km?
#1-6 per km 5rs
#7-12 per km 6rs
#13-20 per km 8rs
#21-30 per km 10rs
#greater than 30 --> ride not possible
'''
testcase:
case1: 10 km
amount: 30+24=54

case2: 15km
amount: 30+36+24 = 90
'''
'''
print("WELCOME TO RAPIDO")
print("-------------------------")
km = int(input("Enter total km: "))
price = []
if km >= 1 and km <= 6:
    price.append(30)
elif km >= 7 and km <= 12:
    price.append(30)
    price.append((km - 6) * 6)
elif km >= 13 and km <= 20:
    price.append(30)
    price.append(36)
    price.append((km - 12) * 8)
elif km >= 21 and km <= 30:
    price.append(30)
    price.append(36)
    price.append(64)
    price.append((km - 20) * 10)
else:
    print("Ride not possible")
#if km >= 1 and km <= 30:
amount = sum(price)
print("Price details:", price)
print("Total amount:", amount)
'''
#====================OR=======================
'''
km = int(input("Enter km: "))

if km >= 1 and km <= 6:
    amount = km * 5
    print("Amount:", amount)

elif km >= 7 and km <= 12:
    amount = (6 * 5) + (km - 6) * 6
    print("Amount:", amount)

elif km >= 13 and km <= 20:
    amount = (6 * 5) + (6 * 6) + (km - 12) * 8
    print("Amount:", amount)

elif km >= 21 and km <= 30:
    amount = (6 * 5) + (6 * 6) + (8 * 8) + (km - 20) * 10
    print("Amount:", amount)

elif km > 30:
    print("Ride not possible")

else:
    print("Invalid km")

'''
#=================================
#toy shop: 1. which type , 2. price
#we sell batter base, more than 500rs wll give wire toy free and 5% discount
#wire base, for every 300rs bought need to give -- dist: reduce 50 rs
#wireless toys, 1. purchase more than 2k purchase give 20% discount
#2. more than 5k 30% disc

'''testcases:
battery:500
500-475+wiretoy  ---> 25rs

wir 900-150=750

wirless --> 5k-3500'''
'''
#--------------------find where is the student---------------------
#college
#block
#floor
#class
college=input("have u seen student in college? reply with yes or no: ")
if college=="yes":
    block=input("have u seen student in block? reply with yes or no: ")
    if block=="yes":
        floor=input("have u seen student in floor? reply with yes or no: ")
        if floor=="yes":
            classes=input("have u seen student in class? reply with yes or no: ")
            if classes=="yes":
                print("student is in class!")
            else:
                print("student is in some floor!")
        else:
            print("student is in block!")
    else:
        print("student is in college!")
else:
    print("student didn't come to college!")
    '''

'''
#this down code is done by me but it shouldnt consider 2 inputs like i m taking now for that chk the below code:
----------LIFT-----------------
up,down -- total 6 floors
baisc which floor ur in now =4
up 3 -- we cant move as it is 7th floor
up 2 -- reached to 6th floor
down 6 -- we cant move
down 4 -- reached ground floor
'''
'''
total=6
options=int(input('1.up 2.down: '))
curr=int(input("which floor ur in: "))
move=int(input("how many floors u wanna move: "))
if options==1:
    curr=curr+move
    if curr>total:
        print("we cant move")
    else:
        print(f" moved to {curr} floor")
else:
    curr=curr-move
    if curr<0:
        print("we cant move")
    else:
        print(f"moved to {curr} floor")
    
#in the below way we need to split the single input and consider'''
'''
floor = int(input("Enter current floor: "))
msg = input("Enter direction and floors: ")
direction, num = msg.split()
num = int(num)
if direction == "up":
    result = floor + num
    if result >= 1 and result <= 6:
        print(result)
    else:
        print("can't move")
elif direction == "down":
    result = floor - num
    if result >= 1 and result <= 6:
        print(result)
    else:
        print("can't move")
else:
    print("Invalid Direction")

'''
'''
#restaurant bill generation
res_name="keerthana restaurant"
print(res_name.center(30))
print("_____________________________")
date="20-11-2026"
print("date: ",date)
name="PAVANA SANDHYA"
print("name: ",name)
food_items={'prawn starter': 350.0,'butter naan': 400.0,'chicken biryani': 750.0,'raspberry mojitho' : 175.0}
print(*food_items.items(),sep="\n")
print((*food_items.keys(),sep="\n"),"            ",(*food_items.values(),sep="\n"))
'''

# TOY SHOP BILLING SYSTEM
'''
# List
toy_categories = ["battery", "wire", "wireless"]

# Tuple
battery_offer = (500, 5)
wire_offer = (300, 50)
wireless_offer = (2000, 20, 5000, 30)

# Set
available_toys = {"battery", "wire", "wireless"}

# Dictionary
offers = {
    "battery": "5% discount for every Rs.500 + 1 free wire toy",
    "wire": "Rs.50 discount for every Rs.300",
    "wireless": "20% discount above Rs.2000 and 30% above Rs.5000"
}

print("WELCOME TO TOY SHOP")
print("-------------------")

print("Available Toy Categories:")
print(toy_categories)

toy_type = input("Enter toy category: ").strip().lower()

if toy_type in available_toys:

    amount = float(input("Enter purchase amount: "))

    discount = 0
    free_toys = 0

    if toy_type == "battery":

        blocks = amount // battery_offer[0]

        discount = blocks * (battery_offer[0] * battery_offer[1] / 100)

        free_toys = int(blocks)

    elif toy_type == "wire":

        blocks = amount // wire_offer[0]

        discount = blocks * wire_offer[1]

    elif toy_type == "wireless":

        if amount >= wireless_offer[2]:
            discount = amount * wireless_offer[3] / 100

        elif amount >= wireless_offer[0]:
            discount = amount * wireless_offer[1] / 100

        else:
            discount = 0

    final_amount = amount - discount

    # Dictionary for bill details
    bill = {
        "Toy Category": toy_type,
        "Purchase Amount": amount,
        "Discount": discount,
        "Free Wire Toys": free_toys,
        "Final Amount": final_amount
    }

    print("\n--------- BILL ---------")
    print(*bill.items(), sep="\n")
    print("------------------------")

    print("Thank you for shopping!")

else:
    print("Invalid toy category!")
    print("Please select battery, wire or wireless.")

'''


# RAPIDO RIDE BOOKING SYSTEM

# List
vehicles = ["scooty", "auto", "car"]

# Set
available_vehicles = {"scooty", "auto", "car"}

# Dictionary: Vehicle prices for each slab
vehicle_rates = {
    "scooty": (5, 6, 8, 10),
    "auto": (8, 10, 12, 15),
    "car": (12, 15, 18, 22)
}

# Dictionary: Available coupon codes
coupons = {
    "RAPIDO10": 10,
    "FIRST20": 20,
    "SAVE15": 15
}

print("WELCOME TO RAPIDO")
print("-----------------")

print("Available vehicles:")
print(vehicles)

vehicle = input("Select your vehicle: ").strip().lower()

if vehicle in available_vehicles:

    km = int(input("Enter distance in km: "))

    if km >= 1 and km <= 6:
        amount = km * vehicle_rates[vehicle][0]

    elif km >= 7 and km <= 12:
        amount = (6 * vehicle_rates[vehicle][0]) + \
                 ((km - 6) * vehicle_rates[vehicle][1])

    elif km >= 13 and km <= 20:
        amount = (6 * vehicle_rates[vehicle][0]) + \
                 (6 * vehicle_rates[vehicle][1]) + \
                 ((km - 12) * vehicle_rates[vehicle][2])

    elif km >= 21 and km <= 30:
        amount = (6 * vehicle_rates[vehicle][0]) + \
                 (6 * vehicle_rates[vehicle][1]) + \
                 (8 * vehicle_rates[vehicle][2]) + \
                 ((km - 20) * vehicle_rates[vehicle][3])

    elif km > 30:
        print("Ride not possible")
        amount = -1

    else:
        print("Invalid km")
        amount = -1

    if amount >= 0:

        print("\n----- RIDE DETAILS -----")
        print("Vehicle:", vehicle)
        print("Distance:", km, "km")
        print("Original Fare: Rs.", amount)

        has_coupon = input("Do you have a coupon? (yes/no): ").strip().lower()

        discount = 0

        if has_coupon == "yes":

            coupon = input("Enter coupon code: ").strip().upper()

            if coupon in coupons:
                discount = amount * coupons[coupon] / 100
                print("Coupon Applied:", coupon)
                print("Discount:", discount)

            else:
                print("Invalid coupon code!")

        elif has_coupon == "no":
            print("No coupon applied.")

        else:
            print("Invalid choice. No coupon applied.")

        final_amount = amount - discount

        print("\n------- FINAL BILL -------")
        print("Vehicle:", vehicle)
        print("Distance:", km, "km")
        print("Original Fare: Rs.", amount)
        print("Discount: Rs.", discount)
        print("Final Amount: Rs.", final_amount)
        print("-------------------------")
        print("Thank you for choosing Rapido!")

else:
    print("Invalid vehicle selection!")





