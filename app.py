print("Create your account")
signupUsername = input("Input username: ")
signupPassword = input("Input password: ")
print("user "+ "'" + signupUsername +"'" " created successfully" )
print("Login now")
loginUsername = input("Input username: ")
loginPassword = input("Input password: ")

if signupUsername == loginUsername and signupPassword == loginPassword :
    print("User logged in successfully")
else:
    print("Invalid credentials")    