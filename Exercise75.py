n = int(input('Nhap so nguyen duong thu nhat: ')) 
m = int(input('Nhap so nguyen duong thu hai: '))

if n % m == 0:
    print('UCLN cua 2 so tren la:', m)
else:
    d = m - 1
    while n % d != 0 or m % d != 0:
        d = d - 1
    
    print('UCLN cua 2 so tren la:', d)