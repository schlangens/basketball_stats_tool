# Import player data
import constants
import copy
import sys


cleaned_data = []
height_data = []
experienced = []



def fetch_data():
    for count, player in enumerate(constants.PLAYERS):
        cleaned_data.append(player)
        # print(cleaned_data)  

# Create a clean_data function
def clean_data():
    for index,item in enumerate(cleaned_data, 1):
        print(f"{index}, {item}") # we are no printing the values from our CONSTANTS 
       
        
                


def start():
    print("Basketball Team Stats Tool")
    print ("--------------------------")
    # First Question
    print ("Here are your choices: \n")
    print ("a) Display Team Stats \n")
    print ("b) Quit \n")
    first_question = input("Enter an option:  (a/b)")
    print ("--------------------------")
    if first_question == 'a':
        print("a) Panthers \n")
        print("b) Bandits \n")
        print("c) Warriors \n")
        second_question = input("Enter an option: (a/b/c) or q for quit \n")
        print ("--------------------------")
        if second_question == "a":# Panthers
            panther()
        if second_question == "b": # Bandits
            print("Team: {team_name}")
            print("--------------------------")
            print("Players on Team: \n")
            print("{player_names}")
        if second_question == "c": # Warriors
            print("Team: {team_name}")
            print("--------------------------")
            print("Players on Team: \n")
            print("{player_names}") # PRINT CSV for ", "   
        if second_question == "q":
            print("Maybe next time we can check those stats out! Closing the program now.")
            sys.exit()  
    if first_question == 'b':
        print("Maybe another time eh? Closing the program now.")
        sys.exit()    


#v Proper use of Dunder Main
if __name__ == '__main__':
    # start() # Main app function 
    fetch_data()
    clean_data()
