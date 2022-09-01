class Category:

    def __init__(self, name, ledger = [], balance = 0):
        self.name = name
        ledger = []
        self.ledger = ledger
        self.balance = balance

# Method for printing out each category details of deposit and withdraw
    def __str__(self):
        total_len = 30
        str4 = self.name.center(30,"*") #adjust first line
        final_str = str4
        count = 0

        for i in self.ledger:
            desc = i["description"]
            amnt = i["amount"]

            if len(desc) < 24 :
                # print(desc)
                str1 = desc
                str2 = "{:0.2f}".format((amnt)).rjust(total_len-len(str1))
                str3 = str1 + str2
            else:
                str1 = desc[:23]
                str2 = "{:0.2f}".format((amnt)).rjust(total_len-len(str1))
                str3 = str1 + str2

            final_str = final_str + '\n' + str3
            count = count + 1

        final_str = final_str + '\n' + "Total: " + str(self.balance)
        return final_str

# Deposit method as per problem statement
    def deposit(self, amount, description = None):
        if description is None :
            temp1 = {"amount" : amount, "description" : ""}
        else:
            temp1 = {"amount" : amount, "description" : description}

        self.balance = self.balance + amount # update balance
        self.ledger.append(temp1) # add the deposit amount to ledger

# Withdraw method according to problem statement
    def withdraw(self, withdraw_amount, description = None):
        if description is None :
            temp2 = {"amount" : -withdraw_amount, "description" : ""}
        else:
            temp2 = {"amount" : -withdraw_amount, "description" : description}

        if len(self.ledger) < 1:
            return False
        elif self.check_funds(withdraw_amount) == False :
            return False
        else:
            self.balance = self.balance - withdraw_amount #update balance based on withdrawl amount
            self.ledger.append(temp2) # add withdrawn amount to ledger
            return True

# Transfer method accroding to problem statement
    def transfer(self, transfer_amount, category):
        temp3 = "Transfer to " + category.name
        temp4 = "Transfer from " + self.name

        if self.check_funds(transfer_amount) == True : # Check if sufficient funds are available for transfer
            self.withdraw(transfer_amount,temp3) # withdrawl from Destination Budget category
            category.deposit(transfer_amount, temp4) # Deposit to Source Budget Category
            return True
        else:
            return False

# check funds method as per problem statement
    def check_funds(self, funds) :
        if (funds > self.balance):
            return False
        else:
            return True

# Method to get balance amount
    def get_balance(self):
        return self.balance




# Function to display percentage withdrawl by each category according to the format
# specified in problem
def create_spend_chart(categories):
    num_categories = len(categories)
    total_withdrawl = 0
    each_withdrawl = {}
    percentage = []
    test_per = []
    count = 0

    # To calculate the withdrawl amount my each category and overall withdrawal
    # amount to calculate percentage
    for i in categories:
        temp_ledger = i.ledger
        temp_name = i.name
        for j in temp_ledger:
            if j["amount"] < 0 :
                # -ve sign for amount as withdrawl amount is saved a negative value
                total_withdrawl = (total_withdrawl - j["amount"])
                each_withdrawl[temp_name] = each_withdrawl.get(temp_name,0) -j["amount"]

    # To calculate and create a list of percetage withdrawl by each category
    # and floor the value to nearest 10
    for k,v in each_withdrawl.items():
        temp_percentage = (v / total_withdrawl) * 100
        temp_percentage = (temp_percentage//10) * 10 # "//" for floor division
        percentage.append(temp_percentage)

    # First string of the output
    line1 = "Percentage spent by category\n"

    # Second string of the output
    # To create a percentage withdrawl by each category chart
    line2 = ""
    for i in range(100, -1, -10) :
        line2 += str(i).rjust(3) + "|"
        for percent in percentage:
            if percent >= i :
                line2 += " o "
            else :
                line2 += "   "
        line2 += " \n"

    # Third string separating the chart from vertical category names
    line3 = "    " + "-"*((len(categories)*3) + 1) + "\n"

    # Fourth string to create the vertically arranged category names
    line4 = "     "
    category_list = list(each_withdrawl.keys())
    loop1 = (len(max(category_list, key=len)))

    for i in range(loop1):
        for j in range(len(category_list)) :
            try :
                line4 += category_list[j][i] + "  "
            except :
                line4 += "   "
        if i < loop1 - 1 :
            line4 += '\n'
            line4 += "     "

    return line1 + line2 + line3 + line4 #returning final concatenated string output
