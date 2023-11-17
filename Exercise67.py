total = 0 

while True :
    guest = input('the ages the guest: ')
    if guest == '':
        break
    else:
        guest = int(guest)
        if guest <= 2:
            cost = 0
        elif 3 <= guest <= 12:
            cost = 14.00
        elif guest >= 65:
            cost = 18.00
        else:
            cost = 23.00
        total += cost
print(f"Admission cost for the group: ${total:.2f}")