work=480
time=0
k=1
customers=0
t=[]
while 1:
    need=int(input('Customer {} needs (min): '.format(k)))
    k=k+1
    t.append(need)
    if time+need<=work:
        time+=need
        customers+=1
    else:
        print('Sorry, come back tomorrow ')
        break

print('Customers served:',customers)
print('Minutes left:',work-time)



