#Easy
var1 = "23"
if type(var1) == int:
	print ("Its an integer")
else:
	print ("It isn't an integer")

#Hard
var2 = "sky"
if var2.lower().count("a") >  0 and var2.lower().count("e") >  0 and var2.lower().count("i") >  0 and var2.lower().count("o") >  0 and var2.lower().count("u") >  0:
	print("all five vowels are present")
elif var2.lower().count("a") >  0 or var2.lower().count("e") >  0 or var2.lower().count("i") >  0 or var2.lower().count("o") >  0 or var2.lower().count("u") >  0:
	print("some vowels are present")
else:
	print("no vowels are present")

#ternary
a=2
b=10
print ("Yes") if a < b else print ("No")

#Easy
import math as m
var3 = 72
print("First condition") if m.sqrt(var3)<5 or m.sqrt(var3)>10 else print("Square root is 10") if m.sqrt(var3) == 10 else print("No conditions are met")

#Hard
var4 = "wrajjssfjfwjfeafaj1-2-e23wrd"
if len(var4)<30 and var4.isalpha():
	print ("valid name")
else:
	print("you are invalid")