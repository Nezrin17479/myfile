password = "secret" 
while True:     
    attempts = 0     
    entered = input("Password: ")     
    if entered == password:         
        print("Welcome")         
        break     
    attempts += 1     
    if attempts == 3:         
        print("Account locked")         
        break 


#in the given code, 
#since the attempts variable is reset to zero every time the loop repeats, 
#it will never equal 3; thus, the break statement will 
#not be executed and the loop will continue indefinitely

#RIGHT CODE:
password = "secret" 
attempts = 0 
while True:         
    entered = input("Password: ")     
    if entered == password:         
        print("Welcome")         
        break     
    attempts += 1     
    if attempts == 3:         
        print("Account locked")         
        break 