# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 18:27:09 2021

@author: frimt
"""
import copy

from constants import PLAYERS

alt_players = copy.deepcopy(PLAYERS)
alt_teams = [] 



Panthers = []
Bandits = []
Warriors = []
for player in alt_players:
    player['height'], units = player['height'].split()
    player['height'] = int(player['height'])
    
    if player['experience'] == 'YES':
        player['experience'] = True
    else:
        player['experience'] = False
        
experience = []
inexperience = []

for player in alt_players:
    if player['experience'] == 'YES':
        experience.append(player)
    else:
        inexperience.append(player)
    
print(experience)
print(inexperience)

    

        
      




