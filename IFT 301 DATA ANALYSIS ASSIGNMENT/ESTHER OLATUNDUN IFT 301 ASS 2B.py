# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:54:20 2024

@author: ESTHER OLATUNDUN
"""

import matplotlib.pyplot as plt


female_times = [22.22, 30.57, 17.47, 22.39, 26.90, 36.85, 27.33, 29.55, 13.87, 34.66]
male_times = [60.75, 67.41, 42.19, 59.74, 52.64, 43.37, 73.27, 59.09, 51.15, 58.32]

plt.plot(['Female'] * len(female_times), female_times, 'o', label='Female', color='red')
plt.plot(['Male'] * len(male_times), male_times, 'o', label='Male', color='blue')
plt.ylabel('Breath-Holding Time (seconds)')
plt.title('Dot Plot of Breath-Holding Times by Gender')
plt.legend()
plt.show()