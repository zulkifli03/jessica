import os, time
balance = 0

def deposit():
    global balance
    i = int(input("Amount to deposit?\n"))

    balance += i
    print("please wait..")
    time.sleep(2)
    print("thenkyu")
    input("press enter to continue")
    
def withdraw():
    global balance
 
    i =int(input("Amount to withdraw?"))
 
    print('hollon..')
    time.sleep(2)
    if i <= balance:
        balance -= i
        print("Thank you")
    else: 
        print("balance is not enough.")
        
    input("press enter to continue")
    
def current_balance():
    print(f"{'Your current balance :':^50}")
    print()
    print(f"{balance :^50}")
    print()
    input(f"{'press enter to continue':^50}")   


while True:
    os.system('cls')
    print('Welcome to C-Bank')
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Current Balance")
    print("4.Exit")
    
    print()
    choose = input('Choice: ')
    if choose == '1':
        deposit()

    elif choose == '2':
        withdraw()

    elif choose == '3':
        current_balance()

    elif choose == '4':
        print("Thank you.")
        break
