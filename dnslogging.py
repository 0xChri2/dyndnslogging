import socket
from datetime import datetime
import csv
import time

domain = 'google.com'
# Get first IP from Hostname
addr = socket.gethostbyname(domain)

# Timestamp
now = datetime.now()
nowstr = now.strftime("%d/%m/%Y %H:%M:%S")


#print in csv file
with open('dnslookup.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([nowstr, addr])




#Output
print("DNS Lookup for ", domain ," is: ", addr)
print("Date and Time: ", nowstr)

#do while loop to keep running


while 1:
    newaddr = socket.gethostbyname(domain)
    time.sleep(1)
#compare old and new IP
    if addr != newaddr:
        print("Address of ", domain ," is now:", newaddr)
        print("Date and Time: ", nowstr)
        with open('dnslookup.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([nowstr, addr])
        addr = newaddr
