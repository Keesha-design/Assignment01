import prices
print("Use any of the following product codes")
print("mlk-->MILK,brd-->BREAD,sug-->SUGAR,mlo-->MILO,lpt-->LIPTON,bsc-->BISCUIT,swt-->SWEET,gum-->CHEWING GUM,cks-->COOKIES,drk-->DRINK")
item=input("Enter item you wish to buy ")
qty=input("Enter the quantity ")

if item=="mlk":
  price=prices.MILK
  total=int(qty)*price
  print("The Total price for total number of milk is :",total)
  
if item=="brd":
  price=prices.BREAD
  total=int(qty)*price
  print("The Total price for total number of bread is :",total)
  
if item=="sug":
  price=prices.SUGAR
  total=int(qty)*price
  print("The Total price for total number of sugar is :",total)
  
if item=="mlo":
  price=prices.MILO
  total=int(qty)*price
  print("The Total price for total number of milo is :",total)
  
if item=="lpt":
  price=prices.LIPTON
  total=int(qty)*price
  print("The Total price for total number of lipton is :",total)
  
if item=="bsc":
  price=prices.BISCUIT
  total=int(qty)*price
  print("The Total price for total number of biscuit is :",total)
  
if item=="swt":
  price=prices.SWEET
  total=int(qty)*price
  print("The Total price for total number of sweet is :",total)
  
if item=="gum":
  price=prices.GUM
  total=int(qty)*price
  print("The Total price for total number of gum is :",total)
  
if item=="cks":
  price=prices.COOKIES
  total=int(qty)*price
  print("The Total price for total number of cookies is :",total)
  
if item=="drk":
  price=prices.DRINK
  total=int(qty)*price
  print("The Total price for total number of drink is :",total)