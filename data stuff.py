# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 23:49:58 2021

@author: david
"""

import pandas as pd
import numpy as np

new_poke_df = pd.read_csv('pokemon.csv')  

new_poke_df['Sprite'] = new_poke_df.apply(lambda row : "<img src=\"" + 
                                       row["Sprite"] + "\">", axis = 1)

new_poke_df.index = [i for i in range(1,899)]

html = new_poke_df.to_html()