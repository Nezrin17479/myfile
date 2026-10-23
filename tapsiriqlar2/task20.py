number=0
for i in range(2,100):
    c=0
    for k in range (2,i):
        if i%k==0:
            c=c+1
    if c==0:
        print(i, end=' ')
        number=number+1
print()
print('Total codes:',number)