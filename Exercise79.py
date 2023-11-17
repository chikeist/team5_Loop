import random
a = random.randrange(1,101)
print(a)
j = 0

for i in range (1,100):
    b = random.randrange(1,101)
    if b > a:
        a = b
        j = j + 1
        print(b, "<== Update")
    else:
        print(b)
        
print("The maxium value found was", a)
print("The maxium value was updated", j, "time")