# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:40:18 2024

@author: ESTHER OLATUNDUN
"""
import matplotlib.pyplot as plt
import numpy as np

#Data
ingredients = ['Spinach', 'Sausage', 'Prawns', 'Pineapple', 'Mushroom']
proportions = [0.275, 0.175, 0.075, 0.275, 0.175]

#Create bar chart
plt.barh(ingredients, proportions, color='purple')

#Set title and labels
plt.title('Proportion of Ingredients')
plt.xlabel('Proportion')
plt.ylabel('Ingredients')

#Show chart
plt.show()
