# Dynamic DNS Logger

This script is a simple tool for logging the IP address of a given domain name. It does the following:

   1. Takes a domain name as a command-line argument and looks up the IP address for that domain.

   2. Prints the IP address and the current date and time to the console.

   3. Enters an infinite loop that checks the IP address for the domain every second. If the IP address has changed, the new IP address and the current date and time are printed to the console.

   4. If the IP address has changed, the date, time, and new IP address are also written to a CSV file called "dyndnslogging.csv".

## Requirements

   - Python 3

## Usage

To use the script, run the following command, replacing example.com with the domain name you want to monitor:

´´´python3 dyndnslogger.py example.com´´´

The script will then print the current IP address for the domain, as well as the current date and time. It will then enter an infinite loop, checking the IP address for the domain every second, and printing any updates to the console.

## License

This script is provided under the MIT License. See the LICENSE file for details.