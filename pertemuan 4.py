import os, time
balance = 0

def deposit():
    global balance
    print("Amount to deposit?")
    i =int(input())
    balance += i
    print("please wait..")
    time.sleep(2)
    print("thenkyu")
    input("press enter to continue")
    
def withdraw():
    global balance
    print("Amount to withdraw?")
    i =int(input())
    balance -= i
    print('hollon..')
    time.sleep(2)
    print("Thank you")
    input("press enter to continue")
    
def current_balance():
    print("")
    
    
    
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