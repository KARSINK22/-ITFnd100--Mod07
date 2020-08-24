# ------------------------------------------------- #
# Title: Assignment 07
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# K. Sinkevitch,8/24/20,Modified code to complete assignment 7
# ------------------------------------------------- #
import pickle  # Import pickle module to read and write binary files

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []
lstFileData = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    #  TODO: store the list object into a binary file
    """ Saves data to a binary file

    :param file_name: (string) name of file:
    :param list_of_data: (list) list of data to save to file:
    :return: (string) status message
    """
    strFunctionStatus = "Data saved to binary file"
    objFile = None

    try:
        objFile = open(file_name, "wb")  # Open file as write binary
        pickle.dump(list_of_data, objFile)
    except IOError as er:  # IO error occurred
        print("There was an error opening or saving the data to the file", file_name)
        print("Built-In Python error info: ")
        print(er, e.__doc__, type(e), sep='\n')
        strFunctionStatus = "Program has stopped execution"
    except Exception as er:  # Non-specific error occurred
        print("There was a non-specific error when opening or saving data to the file", file_name)
        print("Built-In Python error info: ")
        print(er, er.__doc__, type(e), sep='\n')
        strFunctionStatus = "Program has stopped execution"

    objFile.close()  # close file object
    return strFunctionStatus  # return function status string

def read_data_from_file(file_name):
    """ Reads data from a binary file

    :param file_name: (string) name of file:
    :return: (list) list of data from file, (string) status message
    """
    strNewList = []  # Set list to empty set
    strFunctionStatus = "Data read from binary file"
    try:
        objFile = open(file_name, "rb")  # Open file as read binary
        while True:
            try:
                row = pickle.load(objFile)  # Read each row of data
            except EOFError:
                break
            strNewList.append(row)  # Add row of data to list
        objFile.close()  # close file object
    # except IOError as e: # IO error occurred
    #     print("There was an error reading data from the file", file_name)
    #     print("Built-In Python error info: ")
    #     print(e, e.__doc__, type(e), sep='\n')
    # strFunctionStatus = "Program has stopped execution"
    except Exception as er:  # Non-specific error occurred
        print("There was a non-specific error when reading data from the file", file_name)
        print("Built-In Python error info: ")
        print(er, er.__doc__, type(e), sep='\n')
        strFunctionStatus = "Program has stopped execution"

    return strNewList, strFunctionStatus  # Return list of data and function status string

def print_items_in_list(list_of_rows):
    """ Prints items in a list to the screen

    :param list_of_rows: (list) of rows you want to display
    :return: nothing
    """
    print("******* The current customer list is: *******")
    for row in list_of_rows:
        print(row)
    print("*******************************************")


# Presentation ------------------------------------ #

# TODO: Get ID and NAME From user, then store it in a list object
# Prompt user to enter customer IDs and names until user is done
while True:  # Continue to request user input until choice to add data is no
    try:  # Check that entry is an integer
        intId = int(input("Please enter the integer ID: "))  # Prompt user for ID
    except ValueError as e:  # Handle non-integer value error
        intId = 1
        print("ID requires an integer value, ID has been set to 1")

    strCustomerName = input("Please enter customer name: ")  # Prompt user for customer name
    # Append ID and customer name to list
    lstCustomer.append([intId, strCustomerName])

    # Prompt user on whether to enter more customer data or stop
    strChoice = input("Would you like to add more customer data (y/n): ")
    if strChoice.lower() == "n":  # Save the data entered and exit loop
        # Call function to save data to file
        strMsg = save_data_to_file(strFileName, lstCustomer)
        print(strMsg)  # Print function status message
        break  # Exit loop

# TODO: Read the data from the file into a new list object and display the contents
strInput = input("Would you like to view the contents of the file created (y/n)?: ")
if strInput.lower() == "y":
    # Call function to read data from file
    lstFileData, strMsg = read_data_from_file(strFileName)
    print(strMsg)  # Print function status message
    print_items_in_list(lstFileData)  # Print list of items from file
