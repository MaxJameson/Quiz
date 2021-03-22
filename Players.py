#Title                 : Players
#Functions/classes     : player(___init___, storeScore,getName, getName, getScore)
#Use                   : Creates player object
#Creator               : Max Jameson
#Student ID            : 19702735



#Imports error and time modules for use in the program
import ErrorChecker as EC
from datetime import datetime

#Defines the player class
class player:

    #A method which runs when the class is initialised
    def __init__(self):

        #Sets a date attribute for the class
        self.date = datetime.now()

        #A Boolean to test for typing errors
        error = True

        #A loop which runs until the player makes a valid input
        while error == True:

            #Takes a name input from the user
            self.name =  input("What is your name: ")

            #Passes the input to the error checking module
            error = EC.ifString(self.name)
            
    #Defines the storeScore method
    def storeScore(self,score):

        #Stores the score parameter as an object attribute
        self.score = score

    #Defines the getName method
    def getName(self):

        #Returns the name attribute back to the program
        return self.name

    #Defines the getScore method
    def getScore(self):

        #Returns the score attribute back to the program
        return self.score

    #Defines the getDate method
    def getDate(self):

        #Returns the date attribute back to the program
        return self.date
    
