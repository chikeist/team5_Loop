import random 

s = 0 
t = 'HT' 
for i in range (1, 11):
    r1 = random.randint(0, 1)
    r2 = random.randint(0, 1)
    r3 = random.randint(0, 1)
    print(t[r1], t[r2], t[r3], end = ' ')
    
    d = 3 
    while True:
        if r1 == r2 == r3:
            break
        d += 1
        r1 = r2 
        r2 = r3
        r3 = random.randint(0, 1)
        print(t[r3], end =' ')
        
    print('(', d, ' flips)', sep = '')
    s += d 
print('On average,', s/10, 'flips were needed')