# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 00:21:51 2025

@author: Carlos Gil
"""

import string
import re

titulo=[]
i=0

with open('texto_tarea.txt')as archivo:
    for linea in archivo:
       if re.search(r'^\d+\.\-\s', linea):
           titulo.append(linea.strip())

print("titulos:")
for title in titulo:
    print(title)