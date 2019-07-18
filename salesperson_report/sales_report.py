"""Generate sales report showing total melons each salesperson sold.

- Read through sales_report.py and understand the code
- Write comments explaining what each line of code is doing
- Write comments explaining any improvements you can think of
- If you have time, feel free to implement your suggested improvements

"""


salespeople = []
melons_sold = []

f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|')
    salesperson = entries[0]
    melons = int(entries[2])

    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold} melons')
