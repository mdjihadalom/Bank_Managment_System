# Reminder: When you create an account, you will receive an account number.
#           Keep this number for your next login.

import random 

class bank:
    accounts = []
    totalBalance = 0
    totalLoan = 0
    loan_features = True
    isbankrupt = False

    def __init__(self, name, email, address, account_number, type):
        self.name = name
        self.email = email
        self.address = address
        self.account_number = account_number
        self.type=type
        self.balance = 0
        self.transaction_history = []
        self.loan_counter = 0
        bank.accounts.append(self)

    def deposit(self, ammount):
        print("\n------------Deposit result------------")
        if bank.isbankrupt == False:
            self.balance += ammount
            bank.totalBalance += ammount
            self.transaction_history.append(f"Deposited {ammount} TK")
            print(f"Successfully Deposited {ammount} TK.New balance: {self.balance} TK")
        else:
            print("the bank is bankrupt !")
        print("----------Deposit result end----------")

    def witdraw(self, ammount):
        print("\n------------Withdraw result------------")
        if bank.isbankrupt == False:
            if ammount <= self.balance:
                self.balance -= ammount
                bank.totalBalance -= ammount
                self.transaction_history.append(f"withdraw {ammount} TK")
                print(f"Successfully withdraw {ammount} TK.New balance: {self.balance} TK")
            else:
                print("Withdrawal amount exceeded !")
        else:
            print("the bank is bankrupt !")  
        print("----------withdraw result end----------")

    def cheak_user_balance(self):
        print("\n------------User balance result------------")
        print(f"available balance: {self.balance} TK of your {self.type} account !")
        print("----------User balance result end----------")

    def check_transaction_history(self):
        print("\n------------Transection history result------------")
        for history in self.transaction_history:
            print(history)
        print("----------Transection history result end----------")

    def take_loan(self, ammount):
        print("\n------------Take Loan result------------")
        if bank.isbankrupt == False:
            if bank.loan_features == True:
                if self.loan_counter < 2:
                    if bank.totalBalance >= ammount:
                        self.balance += ammount 
                        bank.totalLoan += ammount
                        bank.totalBalance -= ammount
                        self.loan_counter += 1
                        self.transaction_history.append(f" taken loan {ammount} TK")
                        print(f"Successfully taken loan {ammount} TK.New balance: {self.balance} TK")
                    else:
                        print("Not possible to provide Your expected ammount ! Enter right number of ammount.")
                else:
                    print("limited number of loan already taken !")
            else:
                print("Loan features is Off in this time ! Try another time.")
        else:
            print("the bank is bankrupt !")
        print("----------take loan result end----------")
    
    @staticmethod
    def transfer_balance(current_user, receiver_account_num, ammount):
        print("\n------------Transfer balance result------------")
        Flag = False
        if bank.isbankrupt == False:
            for account in bank.accounts:
                if account.account_number == receiver_account_num:
                    if ammount <= current_user.balance and ammount >= 0:
                        current_user.balance -= ammount
                        account.balance += ammount
                        Flag = True
                        current_user.transaction_history.append(f"Successfully transfered balance {ammount} TK to account name {account.name} account number: {account.account_number}")
                        account.transaction_history.append(f"Successfully recceived transfered balance {ammount} TK from account name {current_user.name} account number: {current_user.account_number}")
                        print(f"Successfully transfered taka {ammount} TK.New balance: {current_user.balance} TK")
                        break
                    else:
                        print("Enter right number of ammount !")
                        break   
        else:
            print("the bank is bankrupt !")
        if Flag == False:
            print("Account does not exist")
        print("----------Transfer balance result end----------")

    @staticmethod
    def login():
     Flag = False
     print("\n-------------Enter your data for log in your User/Admin account-------------")
     account_number = int(input("Enter your account number: "))   
     print("\n------------Log in result------------")
     for account in bank.accounts:
        if account.account_number == account_number:
            print(f"Welcome back : {account.name}!")
            Flag = True
            return account
     if Flag == False:
        print("Account not found. Log in failed ! Please enter your valid account number.")
     print("----------Log in result end----------\n")
     return None

    @staticmethod
    def remove_user_account(account_num):
        print("\n------------Remove account result------------")
        for account in bank.accounts:
            if account.account_number == account_num:
                bank.totalBalance -= account.balance
                bank.totalLoan -= account.balance
                bank.accounts.remove(account)
                print(f"User name: {account.name} account number: {account.account_number} removed successfully !")
                break
        print("----after remove a user, All user info result---")
        for account in bank.accounts:
            if account.type != "admin":
                print(f"Account Number: {account.account_number} Name: {account.name}, Email: {account.email}, Balance: {account.balance}, Type: {account.type}")
        print("--after remove a user, All user info result end--")
        print("----------Remove account result end----------")
    
    @staticmethod
    def show_all_user_account_list():
        print("\n------------All user info result------------")
        for value in bank.accounts:
            if value.type != "admin":
                print(f"Account Number: {value.account_number} Name: {value.name}, Email: {value.email}, Balance: {value.balance}, Type: {value.type}")
        print("\n----------All user info result end----------")

class savingsAccount(bank):
    def __init__(self, name, email, address, account_number, type):
        super().__init__(name, email, address, account_number, type)
        print("\n----------------------Creating account result----------------------")
        print(f"Welcome {self.name} in your {self.type} account")
        print(f"take your account number {self.account_number} for next time log in your {self.type} account")
        print("--------------------Creating account result end--------------------")

class currentAccount(bank):
    def __init__(self, name, email, address, account_number, type):
        super().__init__(name, email, address, account_number, type)
        print("\n----------------------Creating account result----------------------")
        print(f"Welcome {self.name} in your {self.type} account")
        print(f"take your account number {self.account_number} for next time log in your {self.type} account")
        print("--------------------Creating account result end--------------------")

current_user = None
while True:
    if current_user == None:
        print("\n-------------Welcome ! Bank Managment System-------------")
        print("---No user log in !---")
        option = input("Enter your choice - User/Admin/Log in (ex: ur/an/ln) :")
        if option == "ur":
            print("\n-------------Enter your data for creating User account-------------")
            name = input("Enter your Name: ")
            email = input("Enter your Email: ")
            address = input("Enter your Address: ")
            account_number = random.randint(5555, 10000)
            type = "user"
            account_type = input("Enter your choice Account savings / Current (ex:sv/cu) : ")
            if account_type == "sv":
                current_user = savingsAccount(name, email, address, account_number, type)
            elif account_type == "cu":
                current_user = currentAccount(name, email, address, account_number, type)
        elif option == "an":
            print("\n-------------Enter your data for creating admin account-------------")
            name = input("Enter your Name: ")
            email = input("Enter your Email: ")
            address = input("Enter your Address: ")
            account_number = random.randint(5555, 10000)
            type = "admin"
            account_type = "cu" 
            current_user = currentAccount(name, email, address, account_number, type)
        elif option == "ln":
            current_user = bank.login()  
        else:
            print("\nWrite valid info !")
    else:
        print(f"\n------{current_user.name} use this system as a {current_user.type}------")
        if current_user.type == "admin":
            print("1. delete user account: ")
            print("2. show all user accounts list: ")
            print("3. Show total available balance of the bank: ")
            print("4. check the total loan amount: ")
            print("5. on or off the loan feature of the bank: ")
            print("6. Select bankrupt data: ")
            print("7. Logout: ")

            option = int(input("Enter a option: "))
            if option == 1:
                account_num = int(input("Enter user account number: "))
                current_user.remove_user_account(account_num)
            elif option == 2:
                bank.show_all_user_account_list()
            elif option == 3:
                print("\n----------total available balance of the bank result----------")
                print(f"total available balance of the bank {bank.totalBalance} TK")
                print("--------total available balance of the bank result end--------\n")
            elif option == 4:
                print("\n------------total loan ammount of the bank result------------")
                print(f"the total loan amount: {bank.totalLoan} TK")
                print("------------total loan ammoun of the bank result end------------\n")
            elif option == 5:
                op = input("Enter on or off the loan feature of the bank: (ex: on or off): ")
                if op == "on":
                    bank.loan_features = True
                    print("\nloan feature ON successfully !\n")
                elif op == "off":
                    bank.loan_features == False
                    print("\nloan feature OFF successfully !\n")
            elif option == 6:
                op = int(input("Enter number: (ex: true = 1 or false = 0): "))
                if op == 1:
                    bank.isbankrupt = True
                    print("\n Setting bankrupt info Successfully !\n")
                elif op == 0:
                    bank.isbankrupt = False
                    print("\n Setting bankrupt info Successfully !\n")
            elif option == 7:
                current_user = None 
            else:
                print("\nInvalid Option !")

        elif current_user.type == "user":
            print("1. check available balance: ")
            print("2. check transaction history: ")
            print("3. take a loan from the bank: ")
            print("4. transfer amount: ")
            print("5. deposit balance: ")
            print("6. withdraw: ")
            print("7. Log out: ")  

            option = int(input("Enter a option: "))
            if option == 1:
                current_user.cheak_user_balance()
            elif option == 2:
                current_user.check_transaction_history()
            elif option == 3:
                ammount = int(input("Enter loan ammount: "))
                current_user.take_loan(ammount)
            elif option == 4:
                receiver_account_num = int(input("Enter receiver account number: "))
                ammount = int(input("Enter transfer ammount: "))
                current_user.transfer_balance(current_user, receiver_account_num, ammount)
            elif option == 5:
                ammount = int(input("Enter deposit ammount: "))
                current_user.deposit(ammount)
            elif option == 6:
                ammount = int(input("Enter withdraw ammount: "))
                current_user.witdraw(ammount)
            elif option == 7:
                current_user = None
            else:
                print("Invalid option !")
