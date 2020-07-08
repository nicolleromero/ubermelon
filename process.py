log_file = open("um-server-01.txt") # accessing data from the server stored in this file


def sales_reports(log_file): # function to generate a sales report from a log file
    for line in log_file: # iterate over the entries in the log
        line = line.rstrip() # remove trailing spaces from each line on the right
        day = line[0:3] # declare the variable day and set it equal to the first three characters in the line
        if day == "Mon": # if the day in the line matches this day, select it
            print(line) # now print that line


sales_reports(log_file) # call the function to generate the sales report
