# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:47:23 2024

@author: ESTHER OLATUNDUN
"""
import matplotlib.pyplot as plt

breath_holding_times = [22.22, 30.57, 17.47, 22.39, 26.90, 36.85, 27.33, 29.55, 13.87, 34.66, 
                        60.75, 67.41, 42.19, 59.74, 52.64, 43.37, 73.27, 59.09, 51.15, 58.32]

plt.hist(breath_holding_times, bins=8, color='blue', alpha=0.7, edgecolor='black')
plt.xlabel('Breath-Holding Time (seconds)')
plt.ylabel('Frequency')
plt.title('Histogram of Breath-Holding Times')
plt.show()