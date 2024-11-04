#1. Define Named Constants
MIN_BALANCE = 100 #Minimum balance put as a constant required for account
OVERDRAFT_FEE = 35.0 #Overdraft fee as a constant 



def main():
    #Main loop 
    balance= 0
    is_running = True #Boolean for the loop

    while is_running:
        #Display the main menu and get user option
        option=main_menu()

        if option == '1':
            #show current balance
            show_balance(balance)
        elif option == '2':
            #Add deposited amount to balance
            balance += deposit()
        elif option == '3':
            #Withdraw from balance and update balance
            balance = withdraw(balance)
        elif option == '4':
            #Exit the menu
            exit_menu()
            is_running = False
        else:
            #Invalid option input
            print("Not valid. Please select options 1-4 please")
  
def main_menu():
    #Display the main menu options and return to option selection
    print("----------------------")
    print("MAIN MENU")
    print("----------------------")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    print("----------------------")
    #Prompt user to select an option
    option=input("Please select an from the following:")
    return option


def show_balance(balance):
    #Display the current balance 
    print("-------------------------------")
    print(f"Your balance is ${balance:.2f}")
    print("--------------------------------")

def deposit():
    #Prompt the user to deposit
    print("--------------------------")
    amount=float(input("Enter an amount to deposit:$ "))
    print("--------------------------")
    #Check if deposit is valid
    if amount <= 0:
        print("--------------------------")
        print("Deposit unsucessful, Please enter a valid amount.")
        print("--------------------------")
        return 0 #Return zero if invalid deposit
    else:
        #Sucessful deposit
        print(f"Deposit sucessful! Your new balance is ${amount:.2f}.")
        print("------------------------------------------------------")
        return amount

def withdraw(balance):
    #Prompt the user for withdrawl amount
    print("----------------------")
    amount=float(input("Enter the amount you would like to withdraw:$ "))

    if amount > balance: #Check if withdrawl amount is greater than current balance
        print("Withdraw unsucessful! Insufficient funds. ")
        print("--------------------")
        return balance #Return current balance if withdrawl fails
    else:
        #Update balance
        new_balance = balance - amount
        print(f"Withdrawl sucessful! Your new balance is ${new_balance:.2f}.")

        if new_balance < MIN_BALANCE:#Check if overdraft fee applies
            print(f"Overdraft! A fee of ${OVERDRAFT_FEE:.2f} has been applied.")
            new_balance-=OVERDRAFT_FEE
            print(f"Your new balance after overdraft fee is: ${new_balance:.2f}")

        print("---------------------")
        return new_balance #Return the updated balance

def exit_menu():
    #exit message
    print("-----------------")
    print("Have a great day!")
    print("-----------------")

if __name__=='__main__':
    main()



