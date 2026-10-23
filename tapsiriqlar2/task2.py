ctickets=0
atickets=0
for i in range(5):
    k=int(input('write an age'))
    if k<=0:
        print('wrong age')
        break
    elif k<18:
        ctickets+=1
    else:
        atickets+=1
print('Child tickets: ',ctickets)
print('Adult tickets: ', atickets)