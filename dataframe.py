# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import pandas as pd
import numpy as np

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=898")
poke_arr = []
type1 = []
type2 = []
ability_1 = []
ability_2 = []
ability_3 = []
#Stats Order: HP, Attack, Defense, Sp Attack, Sp Defense, Speed
hp = []
attack = []
defense = []
sp_atk = []
sp_def = []
speed = []
poke_img = []

for ele in response.json()['results']:
    #Store pokemon name
    poke_arr.append(ele['name'].capitalize())
    
    #Request additional pokemon information
    req_string = "https://pokeapi.co/api/v2/pokemon/" + ele['name']
    poke_response = requests.get(req_string)
    
    #Store pokemon type
    if len(poke_response.json()['types']) == 2:
        type1.append(poke_response.json()['types'][0]['type']['name'].capitalize())
        type2.append(poke_response.json()['types'][1]['type']['name'].capitalize())
    elif len(poke_response.json()['types']) == 1:
        type1.append(poke_response.json()['types'][0]['type']['name'].capitalize())
        type2.append("None")

    #Store pokemon abilities
    if len(poke_response.json()['abilities']) == 3:
        ability_1.append(poke_response.json()['abilities'][0]['ability']['name'].capitalize())
        ability_2.append(poke_response.json()['abilities'][1]['ability']['name'].capitalize())
        ability_3.append(poke_response.json()['abilities'][2]['ability']['name'].capitalize())
    elif len(poke_response.json()['abilities']) == 2:
        ability_1.append(poke_response.json()['abilities'][0]['ability']['name'].capitalize())
        ability_2.append(poke_response.json()['abilities'][1]['ability']['name'].capitalize())
        ability_3.append("None")
    elif len(poke_response.json()['abilities']) == 1:
        ability_1.append(poke_response.json()['abilities'][0]['ability']['name'].capitalize())
        ability_2.append("None")
        ability_3.append("None")
    
    #Store pokemon stats
    hp.append(poke_response.json()['stats'][0]['base_stat'])
    attack.append(poke_response.json()['stats'][1]['base_stat'])
    defense.append(poke_response.json()['stats'][2]['base_stat'])
    sp_atk.append(poke_response.json()['stats'][3]['base_stat'])
    sp_def.append(poke_response.json()['stats'][4]['base_stat'])
    speed.append(poke_response.json()['stats'][5]['base_stat'])
    
    #Store Pokemon image for HTML page
    poke_img.append(poke_response.json()['sprites']['front_default'])
    

poke_df = pd.DataFrame({'Sprite': poke_img,
     'Name': poke_arr,
     'Type 1': type1,
     'Type 2': type2,
     'Ability 1': ability_1,
     'Ability 2': ability_2,
     'Ability 3': ability_3,
     'HP': hp,
     'Attack': attack,
     'Defense': defense,
     'Special Attack': sp_atk,
     'Special Defense': sp_def,
     'Speed': speed})

poke_df.to_csv('pokemon.csv', index=False)

print(poke_df)