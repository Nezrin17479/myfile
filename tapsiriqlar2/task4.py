total=0
c=0
for i in range (5):
    k=int(input('Price of item:'))
    if k<0:
        print('Wrong price')
        break
    else:
        c+=1
        total=total+k
if c==5:
    print('total:', total)
    average=total/5
    print('average:', average)