total = 0

while True :
    item = input('Cost of item: ')   
    if item == "":
        break
    else:
        item = float(item)
        total += item

amount = total // 5
if total % 5 > 2.5 :
    amount +=1
print ('Total cost:','\t',total)
print ('amount:','\t',amount,)