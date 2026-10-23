month=50
goal=1000
money=0
k=1
while money<goal:
    money=money+month
    month=month+10
    print('Month {}:'.format(k), money)
    k=k+1
k=k-1
print('Goal reached in month {}'.format(k))