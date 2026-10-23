k=0
while k==0:
    c=input('New password:')
    if len(c)<8:
        print('Too short, try again ')
    else:
        print('passwort accepted')
        break