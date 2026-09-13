import string
import platform

def greet_user():

    print ("Welcome to the Network Security Tool")


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

    user_choice = input ("Choose an option: ")

    if user_choice == "1":

        print ("System Informaion Selected. ")

        #System Information
        
        print (f"This is your Opperating System: {platform.system()}")
        print (f"This is your Network Name: {platform.node()}")
        print (f"This is your Processor: {platform.processor()}")
        print (f"This is your Machine type: {platform.platform()}")
        print (f"This is your Python Version: {platform.python_version()}")
        

    elif user_choice == "2":

        print ("Network Information selected.")

    elif user_choice == "3":

        print ("Connection Check Selected.")

    elif user_choice == "4":

        print ("Port Check Selected.")

    elif user_choice == "5":

        print ("Exiting...")
        break
        
    else:
    
        print ("Please choose one of the options provided")
        