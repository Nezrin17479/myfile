while 1:
    card=input('Enter card number:')
    sum=0
    if len(card)!=16 or not card.isdigit():
        print('Must be 16 digits')
    else:
        decard=list(card)
        decrd=decard[::-1]
        for i in range(1,len(decard),2):
            t=int(decard[i])*2
            if t>9:
                t=t-9
            decard[i]=str(t)
        for i in decard:
            sum+=int(i)
        if sum%10==0:
            print(card,'-> Valid')
            break
        else:
            print(card,'-> Invalid')
            

