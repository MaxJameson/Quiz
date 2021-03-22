#Title                 : Quiz
#Functions/classes     : main, runQuiz, correction
#Use                   : Runs a quiz from provided text file 
#Creator               : Max Jameson
#Student ID            : 19702735




#Imports error, player, operator and time modules for use in the program
import ErrorChecker as EC
from Players import player as p
from datetime import datetime
import operator



#A function which runs the quiz
def runQuiz(questionFile):

        #Sets score and counter to 0
        counter = 0
        score = 0 

        #A loop which iterates through each line in the selected file
        for line in questionFile:

                #Increase the counter by one
                counter = counter + 1
                print("")

                #Converts the current line into a string
                line = str(line)

                #Finds where the question ends in the string and stores the question
                questionEnd = line.find('?')
                question = line[:questionEnd+1]
                
                #Finds the answer choices within the string and stores them as one string
                choices = line[questionEnd+2:-3]

                #Splits the answers up using a list
                ChoicesOutput = choices.split(',')

                #Finds the number which corresponds to the answer
                answerNumber = int(line[-2])

                #Uses the answer number to find the answer in the choices list
                answer = ChoicesOutput[answerNumber-1]

                #Passes the answer into the correction function
                answer = correction(answer)

                #Prints the question and answer choices
                print("Question",counter)
                print(question)
                print(ChoicesOutput)

                #Takes an answer input from the user
                UserAnswer = str(input("Type your answer: "))
                UserAnswer = correction(UserAnswer)
                print("")

                #A conditional to test if the user inputs the correct answer
                if UserAnswer == answer:

                        #Lets the user know they got the answer correct and increments the score
                        print("You got it right")
                        score = score + 1

                else:

                        #Lets the user know they got the answer wrong and increments the score
                        print("Incorrect")

        #Stores the score in the name object 
        name.storeScore(score)

        #Returns the value of counter to the program
        return counter



#A function which corrects entered strings                
def correction(correctable):

        #Makes the string lower case
        correctable = correctable.lower()

        #Removes all spaces from the string
        correctable = correctable.replace(" ","")

        #Returns the altered string to the program
        return correctable




#Main program

#Creates a name object from the player class Object
name = p()

#Boolean to test quiz selection
quiz = False

#A loop which runs until the player selects a valid quiz option
while quiz == False:

        #A Boolean to test for typing errors
        error = True

        #A loop which runs until the player makes a valid input
        while error == True:

                #Takes a quiz choice input from the user
                quizChoice = (input("Would you like to do quiz 1 or 2? "))

                #Passes the input to the error checking module
                error = EC.ifNumber(quizChoice)

        #Gives the user rules for using the quiz
        print("")
        print("When answering questions either type out your selected answer")
        print("")
        
        #A conditional statement to test which quiz was chosen
        if int(quizChoice) == 1:

                #Lets the whole loop know a correct input was make
                quiz = True
                print("Lets begin")

                #Opens the quiz file
                with open("quiz.txt") as file:

                        #Passes the file into the runQuiz function
                        counter = runQuiz(file)

                        #Set the correct leaderboard in comparison to the quiz
                        leaderboard = "leaderboard.txt"
                        
                        print("")
      

        elif int(quizChoice) == 2:

                quiz = True
                print("Lets begin")

                #Opens the quiz2 file
                with open("quiz2.txt") as file:
        
                        
                        counter = runQuiz(file)

                        #Set the correct leaderboard in comparison to the quiz
                        leaderboard = "leaderboard2.txt"
                        print("")

        else:
                #Lets the user know they have made an incorrect input
                print("This is not a valid input Please choose between quiz 1 and 2")
    

#Prints the users score
print("Well done, you scored",name.getScore(),"out of",counter)
print("")
print("Updating leaderboard to contain your score...")
print("")

#Opens the selected leaderboard in append mode
with open(leaderboard, "a") as file:

        #Appends the users name, score and date to the selected leaderboard file
        write = str(name.getScore()) + ", " + str(name.getName()) + ", " + str(name.getDate())
        file.write(write + '\n')

        #Closes the file
        file.close

#Opens the selected leaderboard in read mode
with open(leaderboard, "r") as file:

        #Creates a list to store the leaderboard
        leaderboardList = []

        #A loop which iterates through each line in the selected file
        for lines in file:

                #removes the newline symbol from the output
                newline = lines.find("\n")
                lines = lines[:newline]

                #Splits the line up into a list
                lines = lines.split(",")

                #Modifies the list so that the score is seen as an integer
                lines = [lines[1],int(lines[0]),lines[2]]

                #Appends the line list to the leaderboard List
                leaderboardList.append(lines)

        #Sorts the leaderboard into score order
        leaderboardList.sort(key = operator.itemgetter(1), reverse = True)

        #A loop which iterates through each element in the list
        for i in leaderboardList:

                #Output the current element
                print(i)

                

        #Closes the file       
        file.close

#Asks for an input to end the program        
print("")
input("Press enter to end the program")
exit()
