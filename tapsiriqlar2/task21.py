for floor in range(1, 4): 
    for room in range(1, 5): 
        if room == 3: 
            break 
        print(floor * 100 + room, end=" ") 
    print() 
#101 102 
#201 202 
#301 302