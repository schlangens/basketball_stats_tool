# Import player data
import constants
import sys

cleaned_list = []

# Create a clean_data function
def clean_data():
    for item in constants.PLAYERS:
        item['height'] = int(item['height'].split()[0]) # Saved as int
        # print("That player is", item['height'], "inches tall") #Prints the height with 
        cleaned_list.append(item['height']) # adds cleaned int to list    

# Create a balance_teams function


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
            print("Team: {team_name}")
            print("--------------------------")
            print("Total Players: {total_players}")
            print("Players on Team: \n")
            print("{player_names}")
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
    #start() # Main app function 
    clean_data()
