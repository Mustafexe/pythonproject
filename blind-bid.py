import sys
import os
last_bidder=False
bid_dictionary = {}
while not last_bidder:
    name = input("What is your name ")
    bid = int(input("What is your bid $"))
    check_bidders = input("Are there any other bidders 'Yes' or 'No' ").lower()
    if check_bidders=="no":
        last_bidder=True
    else:
        sys.stdout.flush()
        os.system("cls")
    bid_dictionary[name]=bid
max=bid_dictionary[name]
person1=""
for person in bid_dictionary:
    if bid_dictionary[person]>= max:
        max=bid_dictionary[person]
        person1=person
print(f"The winner is {person1} with a bid of ${max}")



