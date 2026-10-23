spaces=20
k=20
while 1:
    command=input('command:')
    if command=='in':
        if k==0:
            print('Garage full')
        else:
            k=k-1
            print('Free spaces:',k)
    elif command=='out':
        if k==20:
            print('Garage is empty')
        else:
            k=k+1
            print('Free spaces:',k)
    elif command=='stop':
        break
    else:
        print('Unknown command ')
