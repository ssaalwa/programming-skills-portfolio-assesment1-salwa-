correct_password = "12345"
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    entered_password = input("Please enter the password: ")
    
    if entered_password == correct_password:
        print("Correct password entered. Welcome!")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Incorrect password. You have {remaining_attempts} attempts remaining.")
        
        if attempts == max_attempts:
            print("Maximum attempts reached. Authorities have been alerted.")