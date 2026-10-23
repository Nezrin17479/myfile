password=input('Password:')
digit=0
upper=0
lower=0
for i in password:
    if i.isdigit():
        digit+=1
    elif i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
if len(password)>=8:
    if digit>=1 and upper>=1 and lower>=1:
        print('Strong password ')
    else:
        print('Weak password: no uppercase letters')
else:
    print('Weak password: no uppercase letters')
