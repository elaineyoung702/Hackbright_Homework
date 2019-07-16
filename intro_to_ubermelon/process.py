# log_file = open("um-server-01.txt") #importing the file from src to review


# def sales_reports(log_file): # beginning of function with log_file as argument
#     for line in log_file: #for ever line within the text file
#         line = line.rstrip() #removes spaces from line
#         day = line[0:3] #slices the line so only first 3 letters are left
#         if day == "Tue": # if the first 3 letter (the only letters) equal "Tue"
#             print(line) #then print line


# sales_reports(log_file) #calling the function 

#Solution
log_file = open("um-server-01.txt")


def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


sales_reports(log_file)