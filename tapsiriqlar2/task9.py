k=500
p=1
while p>0:
    amoun=int(input('amount:'))
    if amount==0:
        print('Goodbye')
        break
    elif amount<0:
        print('invalid amount')
    elif amount>k:
        print('Insufficient funds')
    else:
        print('Balance:', k-amount)
                

