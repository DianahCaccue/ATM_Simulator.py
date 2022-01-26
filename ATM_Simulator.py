
accountHolders = {
  "username1" : {
    "name" : "Grace",
    "pin" : 1000,
    "bal" : {'KSh' : 140, 'USD': 0000}
  },
  "username2" : {
    "name" : "Albert",
    "pin" : 2000,
    "bal" : {'KSh' : 140, 'USD': 0000}
  },
  "username3" : {
    "name" : "Diana",
    "pin" : 3000,
    "bal" : {'KSh' : 140, 'USD': 0000}
  },
  "username4" : {
    "name" : "Ronny",
    "pin" : 4000,
    "bal" : {'KSh' : 140, 'USD': 0000}
  },
  "username5" : {
    "name" : "Kelvin",
    "pin" : 5000,
    "bal" : {'KSh' : 140, 'USD': 0000}
  },
  "username6" : {
    "name" : "Martin",
    "pin" : 6000,
    "bal" : {'KSh' : 140, 'USD': 0000}
  },
  "username7" : {
    "name" : "Sally",
    "pin" : 7000,
    "bal" : {'KSh' : 140, 'USD': 0000}
  },
  "username8" : {
    "name" : "Spot",
    "pin" : 8000,
    "bal" : {'KSh' : 140, 'USD': 0000}
  },
  "username9" : {
    "name" : "Joe",
    "pin" : 9000,
    "bal" : {'KSh' : 140, 'USD': 0000}
  },
  "username10" : {
    "name" : "McIntyre",
    "pin" : 1100,
    "bal" : {'KSh' : 140, 'USD': 0000}
  },
  "username11" : {
    "name" : "Becks",
    "pin" : 1200,
    "bal" : {'KSh' : 140, 'USD': 0000}
  },
  "username12" : {
    "name" : "Bayley",
    "pin" : 1300,
    "bal" : {'KSh' : 140, 'USD': 0000}
  }
}

loggedInUser = {}
#print(accountHolders)
def userLogin():
    global loggedInUser
    name = input("enter your username ")
    passcode = int(input("enter your pin "))
    for username in accountHolders:
        user = accountHolders[username]
        if user["name"] == name and user["pin"] == passcode:
            print("successful login")
            loggedInUser = user
            userInterface()
            return
    print("invalid login credentials")

def userInterface():
    while True:

        print("1. withdraw\n2. check balance\n3.print receipt\n4.deposit")
        reply = input("choose an option (1,2,3 or 4) ")
        if reply == "1" or reply== "4":
            action = "withdraw" if reply== "1" else "deposit" 
            currency = input(f"choose a currency to {action} (KSh or USD) ") 
            if currency == "KSh" or currency == "USD":
                withdrawOrDeposit(currency, action)
            else:
                print("invalid input")

            answer = input(f"do you want to make another transaction (yes or no) ")
            if answer == "yes":
                pass #loop continues running
            elif answer == "no":
               break
            else:
                print ("invalid input")
                break

        elif reply == "2":
            checkBalance()
            break
        elif reply == "3":
            printReceipt()
            break
        
        else:
            print("invalid option")

def withdrawOrDeposit(bankCurrency,action):
    rewithdraw = True
    while rewithdraw:

        try:
            amount =int(input(f"how much do you want to {action} "))
        except ValueError:
            print("the value you entered is not an integer")
            return
 
        if action == "withdraw":

            bankBalance = loggedInUser["bal"][bankCurrency]
            if amount < bankBalance:
                loggedInUser["bal"][bankCurrency] -= amount
                print(f"you have withdrawn {bankCurrency} {amount}")
                checkBalance()
                finalReceipt =input("do you want a receipt for your transaction? (yes or no) ")
                if finalReceipt == "yes":
                    printReceipt(bankCurrency, amount, action)
                
            elif amount > bankBalance:
                print ("insufficient funds")
        elif action == "deposit":
            loggedInUser["bal"][bankCurrency] += amount
            print(f"you have deposited {bankCurrency} {amount}")
            checkBalance()
            finalReceipt =input("do you want a receipt for your transaction? (yes or no) ")
            if finalReceipt == "yes":
                printReceipt(bankCurrency, amount, action)
         
        answer = input(f"do you want to {action} again (yes or no) ")
        if answer == "yes":
            pass 
        #rewithdraw remains true
        elif answer == "no":
            rewithdraw = False
        else:
            print ("invalid input")


def checkBalance():
    print(f"balance: KSh {loggedInUser['bal']['KSh']} USD {loggedInUser['bal']['USD']}")

def printReceipt(currency=None, amount=None, action=None):
    print("receipt")
    print(f"loggedInUser: {loggedInUser['name']}")
    if currency is None and amount is None: 
        #when we have not withdrawn
        checkBalance()
    else:

        print(f"{action}: {currency} {amount}")
        print(f"balance: {currency} {loggedInUser['bal'][currency]}")

userLogin()