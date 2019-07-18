"""Generate sales report showing total melons each salesperson sold.

- Read through sales_report.py and understand the code
- Write comments explaining what each line of code is doing
- Write comments explaining any improvements you can think of
- If you have time, feel free to implement your suggested improvements

"""


salespeople = [] # establishing an empty list to store salespeople names
melons_sold = [] #establishing an empty list to store amount of melons sold

f = open('sales-report.txt') #opening .txt file w/ salesppl names & amtsold
for line in f: #looping through each line of txt file
    line = line.rstrip() #stripping new line characters at end of line
    entries = line.split('|') #splitting items into list notated by | character
    salesperson = entries[0] #0th index is set to salesperson variable
    melons = int(entries[2]) #2nd index is set to melons var and converted to int

    if salesperson in salespeople: #if name saved to salesperson var is in salespeople
                                    #list
        position = salespeople.index(salesperson) #assign position based on index
                                        #of that salesperson within salespeople list
        melons_sold[position] += melons #adds melons variable into melons_sold list
                            #at the same index as salesperson within salespeople list
    else: #for all other cases
        salespeople.append(salesperson) #add salesperson to end of saespeople list
        melons_sold.append(melons) #add melons to end of melons_sold list


for i in range(len(salespeople)): #loop for the length of salespeople list
    print(f'{salespeople[i]} sold {melons_sold} melons') #print each salesperson
                            #and the amount of melons they sold

"""Suggestion is to create a class for Sales.

class Sales:
    <insert docstring>

    def __init__(self, name, money_made, amount_sold)

    self.name = name.capitalize()
    self.money = money_made
    self.amount = amount_sold