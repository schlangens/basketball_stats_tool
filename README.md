Python Techdegree
Project 2 - Basketball Team Stats Tool
Scott Schlangen - V1 - 09/06/2021


# Basketball Team Stats Tool
In this project you will be writing a program that reads from the "constants" data (`PLAYERS` and `TEAMS`) in `constants.py`. This data will need to be translated into a new collection of your choosing and the fields need to be changed to something that makes more sense for Python to do its comparisons.

**Core Requirements**

- [ ] Create a file name which contains the entry point to start your program logic.
- [ ] import and use the data from the constants.py in your program.
- [ ] The script should not crash due to uncaught exceptions. Raised exceptions should be handled appropriately so the program can continue or exit without a crash.
- [ ] Function calls, print statements, or any calculated execution logic should be wrapped inside a Dunder Main statement for you script.
- [ ] The player data imported from constants.py needs to be cleaned up and stored in new data types in a structure that makes since.
- [ ] the guardian string so that it becomes a List of strings. Remove the and between the names and storing each guardian in a List together for that player
- [ ] Convert the height string to int, the experienced string should become a boolean of:True if YES or Fale if NO
- [ ] Do not modify or mutate the imported data from the constants.py in any way
- [ ] Assign players to each team so the teams are evenly balanced by total. The order in which you assign players do not matter but should be balanced when team assignment finished. 
- [ ] The same player cannot be assigned to multiple teams
- [ ] Balance players in a way that also ensures teams have equal numbers of experienced vs inexperienced players.
- [ ] Build Menu - Display a given teams stats, quit.
- [ ] Display Stats - Team's name, Total # of Players on team, The player names(joined together as comma-separated string)
- [ ] Display Additional Stats - Total Number of inexperienced players - total number of experienced players - average height of team - guardian names of all the players on the team.

# Math formula for average height: (sum of all the heights) / (total players)