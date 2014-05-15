'''
Created on 14-05-2014

@author: leonardojofre
'''

import random
from tools.serial import get_pattern
# a modo de ejemplo generamos un array de numeros aleatorios
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

# Generamos un vector aleatorio con esta informacion posible
N = 1000000
text = [random.choice(alfabeto) for _ in range(N)]

match = get_pattern(text=text, rank=2, word="casa")
print match
