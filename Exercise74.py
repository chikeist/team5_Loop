print('    ', end ='')

for i in range (1, 11):
    print(str(i).rjust(4), end = '')
print()

for i in range (1, 11):
    print(str(i).rjust(4), end = '')
    
    for j in range (1, 11):
        print(str(i*j).rjust(4), end = '')
    print()