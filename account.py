import json
import random
import datetime

class Account:
    def __init__(self, id=None):
        print(id)
        if not id or str(id) == "-1" or not id.isdigit(): # If id is invalid or user wants to create account
            self.id = self.generate_unique_id()
        else:
            self.id = id

        data = self.load()

        if data == -1:
            self.balance = 0
            self.transactions = {}
            data = {
                "id": self.id,
                "balance": self.balance,
                "transactions": self.transactions
            }
            self.save(data)
        else:
            self.balance = data["balance"]
            self.transactions = data["transactions"]

    def generate_unique_id(self):
        try:
            with open('accounts.json', 'r') as file:
                accounts = json.load(file)
        except FileNotFoundError:
            accounts = {}

        while True:
            new_id = random.randint(0, 1000000000)
            if str(new_id) not in accounts:
                return new_id

    def load(self):
        try:
            with open('accounts.json', 'r') as file:
                data = json.load(file)

            if data.get(str(self.id)):
                return data[str(self.id)]
            else:
                return -1
        except FileNotFoundError:
            with open('accounts.json', 'w') as file:
                json.dump({}, file)
            return -1

    def save(self, data: any):
        try:
            with open('accounts.json', 'r') as file:
                accounts = json.load(file)
        except FileNotFoundError:
            accounts = {}

        accounts[str(self.id)] = data

        with open('accounts.json', 'w') as file:
            json.dump(accounts, file, indent=4)

    def view_account(self):
        data = self.load()
        print(f"\nID: {data['id']}")
        print(f"Account Balance: ${data['balance']:.2f}")
        if data["transactions"] == {} or data["transactions"] == None:
            print("No transaction history!")
        else:
            print("Transactions:")

            for date, transaction in data["transactions"].items():
                print(f"    Date: {date} | Transaction: {transaction}")

    def withdraw(self, value=None):
        data = self.load()
        if value is None:
            print("How much money would you like to withdraw: ")
            try:
                value = float(input())
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
                return -1
        if value <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
            return -1
        if value > data["balance"]:
            print(f"Error: Withdrawal amount exceeds available balance of ${data['balance']:.2f}.")
            return -1
        self.balance = data["balance"] - value
        print(f"Your new balance is ${self.balance:.2f}.\n")
        self.transactions[datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")] = f"Withdrew ${value:.2f} from account."
        data = {
            "id": self.id,
            "balance": self.balance,
            "transactions": self.transactions
        }
        self.save(data)
        return 0

    def deposit(self, value=None):
        data = self.load()
        if value is None:
            print("Please enter the amount you wish to deposit: ")
            try:
                value = float(input())
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")
                return -1
        if value <= 0:
            print("Error: Deposit amount must be greater than zero.")
            return -1
        if value >= 1000000:
            print("Error: Deposit was denied due to a suspicious amount of money being deposited at once (did you steal this money? Rob a bank?)")
            return -1
        self.balance = data["balance"] + value
        print(f"Your new balance is ${self.balance:.2f}.")
        self.transactions[datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")] = f"Deposited ${value:.2f} to account."
        data = {
            "id": self.id,
            "balance": self.balance,
            "transactions": self.transactions
        }
        self.save(data)
        return 0
