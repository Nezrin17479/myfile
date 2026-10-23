for floor in range(1, 6):
    c=0
    if floor != 4:  
        for room in range(1, 5): 
            if c==0:
                print('Floor {}:'.format(floor), end=' ')
                c=1
            print(floor * 100 + room, end=" ") 
        print() 