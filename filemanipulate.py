import datetime
import sys
import os
import shutil
import time
import glob

#/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY

source = '/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY/'

now = datetime.datetime.now()
newDirName = now.strftime("%Y%m%d_%H%M%S")

def file():
    print('Step 1 : Checking if Success_Directory exists')
    time.sleep(1)
    CHECK_SUCCESSFOLDER = os.path.isdir("/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY/Success_Directory")
    if CHECK_SUCCESSFOLDER:
        print(' Success_Directory Exists')
    else:
        os.makedirs('/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY/Success_Directory')
        print("Created folder : Success_Directory " )
    print
    print('Step 2 : Checking if Error_Directory exists')
    CHECK_ERRORFOLDER = os.path.isdir("/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY/Error_Directory")
    time.sleep(1)
    if CHECK_ERRORFOLDER:
        print(' Error_Directory Exists')
    else:
        os.makedirs('/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY/Error_Directory')
        print("Created folder : Error_Directory " )
    print
    time.sleep(1)
    print('Step 3 : Moving success files to Success_Directory')
    os.chdir('/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY/')
    dest_dir = '/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY/Success_Directory/'
    for file in glob.glob(r'success_output*'):
        print(file)
        shutil.move(file, dest_dir)
    print('Step 4 : Moving error files to Error_Directory')
    os.chdir('/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY')
    dest_dir = '/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY/Error_Directory/'
    for file in glob.glob(r'error_output*'):
        print(file)
        shutil.move(file, dest_dir)

def backup():        
    print('Step 5: Backup files from BIPREPORT_DEPLOY directory' )
    if len(os.listdir('/appsib_01/ses/siebsrvr/temp/BIPREPORT_DEPLOY')) == 0:
        print("BIPREPORT_DEPLOY is empty, Nothing to Backup")
    else:
        print
        print('Step 6: Creating directory with current timestamp')    
        os.chdir('/appsib_01/ses/siebsrvr/temp')
        os.mkdir(newDirName)
        print('Directory '+newDirName+' created in /appsib_01/ses/siebsrvr/temp')
        time.sleep(1)
        os.chdir("/appsib_01/ses/siebsrvr/temp/" + str(newDirName))
        newdir1 = os.getcwd()
        destination = newdir1   
        files = os.listdir(source)
        for f in files:
            shutil.move(source+f, destination)
        print('Backuping files from BIPREPORT_DEPLOY directory to /appsib_01/ses/siebsrvr/temp/'+str(newDirName))
        time.sleep(1)
        print('Done')
    print


