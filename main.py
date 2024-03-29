from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bid={}
continue_bid=True
def highest_bid():
  max_bid=0
  for bidder in bid:
    a=bid[bidder]
    if a>max_bid:
      max_bid=a
      winner=bidder
  print(f"The winner is {winner} with highest bid of {max_bid}")
while continue_bid:
  name=input("What is your name? ")
  bid_price=int(input("What is your bid price? $"))
  bidders=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  bid[name]=bid_price
  if bidders=="yes":
    clear()
  elif bidders=="no":
    continue_bid=False
    highest_bid()