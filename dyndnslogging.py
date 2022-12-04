import socket
import sys
from datetime import datetime
import csv
import time

def nowtime():
    now = datetime.now()
    nowstr = now.strftime("%d/%m/%Y %H:%M:%S")
    return nowstr

def write_to_csv(timestamp, addr):
    with open('dyndnslogging.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([timestamp, addr])

# Get domain from command-line argument
domain = sys.argv[1]

# Get first IP from Hostname
addr = socket.gethostbyname(domain)
nowstr  = nowtime()
# Output
print("DNS Lookup for ", domain ," is: ", addr) 
# Output date and time
print("Date and Time: ", nowstr)


# Loop forever
while True:
    # Get current date and time
    nowstr  = nowtime()

    # Wait for 1 second
    time.sleep(1)

    # Get new IP from Hostname
    try:
        newaddr = socket.gethostbyname(domain)
    except socket.gaierror:
        print("Error: Unable to resolve domain name")
        continue

    # Check if IP has changed
    if addr != newaddr:
        # Output new IP
        print("Address of ", domain ," is now:", newaddr)
        print("Date and Time: ", nowstr)
        # Update stored IP
        addr = newaddr
        # Write to CSV file
        write_to_csv(nowstr, addr)