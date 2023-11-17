n = str(input('Nhap chuoi nhi phan: '))  
tp = len(n) - 1
s = 0

while tp >= 0:
    s = s + int(n[len(n) - tp - 1]) * pow(2, tp) 
    tp -=1  
print('So thap phan la:', s)