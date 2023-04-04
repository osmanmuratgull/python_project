# ATM Automation V2!
# @osmanmuratgull

# User Login
userName = str(input("Please Enter Your Username....:"))
password = input("Please Enter Your Password.....:")
print("1- Shows Balance!\n", "2-Loads Money!\n", "3- Withdraws Money from Account!\n", "4-Quit")
balance = 0

while True:

# User Authentication
    if userName!= "Osman" and password!="123123":
        print("Username or Password Incorrect....")
        break
# Value Parts
    value=int(input("Please Enter a Value....: "))
    if value==2:
        process=int(input("Please Enter An Amount....:"))
        balance+=process
        print("Amount Remaining in Your Account...: ",balance)
        
    elif value==1:
        print(balance)

    elif value==3:
        process=int(input("Please Enter An Amount....:"))
        balance-=process
        print("Amount Remaining in Your Account...:",balance)
    elif value==4:
        print("Leaving the ATM.....:")
        break

    
