# first create Category class
# _init_ to create some instance variables
# self.name uses object reference, so that each object has it's own copy of the instance variable
# self is the instance of the class, i.e. the object

class Category:
    def __init__(self, name = ""):
        self.name = name.lower().capitalize()
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
            #print("Not enough funds, transaction not recorded")
            return False

    # transfer only when sufficient money
    # include a transfer message as the description for deposit/withdrawal
    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            #print("Not enough funds for a transaction")
            return False
            
    # define the print behavior of the object
    # for each transaction (dict) in the ledger, we extract the amount and description
    # we make a newline each time and add to the final format
    # we get the length of the description to calculate where to put the amount
    def __str__(self):
        line1 = self.name.center(30, "*")
        final = line1 + "\n"
        for transaction in self.ledger:
            spaces = len(transaction["description"][:23])
            # format the numbers with 2 decimal places
            formamount = "{:.2f}".format(float(transaction["amount"]))
            linex = transaction["description"][:23] + str(formamount)[:7].rjust((30-spaces)) + "\n"
            final = final + linex
        lastline = "Total: " + str("{:.2f}".format(float(self.get_balance())))[:7]
        final = final + lastline
        return final


# we take a list of categories as an input, and then iterate through them
def create_spend_chart(inp):
    total = 0
    # first calculate the global total - we only want the withdrawals
    # so we have to go into each dict/transaction of the categories ledger
    for category in inp:
        for dict in category.ledger:
            if dict["amount"] < 0:
                total = total + dict["amount"]
    # then get the percentages
    # we need to account for having multiple withdrawals
    # for each dict/transaction in the ledger we add up the category total (for withdrawals)
    # once done with all transactions we calculate the percentage and commit
    li = list()
    for category in inp:
        #print(category.ledger)
        catamount = 0
        for dict in category.ledger:
            if dict["amount"] > 0:
                continue
            catamount = catamount + dict["amount"]
        percentage = catamount / total
        li.append((category.name, percentage))
    #print(li)

    # make the header
    wholechart = "Percentage spent by category\n"
    # make the bar charts
    perc = 100
    line = ""
    # for each percentage on the y-axis (vertical) we create a line
    # you iterate through the percentage on the y-axis (vertical), substract -10 each time
    # you check if the perc of the category is equal to or greater than the label
    # if so you add the o
    while perc >= 0:
        # first we create the beginning
        line = str(perc).rjust(3) + "|"
        # then for each category we check if we should include an "o" to make the bar chart
        for category in li:
            if (category[1]*100) >= perc:
                partline = " " + "o" + " "
                line = line + partline
            else:
                partline = "   "
                line = line + partline
        # make a new line and concatenate to the whole thing
        line = line + " \n"
        wholechart = wholechart + line
        perc = perc - 10
    
    # add the horizontal line
    length = len(li)*3 + 1
    horline = (" "*4) + ("-"*length) + "\n"
    wholechart = wholechart + horline

    # add the categories vertically
    # first find the longest string to know how far "down" we have to go
    strlen = 0
    for category in li:
        if len(category[0]) > strlen:
            strlen = len(category[0])
    
    # we're creating a number of lines based on the longest category
    count = 0
    while strlen > 0:
        # each line starts with 4 spaces
        line = " " * 4
        # then for each category we try to get the letter and add it to the line
        for category in li:
            try:
                partline = " " + category[0][count] + " "
            except:
                partline = " " * 3
            # we join the line
            line =  line + partline
        # and then add the entire line to the final result
        if strlen > 1:
            wholechart = wholechart + line + " \n"
        else:
            wholechart = wholechart + line + " "
        count = count + 1
        strlen = strlen - 1

    return wholechart
    

business = Category("business")
business.deposit(900, "deposit")
business.withdraw(10.99)

food = Category("fOod")
food.deposit(900, "deposit")
food.withdraw(105.55)

entertainment = Category("entertainment")
entertainment.deposit(900, "deposit")
entertainment.withdraw(33.40)

print(create_spend_chart([business, food, entertainment]))

