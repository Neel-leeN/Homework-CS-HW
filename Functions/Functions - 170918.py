import random


#Defining all functions
# #1
def mix_number (var1,var2):
    ans2 = str(var1%var2)
    ans1 = str(var1//var2)
    return (ans1 + ' ' + ans2 + '/' + str(var2))

#2
def vowel_count1 (string):
    count = 0
    for n in range (0,len(string)):
        if string[n] == "a" or string[n] == "e" or string[n] == "i" or string[n] == "o" or string[n] == "u":
            count +=1
    return count

#3 & 4
def vowel_count2 (string):
    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0
    for n in range (0,len(string)):
        if string[n] == "a":
            a_count +=1
        elif string[n] == "e":
            e_count +=1
        elif string[n] == "i":
            i_count +=1
        elif string[n] == "o":
            o_count +=1
        elif string[n] == "u":
            u_count +=1
    return a_count,e_count,i_count,o_count, u_count

#6
def sphere_measures (dimension):
    volume = dimension**3 * 4/3 * 3.14
    surface_area = 4 * 3.14 * dimension**2
    return volume, surface_area

#7
def Personal_info (name, age, gender = "Social Construct", married = "NA"):
    print (name, age, gender, married)
    return name, age, gender, married

#8
def Hex2RGB(r=int(input(),16),g=int(input(),16),b=int(input(),16)):
   print(str(r)+"-"+str(g)+"-"+str(b))

def RGB2Hex(R,G,B):
   R = hex(R)
   G = hex(G)
   B = hex(B)
   print(R,"-",G,"-",B)


#Calling functions
#1
num1 = int(input("input number"))
num2 = int(input("input number"))
print(mix_number(num1, num2))

#2
str1 = input("input a string value")
print(vowel_count1(str1))

#3
print(vowel_count2(str1))

#4
vowel_count2(str1)

#6
var1 = float(input("input a number here"))
x,y = sphere_measures(var1)
print ("The volume of the sphere is ", x ,"cm3\nThe surface area of the sphere is ", y ,"cm2")

#7
name_in = input("Input your name here:\t")
age_in = int(input("Input your age here:\t"))
Personal_info(name_in, age_in)

R_val = (random.randint(0,255))
G_val = (random.randint(0,255))
B_val = (random.randint(0,255))

Hex2RGB()
RGB2Hex(R_val,G_val,B_val)
