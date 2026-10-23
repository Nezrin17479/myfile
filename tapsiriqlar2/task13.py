hot=0
hottest=0
for i in range (1,8):
    day=int(input('Write temperature'))
    if day>30:
        hottest+=1
    else:
        hot+=1
print('Hot days:', hot)
print('Hottest day:', hottest)
