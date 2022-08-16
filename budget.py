# first create Category class
# _init_ to create some instance variables
# self.name uses object reference, so that each object has it's own copy of the instance variable
# self is the instance of the class, i.e. the object
class Category:
    def __init__(self, name = ""):
        self.name = name
        ledger = list()
        self.ledger = ledger
    
    # you need to add self to the method you want to create inside the class
    # self (so the instance/ object) needs to have it's own parameter, else we have not enough
    # i.e. without self as a parameter, we give 3 arguments but only have 2 parameter
    def deposit(self, amount, description = ""):
        transaction = {"amount": amount, "description": description}
        self.ledger.append(transaction)

    # calc balance of the object by iterating through the list of dict
    # take the value of each "amount" key and add them up
    def get_balance(self):
        balance = 0
        for trans in self.ledger:
            balance = balance + trans["amount"]
        return balance

    # to check if there are enough funds for a withdrawal
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True
    
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount) == True:
            amount = - amount
            transaction = {"amount": amount, "description": description}
            self.ledger.append(transaction)
            return True
        else:
            print("Not enough funds, transaction not recorded")
            return False

    # transfer only when sufficient money
    # include a transfer message as the description for deposit/withdrawal
    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            print("Not enough funds for a transaction")
            return False
            



food = Category("Food")
food.deposit(50, "Paycheck")
food.deposit(55, "Paycheck2")
print(food)
