from msilib import change_sequence


class BankAccount:
    """
    Represents a bank account
    """
    total_accounts = 0
    def __init__(self, name: str, balance: float = 0) -> None:
        self.balance = balance
        self.name = name
        self.number = BankAccount.total_accounts
        BankAccount.total_accounts += 1
    
    def deposit(self, amount: float) -> None:
        self.balance += amount
    
    def withdraw(self, amount: float) -> float:
        withdraw_amount = amount
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"Can't withdraw {amount}, emptying account instead.")
            withdraw_amount = self.balance
            self.balance = 0
        return withdraw_amount
    
    def __str__(self) -> str:
        return f"Account #{self.number} ({self.name}) balance is ${self.balance:.2f}"

def main() -> None:
    chequing = BankAccount("Chequing")
    savings = BankAccount("Savings", 100)
    print(chequing)
    print(savings)

    my_money = savings.withdraw(1000)
    print(f"I just withdrew {my_money}")
    print(savings)

    # Class variables
    print(f"There are {savings.total_accounts} accounts")
    
    # This doesn't do what I thought it would
    # chequing.total_accounts = 2
    # print(f"There are {savings.total_accounts} accounts")

main()