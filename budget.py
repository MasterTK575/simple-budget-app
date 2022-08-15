# first create Category class
# _init_ to create some instance variables
# self.name uses object reference, so that each object has it's own copy of the instance variable
# self is the instance of the class, i.e. the object
class Category:
    def __init__(self, name = ""):
        self.name = name
        ledger = list()
        self.ledger = ledger
    
    def deposit(amount, description = ""):
        print(amount, description)
        #transaction = {"amount": amount, "description": description}
        #self.ledger.appen(transaction)




food = Category("Food")
food.deposit(50,"Mercadona")

