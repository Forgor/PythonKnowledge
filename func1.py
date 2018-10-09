#!usr/bin/python
#Filename e:func1.py

import os
import time

#1.The files and the directories to ba backed up are specified in a list
source = ['E:\MyGitfile\hello-world','E:\MyGitfile\myPro']

#2.The backup must be stored in a main backup directory
target_dir = 'E:\MyGitfile'#remember to change this to what you will be using

#3.The files are backed up into a zip file
#4.The name of the zip archive is the current date and time
target = target_dir+time.strptime('%Y %m %d %H:%M:%S')+'.zip'

#5.we use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr'%s'%s"% (target,''.join(source))

#Run the backup
if os.system(zip_command)==0:
    print('Successful backup to',target)
else:
    print('Backuo Failed')
