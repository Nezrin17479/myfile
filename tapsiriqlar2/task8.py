username=admin
password=1234
t=0
for i in range(3):
    k=input('write your username')
    c=input('write your password')
    if k==username and c==password:
        print('Welcome!')
        break
    else:
        print('Wrong username or password ')
        t+=1
if t==3:
    print('Account locked"')