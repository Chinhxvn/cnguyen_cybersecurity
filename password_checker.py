#Password Testing File
#This is a script for testing passwords 
#Test

def password_length_checker(input_string):
	return len(input_string) >= 8 

while True:
	password = input("Enter your password that is 8 characters long: ") 
	
	if password_length_checker(password):
		print("Your password is 8 characters long")
		break
	else:
		print("Your password is not long enough, please try again. ") 

print("Your password is:", password)

