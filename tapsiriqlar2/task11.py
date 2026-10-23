sum=0  #(sum)
highest=0  #(highest)
passed=0  #passed
failed=0  #failed
number=0  #number
while 1:
    grade=int(input('Grade:'))
    if grade==-1:
        break
    if grade<0 or grade>100:
        print('wrong grade')
    elif grade>=51:
        sum+=+grade
        passed=c+1
        number+=1
        if grade>highest:
            highest=grade
    else:
        sum+=grade
        number+=1
        failed+=1
print('Passed:',passed)
print('Failed:',failed)
print('Highest:',highest)
print('Average:', sum/number)




