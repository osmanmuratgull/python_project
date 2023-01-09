print("******Welcome ATM App******")

print("1-Balance",
"2- Deposit",
"3- Withdraw Money",
"4- q (Exit)")


balance=0
while True:
    process=input("please enter a transaction")
    if(process=="1"):
        print(balance)
    elif(process=="2"):
        process=int(input("enter the amount to deposit"))
        balance+=process
        print("deposit is complete",balance)
    elif(process=="3"):
        process=int(input("enter amount to withdraw"))
        balance-=process
        print("Pulling completed",balance)
    elif(process=="0"):
        print("Exit ATM")
        break