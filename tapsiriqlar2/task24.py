a=0
b=0
c=0
s=0
while 1:
    vote=input('Vote:')
    if vote == 'end':
        break
    elif vote=='A':
        a+=1
    elif vote=='B':
        b+=1
    elif vote=='C':
        c+=1
    else:
        s+=1
    if a>0 and b>0 and c>0:
        print('Vote: end')
        break
print('A:',a,'B:',b,'C:',c)
print('Spoiled:',s)
max_votes = max(a, b, c)
winners = []
if a == max_votes:
    winners.append('A')
if b == max_votes:
    winners.append('B')
if code_c := c == max_votes: # sadəcə c == max_votes
    if c == max_votes:
        winners.append('C')


if len(winners) > 1:
    print("Winner: Tie") 
else:
    print("Winner:", winners[0])