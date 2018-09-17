#1
print(9%7)
print(8*4-4)
print(bool(4/4))
print(abs(-1)*4+10)
print(pow(2,(4%4)))
print(20-int(14.5))
print(bool(10/5 - int(2.2)))
print(divmod(19,4))
print(str(5-(3-2)**5))
print(float((15-True)%4 ))

#2 - int / float
#3 - bool
#4
var1 = 2
var1 += 1
print (var1)
    # benefit: (less time), allows var1 to be interchanged with other variables
#5
print(4>1 and 2<3)
print(len("Hi")<3)
print(8>10 or 6<12)
print(not(7>10))
print(5>6 and 8>7)
print(not(5>6 and 8>7))
print(10/2 == 5 and 'A'!='B')
print(10/2 != 5 and 'A'=='B')

#6a --> move over the 1
a = 10
b = 100 - 1
print(a,b)

#6b --> variable w/o spacing, extra lie in between
var1 = 100
var1 += 10
print(var1)

#6c --> no changes
a="Hi"
b="Bye"
a+=a+b
a*=2
print(a)

#6d --> removed = sign in print
my_name = "Mr. Bach"
your_name = "Mr. Student"
print(my_name + " or " + your_name + "?")

#6e -->
this_val = False
that_val = True
some_val = 0
this_val +=1
print(this_val)
some_val=this_val and that_val
print(some_val + 0)

#7 --> Quadratic formula?
#y = a*(x**2) + b*x + c
a=1
b=1
c=1
x = ((b*b - 4*a*c)**1/2-b) / 2*a
x2 = (-b - (b**2 - 4*a*c)**1/2)/ 2*a
print (x,x2)

#8
print("A","B","C","X")
for A in range (0,2):
    for B in range (0,2):
        for C in range (0,2):
            AandB = A*B
            AnandC = 1-(A*C)
            X=AandB+AnandC
            if X == 2:
                X=1
            print (A,B,C,X)
