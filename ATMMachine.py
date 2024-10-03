from enum import Enum


class User:
    def __init__(self, card_id, user_name, card_number, balance = 0, password = None, active = True):
        self.card_id = card_id
        self.user_name = user_name
        self.card_number = card_number
        self.balance = balance
        self.password = password
        self.active = active

        
class Language(Enum):
    AZE = 1
    ENG = 2
    RUS = 3


class BankAccount:
    def __init__(self):
        self.user_accounts = {}
        
    def add_user(self, user):
        self.user_accounts[user.card_id] = user
        
    def create_password(self, card_id, password):
        self.user_accounts[card_id].password = password
        print("Password created successfully.\n")
        

class ATMMachine:
    def __init__(self, bank_accounts, current_card = None, language_selected = None):
        self.bank_accounts = bank_accounts
        self.current_card = current_card
        self.language_selected = language_selected
    
    def print_language_options(self, user_name):
        print(f"Welcome {user_name}. Please choose one of the languages to continue:")
        print('\t1. Azerbaijani')
        print('\t2. English')
        print('\t3. Russian\n')
        print()
        
    def print_main_screen_options(self):
        print("You can choose one of the following actions to perform:")
        print('\t1. Check balance')
        print('\t2. Add money')
        print('\t3. Withdraw money')
        print('\t4. Exit\n')
        
    def validate_card(self, card_id):
        if card_id not in self.bank_accounts.user_accounts:
            print("Invalid card. Please contact with your bank!\n")
            return False

        if self.bank_accounts.user_accounts[card_id].active == False:
            print("Your account is blocked. Please contact with your bank!\n")
            return False
        
        return True
    
    def check_balance(self, card_id):
        return self.bank_accounts.user_accounts[card_id].balance
    
    def add_money(self, card_id, amount):
        self.bank_accounts.user_accounts[card_id].balance += amount
        
    def withdraw_money(self, card_id, amount):
        if self.check_balance(card_id) >= amount:
            self.bank_accounts.user_accounts[card_id].balance -= amount
            return True
        else:
            return False
    
if __name__ == '__main__':
    bank_accounts = BankAccount()
    bank_accounts.add_user(User(1, "Ali Mehdi", 1111222233334444, 1000, 5345))
    bank_accounts.add_user(User(2, "Vali Samad", 2222111133334444, 100, 6433))
    bank_accounts.add_user(User(3, "Vagif Ahmad", 4444222211113333))
    
    atm_machine = ATMMachine(bank_accounts)
    
    while True:  
        print("\t\t\t\t\tWelcome to out ATM. Please enter your card!\n")
        
        atm_machine.current_card = int(input("Entered Card ID: "))
        
        if atm_machine.current_card == 0:
            break
        
        if not atm_machine.validate_card(atm_machine.current_card):
            continue
                    
        while atm_machine.language_selected == None:
            atm_machine.print_language_options(bank_accounts.user_accounts[atm_machine.current_card].user_name)

            language_input = int(input("Language Option: "))
            print()
        
            for language in list(Language):
                if language.value == language_input:
                    atm_machine.language_selected = language.name
                    print(f"You have selected {atm_machine.language_selected}.\n")
                    break
        
        while bank_accounts.user_accounts[atm_machine.current_card].password == None:
            try:
                password_input = int(input("Set your 4-digit new password: "))
                print()
                
                if 1000 <= password_input <= 9999:
                    bank_accounts.create_password(atm_machine.current_card, password_input)
                else:
                    print("Invalid input. Please set your 4-digit new password again.\n")
                    continue
            except:
                print("Invalid input. Please enter only digits for setting new password.\n")
                continue
        
        trial = 3
        
        while trial > 0:
            print(f"Please enter your password to continue. You have {trial} trial(s) left.\n")
            try:
                password_input = int(input("Password: "))
                print()
                
                if 1000 <= password_input <= 9999:
                    if bank_accounts.user_accounts[atm_machine.current_card].password == password_input:
                        print("Successful.\n")
                        break
                    else:
                        print("Password is wrong. Try again.\n")
                        trial -= 1
                else:
                    trial -= 1
                    print("Invalid input. Please enter 4 digits for your password.\n")
                    continue
            except:
                trial -= 1
                print("Invalid input. Please enter only digits for your password.\n")
                continue
                
        if trial == 0:
            bank_accounts.user_accounts[atm_machine.current_card].active = False
            print("Your account has been blocked. Please contact with your bank!\n")
            continue
                    
        exit = False
        
        while not exit:
            atm_machine.print_main_screen_options()
            
            try:
                option = int(input("Option: "))
                print()
                
                if option == 1:
                    print(f"Your balance: {atm_machine.check_balance(atm_machine.current_card)} AZN\n")
                elif option == 2:
                    amount = int(input("Amount: "))
                    atm_machine.add_money(atm_machine.current_card, amount)
                    print(f"Successful. {amount} AZN has been added to your account.\n")
                elif option == 3:
                    amount = int(input("Amount: "))
                    print()
                    
                    if atm_machine.withdraw_money(atm_machine.current_card, amount):
                        print(f"Successful. {amount} AZN has been withdrawn from your account.\n")
                    else:
                        print(f"You don't have enough money in your balance.\n")
                elif option == 4:
                    exit = True
                else:
                    print("Wrong selection.\n")
            except:
                print("Wrong selection.\n")
