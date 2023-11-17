n = int(input('Nhap mot so nguyen (2 hoac lon hon): '))
ts = 2 
print('Thua so nguyen to cua', n, 'la:')

while ts <= n:
    if n % ts == 0:
        print(ts)
        n = n / ts
    else: 
        ts +=1