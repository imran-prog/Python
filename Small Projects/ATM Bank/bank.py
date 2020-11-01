# Main File of the ATM Program

balance = 1000              # My Total Balance Before Any Process

while True:
    print("     ATM     ")
    print("""   
    1)          Balance
    2)          Withdraw
    3)          Deposit
    4)          Quit
    """)

    try:
        Option = int(input("Enter Option: "))
    except Exception as e:
        print("Error:", e)
        print("Enter only 1, 2, 3 and 4")

    if Option == 1:
        print("Balance $", balance)
    elif Option == 2:
        print("Balance $", balance)
        withdraw = float(input("Enter Withdraw amount $: "))
        if withdraw > 0:
            balance = balance - withdraw
            print("Remaining Balance $", balance)
        elif withdraw > balance:
            print("Insufficient Funds To Transfer")
        else:
            print("No Withdraw Process Occurred")
    elif Option == 3:
        print("Balance $", balance)
        deposit = float(input("Enter Deposit amount $: "))
        if deposit > 0:
            balance = balance + deposit
            print("After deposit Balance $", balance)
        else:
            print("No Withdraw Process Occurred")
    elif Option == 4:
        exit()