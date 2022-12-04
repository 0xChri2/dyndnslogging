# dyndnslogging

This script, called dyndnslogging, performs a DNS lookup on the specified domain and logs the IP address and date and time to a CSV file. The script then enters an infinite loop, in which it continuously performs DNS lookups and checks if the IP address has changed. If the IP address has changed, the new IP address and date and time are logged to the CSV file.
## Requirements

   - Python 3.x
   - The socket and csv modules (included with Python by default)

## Usage

To run the script, open a terminal or command prompt and navigate to the directory containing the script. Then, run the following command:

```python dyndnslogging.py```

By default, the script performs a DNS lookup on the domain google.com and logs the results to a CSV file called dyndnslogging.csv. To perform a DNS lookup on a different domain, edit the domain variable at the top of the script file.
Output

The script outputs the IP address and date and time of the initial DNS lookup to the console, and logs the results to the CSV file. If the IP address changes, the new IP address and date and time are also logged to the CSV file.

The CSV file has the following format:

```<timestamp>,<ip_address>```

where <timestamp> is the date and time of the DNS lookup in the format DD/MM/YYYY HH:MM:SS, and <ip_address> is the IP address of the domain.
