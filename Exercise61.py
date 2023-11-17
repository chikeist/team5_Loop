total = 0
count = 0

while True:
    a=float(input(''))
    total += a
    count += 1 
    if a == 0:
        count -= 1
        break

if count > 0:
    print('The average of a collection of values entered: ', total/count)
else:
    print('Error!')