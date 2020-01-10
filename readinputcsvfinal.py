import csv
import time

#Prints the reports from input.csv
def csvnumber():
    with open('C:\\Users\\vadiraj.b\\Desktop\\inputfinal.csv','r') as csvfile:
        row_count = sum(1 for row in csvfile)
        print('Number of Reports uploaded in input.csv: ')
        print(row_count if row_count else 'Empty')
        #row_count = len(data)
        #print('Number of Reports uploaded in input.csv: ' + str(row_count))
        #return (str(row_count))
def reportname():
    #Prints the Report Name (First Column) from input.csv file
    fileHandle = open('C:\\Users\\vadiraj.b\\Desktop\\inputfinal.csv', 'r')
    print('Report Names :')
    print
    for line in fileHandle:
        fields = line.split('|')
        print(fields[0]) # prints the first column value
        #print(fields[1]) # prints the second column value
    fileHandle.close()

csvnumber()
time.sleep(1)
print
reportname()
