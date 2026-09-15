import platform
import socket 
import os 



print ("\nWelcome to the Network Security Tool")


def show_menu():

    print ("\n1. System Information \n2. Network Information \n3. Connection Check \n4. Port Check \n5. Exit ")


while True:

    show_menu()

    user_choice = input ("\nChoose an option: ").strip()

    if user_choice == "1":

        print ("\nSystem Information Selected.\n ")

        #System Information
        
        print (f"This is your Operating System: {platform.system()}")
        print (f"This is your Network Name: {platform.node()}")
        print (f"This is your Processor: {platform.processor()}")
        print (f"This is your Machine type: {platform.platform()}")
        print (f"This is your Python Version: {platform.python_version()}")
        

    elif user_choice == "2":

        print ("\nNetwork Information selected.\n")

        #Network Information
        
        host_name = socket.gethostname()
        IP_address = socket.gethostbyname(host_name)

        print (f"Host Name: {host_name}")
        print (f"IP Address: {IP_address}")


    elif user_choice == "3":

        print ("\nConnection Check Selected.")

        #Connection Check

        print ("\nCHECKING...")

        response = os.system ("ping -n 1 8.8.8.8 > nul 2>&1")

        if response == 0:
            print ("\nSUCCESS \n \nYou have a live internet connection. \n")

        else:

            print ("FAILED \n \nDestination unreachable. You do not have a live connection. \n")

    elif user_choice == "4":

        print ("\nPort Check Selected.\n")

        #Port Check

        target = input ("Enter Target: ")

        port = int(input ("Enter Port: "))

        user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        connection_result = user_socket.connect_ex((target, port))

        if connection_result == 0:

            print ("\nPort is open")

        else:

            print ("\nPort is closed")



    elif user_choice == "5":

        print ("\nExiting...\n")
        break
        
    else:
    
        print ("\nPlease choose one of the options provided")
        