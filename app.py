# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 18:27:09 2021

@author: frimt
"""

import copy
from constants import PLAYERS

def basketball_tool():
    alt_players = copy.deepcopy(PLAYERS)
    alt_teams = []

    Panthers = []
    Bandits = []
    Warriors = []

    alt_teams.append(Panthers)
    alt_teams.append(Bandits)
    alt_teams.append(Warriors)
    while True:
        

        for player in alt_players:
            player['height'], units = player['height'].split()
            player['height'] = int(player['height'])

            player['guardians'] = player['guardians'].split("and")
            player['guardians'] = " ,".join(player['guardians'])

            if player['experience'] == 'YES':
                player['experience'] = True
            else:
                player['experience'] = False

        experience = []
        inexperience = []


        for player in alt_players:
            if player['experience']:
                experience.append(player)
            else:
                inexperience.append(player)

        alt_players = []
        alt_players = experience + inexperience

        for player in alt_players:
            if alt_players.index(player) % len(alt_teams) == 0:
                alt_teams[0].append(player)
            elif alt_players.index(player) % len(alt_teams) == 1:
                alt_teams[1].append(player)
            else:
                alt_teams[2].append(player)


        print("BASKETBALL TEAM STATS TOOL")

        options = input(
            "Here are your choices:\n A) Display Team Stats \n B) Quit \n.......")
        if options.upper() == "A":
            team_selection = input(
                'Enter an option  \n A) Panthers  \n B) Bandits  \n C) Warriors\n.......')
            if team_selection.upper() == "A":

                print("Team Panthers Stats")
                print("-------------------")
                print("total players : ", len(Panthers))
                team = []

                for i in range(len(Panthers)):
                    player = Panthers[i]
                    player1 = player['name']
                    team.append(player1)

                team1 = ", ".join(team)
                print("Player Names: ", team1)
                guardians_list = []
                for i in range(len(Panthers)):
                    player = Panthers[i]
                    guardian = player['guardians']
                    guardians_list.append(guardian)

                guardians_str = ", ".join(guardians_list)[0:]
                print("Guardian Names: ", guardians_str)

                exp = 0
                for player in Panthers:
                    if player['experience'] == True:
                        exp += 1
                print('Number of experienced players is: ', exp)
                print("Number of inexperienced players is: ", len(Panthers) - exp)
                height = []
                for player in Panthers:

                    height.append(player['height'])

                print('Average height of Players in Team is: ',
                      int(sum(height)/len(Panthers)), 'inches')
                break

            elif team_selection.upper() == "B":
                print("Team Bandits Stats")
                print("-------------------")
                print("total players : ", len(Bandits))
                team = []

                for i in range(len(Bandits)):
                    player = Bandits[i]
                    player1 = player['name']
                    team.append(player1)

                team1 = ", ".join(team)
                print("Player Names: ", team1)
                guardians_list = []
                for i in range(len(Bandits)):
                    player = Bandits[i]
                    guardian = player['guardians']
                    guardians_list.append(guardian)

                guardians_str = ", ".join(guardians_list)[0:]
                print("Guardian Names: ", guardians_str)

                exp = 0
                for player in Bandits:
                    if player['experience'] == True:
                        exp += 1
                print('Number of experienced players is: ', exp)
                print("Number of inexperienced players is: ", len(Panthers) - exp)
                height = []
                for player in Bandits:

                    height.append(player['height'])

                print('Average height of Players in Team is: ',
                      int(sum(height)/len(Bandits)), 'inches')
                break

            elif team_selection.upper() == "C":
                print("Team Warriors Stats")
                print("-------------------")
                print("total players : ", len(Warriors))
                team = []

                for i in range(len(Warriors)):
                    player = Warriors[i]
                    player1 = player['name']
                    team.append(player1)

                team1 = ", ".join(team)
                print("Player Names: ", team1)
                guardians_list = []
                for i in range(len(Warriors)):
                    player = Warriors[i]
                    guardian = player['guardians']
                    guardians_list.append(guardian)

                guardians_str = ", ".join(guardians_list)[0:]
                print("Guardian Names: ", guardians_str)

                exp = 0
                for player in Warriors:
                    if player['experience'] == True:
                        exp += 1
                print('Number of experienced players is: ', exp)
                print("Number of inexperienced players is: ", len(Panthers) - exp)
                height = []
                for player in Warriors:

                    height.append(player['height'])

                print('Average height of Players in Team is: ',
                      int(sum(height)/len(Warriors)), 'inches')
                break
            else:
                print("Not a valid response. Please try again1")
                continue
    
        elif options.upper() == "B":
            print("Thanks for playing")
            break
        else:
            print("Not a valid respose. please Try again2")
            continue

    
if __name__ == "__main__":

    basketball_tool()
    
    replay_stats = input("Would you like to see stats again: Yes / No    ")
    while replay_stats.upper() == "YES":
        basketball_tool()
        replay_stats = input("Would you like to see stats again: Yes / No    ")
    else:
        print("Have a great Day!!!")

