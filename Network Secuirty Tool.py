import string
import platform
import socket 
import os 


def greet_user():

    print ("Welcome to the Network Security Tool \n")


greet_user()



def show_menu():

    print ("1. System Information," \
    " 2. Network Information," \
    " 3. Connection Check," \
    " 4. Port Check," \
    " 5. Exit "\
        )


while True:

    show_menu()

    user_choice = input ("\n Choose an option: ")

    if user_choice == "1":

        print ("System Informtaion Selected. ")

        #System Information
        
        print (f"This is your Opperating System: {platform.system()}")
        print (f"This is your Network Name: {platform.node()}")
        print (f"This is your Processor: {platform.processor()}")
        print (f"This is your Machine type: {platform.platform()}")
        print (f"This is your Python Version: {platform.python_version()}")
        

    elif user_choice == "2":

        print ("Network Information selected.")

        #Network Information
        
        host_name = socket.gethostname()
        IP_addess = socket.gethostbyname(host_name)

        print (f"Host Name: {host_name}")
        print (f"IP Address: {IP_addess}")


    elif user_choice == "3":

        print ("Connection Check Selected.")

        #Connection Check

        response = os.system ("ping -n 1 8.8.8.8 > nul 2>&1")

        print ("\n CHECKING...")

        if response == 0:
            print ("\n SUCCESS \n  You have a live internet connection. \n")

        else:

            print ("FAILED \n  Destination unreachable. You do not have a live connection. \n")

    elif user_choice == "4":

        print ("Port Check Selected.")

        #Port check

        target = input ("Enter Target: ")

        port = int(input ("Enter Port: "))

        user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        connection_result = user_socket.connect_ex((target, port))

        if connection_result == 0:

            print ("Port is open")

        else:

            print ("Port is closed")



    elif user_choice == "5":

        print ("\n Exiting...")
        break
        
    else:
    
        print ("Please choose one of the options provided")
        