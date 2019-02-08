from random import randint, random
 
time = 24
rate_A = 3
rate_B = 4
return_rate = 7
 
location_A = [i for i in range(1, 8)]
location_B = [i + 8 for i in range(0, 8)]
outside = []
 
 
# Main
print("Location A: ", location_A)
print("Location B: ", location_B)
print('')
 
for i in range(time):
    for j in range(rate_A):
        outside.append(location_A.pop(randint(1, len(location_A) - 1)))
 
    for j in range(rate_B):
        outside.append(location_B.pop(randint(1, len(location_B) - 1)))
 
    for j in range(return_rate):
        rented = int(random())
 
        if rented == 0 and len(location_A) < 10:
            location_A.append((outside.pop()))
 
        elif rented == 1 and len(location_B) < 10:
            location_B += outside.pop()
 
        elif rented == 0 and len(location_A) >= 10:
            location_B.append(outside.pop())
 
        elif rented == 1 and len(location_B) >= 10:
            location_A += outside.pop()
 
    location_A.sort()
    location_B.sort()
 
    print('After ', i + 1, 'hour(s): \nLocation A: ', len(location_A), location_A)
    print('After ', i + 1, 'hour(s): \nLocation B: ', len(location_B), location_B)
 
 
print('-----------------------------------------------------------')
print('End of the day: ')
print('')
print('Location A:', len(location_A), location_A)
print('Location B:', len(location_B), location_B)
print('')
print('-----------------------------------------------------------')
