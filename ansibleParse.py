import re
import pytz
import os
from datetime import date
from datetime import datetime
import linecache
os.system("ansible-playbook /path/to/playbook -e  | tee /path/to/logfile.txt")

# read second line
venue = linecache.getline(r"/path/to/logfile.txt", 2)
first = venue.find("[")+1
last = venue.find("]")
venue=venue[first:last]

# Initialize variables to store the data
successful_devices = set()
failed_devices = set()
unreachable_devices = set()

# Open the log file
with open("/path/to/logfile.txt"", "r") as file:
    for line in file:
        if 'ok=' in line:
            match = re.search(r"(\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b)", line)
            if match:
                if 'unreachable=0    failed=0' in line:
                    successful_devices.add(match.group(1))
                elif "unreachable=1" in line:
                    unreachable_devices.add(match.group(1))
                else:
                    failed_devices.add(match.group(1))


#Gettig time from localtime
today= datetime.now(pytz.timezone("US/Central"))
d = today.strftime("%m-%d-%Y_")
t = today.strftime("%H:%M:%S")
fname =d +"T"+ t

#Clearing output file path
os.system("rm /path/to/parselogfile.txt")
os.system("touch rm /path/to/parselogfile.txt")

#opening log file
f = open("rm /path/to/parselogfile.txt","w")

#writing to outputfile
f.write("Successful Devices:\n")
for val in successful_devices:
        f.write(val+"\n")
f.write("\n")
f.write("Failed Devices:\n")
if len(failed_devices) == 0:
        f.write("None\n")
else:
        for val in failed_devices:
                f.write(val+"\n")
f.write("\n")
f.write("Unreachable Devices:\n")
if len(unreachable_devices) == 0:
        f.write("None")
else:
        for val in unreachable_devices:
                f.write(val+"\n")
f.close()
with open("rm /path/to/parselogfile.txt","r") as f:
        data = f.read()

#Sending email
subject =venue+ " "+ fname
os.system("echo \""+data+"\" | mail -aFrom:user@email.com  -s \""+subject+"\" user@email.com")

