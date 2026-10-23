pin = "1234" 
attempts = 0 
while attempts < 3:     
    entered = input("PIN: ")     
    attempts += 1     
    if entered == pin:         
        print("Access granted")         
        break     
    print("Wrong PIN,", 3 - attempts, "attempts left") 
print("Attempts used:", attempts) 
#Wrong PIN, 2 attempts left
#Wrong PIN, 1 attempts left
#Acces granted
#Attempts used:3