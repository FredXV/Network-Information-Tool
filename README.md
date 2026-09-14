# Network Security Tool

A python command line tool offering a menu of networking and system information

## Features
Menu to select different tools
System information
- Operating system
- Network name
- Processor
- Machine type
- Python version
Network Information
- Host name
- Local IP address
Connection Check
- Checks if an internet connection is available
Port Check
- Allows the user to enter a target and a port
- Checks if the port is open or clossed
Exit Option

## What I learned

- Structuring a program around a menu loop
- Using Python's 'platform' module to retrieve system and OS information
- Using Python's 'socket' module for network information and port checking
- Using 'os.system()' to perform a connection check
- Understanding how 'socket.connect_ex()' works
- Creating and using socket objects
- Debugging control flow 
- Handling user input and different menu options


## How to run

python "Network Security Tool.py"

You will see a menu with 5 options. Choose System Information to see details about your machine, or Exit to close the program. The other options are still in development
