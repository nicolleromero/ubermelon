"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

# Opens and reads in the lines from the sales report file
f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|')

    salesperson = entries[0]
    melons = int(entries[2])

""" Using a different data structure (dict instead of lists) would
 allow you to loop once and print the report in that loop
 """


if salesperson in salespeople:
    position = salespeople.index(salesperson)

    melons_sold[position] += melons
else:
    salespeople.append(salesperson)
    melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
