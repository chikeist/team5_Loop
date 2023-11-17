n = int(input('Nhap mot so nguyen duong: '))
r = "" 

while n > 0:
    q = n % 2
    r = str(q) + r  
    n //= 2
print('Chuoi nhi phan la:', r )