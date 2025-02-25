from account import Account

def print_menu(user_id):
    print(f"""
          
    ================================
                USER ID
    {user_id}
    ================================
    |                              |
    |         BANKING MENU         |
    |                              |
    ================================
    | 1. View Account              |
    | 2. Withdraw                  |
    | 3. Deposit                   |
    | 4. Exit                      |
    ================================

    """)

def main():
    account_id = input("Enter your account ID (Enter -1 to create a new account): ")
    account = Account(account_id)
    account_id = account.id
    
    while True:
        print_menu(account_id)
        choice = input("Enter your choice: ")
        
        if choice == '1':
            account.view_account()
        elif choice == '2':
            account.withdraw()
        elif choice == '3':
            account.deposit()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()