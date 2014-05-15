# -*- coding: utf-8 -*-
'''
Created on 13-05-2014

@author: leonardo jofre
'''

import random
import numpy as np
import re

def get_pattern(text, rank, word):
    # pasarlo a un array
    text = np.array(text)
    # buscamos la palabra casa
    pattern = re.compile(word)
    
    # el computador que tenga rank = 1 busca en el string formado de dos en dos
    rank = 1
    
    text_rank1 = text[np.arange(0, N, rank + 1)]
    text_rank1 = text_rank1.tolist()
    text_rank1 = "".join(text_rank1)
    
    # buscamos las coincidencias de la palabra casa dentro de este string
    return pattern.findall(text_rank1)
    




