#Title                 : ErrorChecker
#Functions/classes     : ifString, ifNumber
#Use                   : Checks for incorrect inputs 
#Creator               : Max Jameson
#Student ID            : 19702735




#Defines a function to detect characters
def ifString(subject):

    #A conditional to test if the input contains only digits
    if subject.isdigit():

        #Lets the user know this input is invalid as it only contains numbers
        print("Input not valid, must be a string")

        #Returns Boolean to the program
        return True
    
    else:

        #Returns Boolean to the program
        return False
    
#Defines a function to detect numbers
def ifNumber(subject):

    #A conditional to test if the input contains only digits
    if subject.isdigit():
        
        #Returns Boolean to the program
        return False
    
    else:

        #Lets the user know this input is invalid as contains letters/symbols
        print("Input not valid, must be an integer")

        #Returns Boolean to the program
        return True

    
    
