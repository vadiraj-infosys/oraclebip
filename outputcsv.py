import os
import csv
import time
from time import sleep
#import filemanipulate
import filewin

#from readinputcsvfinal import csvnumber 


timestr = time.strftime("%Y%m%d-%H%M%S")
#print(timestr)
#inputnumber = csvnumber()
#print(inputnumber)

def countoutputcsv():
    input_file = open('/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY/output.csv','r+')
    reader_file = csv.reader(input_file)
    value = len(list(reader_file))
    return value

def countinputcsv():
    with open('/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY/inputfinal.csv','r') as f:
        #reader = csv.reader(f,delimiter = "|")
        reader = f.readlines()
        #data = list(reader)
        row_count = len(reader)
    #print("Number of Reports uploaded in input.csv: " + str(row_count))
        #print(data)
        #print(row_count)
        return row_count

    
def checkstatus(): #Definition to check status of Deployment by checking error.log file
    b = os.path.getsize("C:\\Users\\vadiraj.b\\Desktop\\Prod\\error_output_"+timestr+".csv")
    #print(b)
    if b > 0:
        print ( "Check for C:\\Users\\vadiraj.b\\Desktop\\Prod\\error_output_"+timestr+".csv")

   
         
def outputcsv():      
    #Definition to parse the output.csv & generate two files success & error with time stamp based on status       
    fileHandle = open('/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY/output.csv', 'r')
    successFile = open('/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY/success_output'+timestr+'.csv','w+')
    errorFile = open('/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY/error_output_'+timestr+'.csv','w+')
    
    while True:
        var = "success"
        combined=""
        line1 = fileHandle.readline()
        line1 = line1[:-1]
        line2 = fileHandle.readline()
        if (not line1) or (not line2): break
        reportList = line1.split('|')
        messageList = line2.split('|')
        
        combined = reportList[0] + " >> " + messageList[1]
        combined1 = reportList[0] + " | " + reportList[1] + " | " + reportList[2] + " | " + reportList[3]
        print(combined)
        var1 = messageList[1].find("Success")
        #print(var1)
        if var1 > 1:
            successFile.writelines("%s\n" % combined)
        else:
            errorFile.writelines("%s\n" % combined1)
    
    
    fileHandle = open('/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY/output.csv', "r")
    last_line = fileHandle.readlines()[-1]
    reportList = last_line.split('|')
    combined = reportList[0] +  ">>" +reportList[6]
    print(combined)
    combined1 = reportList[0] + " | " + reportList[1] + " | " + reportList[2] + " | " + reportList[3]
    print(combined1)
    print(reportList)
    var1 = reportList[1].find("Success")
    #print(var1)
    flag = 0
    for i in reportList:
        if i == "Success":
            flag = 1
            break
    #print(flag)
    if flag == 1:
        successFile.writelines("%s\n" % combined)
    else:
        errorFile.writelines("%s\n" % combined1)

    
    successFile.close()
    errorFile.close()
    fileHandle.close()



#timeout = time.time() + 0 * int(inputnumber)
timeout = time.time() + 60 * 0.25
while time.time() < timeout:
    if (countoutputcsv() == (2 * countinputcsv() - 1) ):
        outputcsv()
        filewin.file()
        filewin.backup()
        break
    
    if time.time() > timeout: 
        if countoutputcsv() == (2 * countinputcsv() - 1 ):
            outputcsv()
            filewin.file()
            filewin.backup()
            break        
        else:    
            print( "Timeout Exceeded.. Check Logs!!")
            outputcsv()
            filewin.file()
            break

    
checkstatus()    
