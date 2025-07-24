#Import random library
import random

#Setting important variables
score = 0

responseCorrect = "Correct! You were exactly right! {} points!"
response5 = "You were close! The right answer was {}! {} points!"
response10 = "You were 10 or less years off! The right answer was {}! {} points!"
response20 = "Your were off! The right answer was {}! {} point!"
responseIncorrect = "You were way off! The right answer was {}! {} points!"

endResponse = "Thanks for playing! Your final score was {}!"

questionList = [
    ("the start of the Revolutionary War", 1775),
    ("the United States Constitution signed", 1783),
    ("President Lincoln assassinated", 1865),
    ("Theodore Roosevelt's first day in office as President of the United States", 1901),
    ("the beginning of World War II", 1939),
    ("the first personal computer introduced", 1975),
    ("the Berlin Wall taken down", 1989),
    ("the attack on Pearl Harbor", 1941),
    ("the first solo nonstop transatlantic flight undertaken?", 1927),
    ("the 22nd amendment ratified?", 1951)
    ]

questionText = "In what year was {}?\n> "

#Function for checking answers
#Takes absolute value of difference between input and answer and uses that to determine score added and display appropriate response
def checkAnswer(input, answer):
    global score
    difference = abs(answer - input)

    if difference == 0:
        print(responseCorrect.format(10))
        score += 10
    elif difference <= 5:
        print(response5.format(answer, 5))
        score += 5
    elif difference <= 10:
        print(response10.format(answer, 2))
        score += 2
    elif difference <= 20:
        print(response20.format(answer, 1))
        score += 1
    elif difference > 20:
        print(responseIncorrect.format(answer, "No"))

#Shuffle question list
random.shuffle(questionList)

#Loops through question list and prints a response with the score added
#If user input is a number and can be converted to an int, it will be stored in "a" and checked
#If conversion fails (not a number, no input, etc.), print a message asking the user for a number, and ask for input again until valid
for i, item in enumerate(questionList, 0):
    a = "answer"
    
    while True:
        try:
            print("------------------------------------------------------------------------------------------------------------------------")
            a = int(input(questionText.format(questionList[i][0])))
            checkAnswer(a, questionList[i][1])
            break
        except:
            print("Please enter a number!")

#Print end response with score
print("------------------------------------------------------------------------------------------------------------------------")
print(endResponse.format(score))
print("------------------------------------------------------------------------------------------------------------------------")