#Defining
#1
def Return_none(var1,var2):
    print(var1 + var2)

#2
def Unlimited_HiBye(var3):
    Hi="Hi"
    Bye="Bye"
    Result=""
    for n in range (0,var3):
        Result += Hi
        Result += Bye
    return Result

#Running
#1
num1 = int(input("Input an integer"))
num2 = int(input("Input another integer"))
print (Return_none(num1 , num2))

#2
num3 = int(input("Input number of HiBye s"))
print (Unlimited_HiBye(num3))
