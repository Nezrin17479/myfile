water=1.50
cost=0
a=[0.05, 0.10, 0.20, 0.50, 1]
while 1:
    coin=float(input('enter your coin(0.05, 0.10, 0.20, 0.50, 1):'))
    if coin in a:
        cost=cost+coin
        if cost>=water:
            print('Here is your water ')
            print('change:',round(cost-water,2))
            break
    else:    
        print('Coin not accepted ')

