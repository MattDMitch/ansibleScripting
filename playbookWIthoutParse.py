#Created by Matthew Mitchell
#8/31/2022
import os
import readline
import pytz
from datetime import date
from datetime import datetime

#Function to get input from user about playbook and checking if filename is legit
#Returns Checked Filename
def start():
        while True:
                #Autocomplete Function
                readline.parse_and_bind("tab: complete")
                readline.set_completer(completer)

                playBook= input("Enter the filename of the playbook you want to run \n")
                try:
                        play = open(playBook,"r").readlines()
                except FileNotFoundError:
                        print("Incorrect Filename")
                else:
                         break
        confirm = input("Are you sure you want to run "+playBook+"?  y/n \n")
        if confirm.upper() == "Y":
                return  runPlayBook(playBook)
        else:
                start()

#Tab Autocomplete function
def completer(text, state):
        #Getting all files in current directory
        # folder path
        dir_path = r'/path/to/dir'

        # list to store files
        res = []

        # Iterate directory
        for path in os.listdir(dir_path):
                # check if current path is a file
                if os.path.isfile(os.path.join(dir_path, path)):
                         res.append(path)

        #Autocomplete part
        options = [x  for x in res if x.startswith(text)]

        return options[state]




#Running playbook
def runPlayBook(playBook):
        print("Running "+playBook)
        newlog(playBook)

#New logging function
def newlog(playBook):
        #Getting Date and time
        today= datetime.now(pytz.timezone("US/Central"))
        d = today.strftime("%m-%d-%Y_")
        t = today.strftime("%H:%M:%S")
        fname =d +"T"+ t+"_"+playBook.replace(".yml", "")
        #Creates  file for logs
        print(playBook)
        os.system("touch /path/to/"+fname".txt")
        #Runs playbook and pipes output to txt file create
        os.system("ansible-playbook --ask-pass --ask-become-pass "+playBook+" | tee /path/to/"+fname+".txt")
        #Clean up
        print("Writing Logs...")
        print("Logs Complete")
        userIn= input("Would you like to run another playbook? Y/N\n")
        if userIn.upper()=="Y":
                start()
        else:
                print("Bye Bye")


#Old Logging Function depricated
def logging(playBook):
        #Getting Date and time
        today= datetime.utcnow()
        d = today.strftime("%b-%d-%Y")
        t = today.strftime("%H:%M:%S")

        print("Writing Logs...")
        #Writing to logs file
        f=open("logs.txt", "a")
        f.write(d+","+t+","+ playBook+","+"\n")
        f.close()

        print("Logs Complete")
        userIn= input("Would you like to run another playbook? Y/N\n")
        if userIn.upper()=="Y":
                start()
        else:
                print("Bye Bye")

start()
