log_file = open("um-server-01.txt") # accessing data from the server stored in this file


def sales_reports(log_file): # function to generate a sales report from a log file
    sum = 0
    watermelon_total = 0
    for line in log_file: # iterate over the entries in the log
        line = line.rstrip() # remove trailing spaces from each line on the right
        day = line[0:3] # declare the variable day and set it equal to the first three characters in the line
        total = line[16:18]
        total = int(total.rstrip())
        if day == "Mon": # if the day in the line matches this day, select it
            sum += total
            if "Watermelon" in line:
                watermelon_total += total
            print(line) # now print that line
    print(f"Grand sum: {sum}")
    print(f"Watermelons: {watermelon_total}")
      


sales_reports(log_file) # call the function to generate the sales report
