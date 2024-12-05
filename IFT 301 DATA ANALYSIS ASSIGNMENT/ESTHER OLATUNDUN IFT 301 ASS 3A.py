# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:55:38 2024

@author: ESTHER OLATUNDUN
"""

import matplotlib.pyplot as plt

music_group = [15.2, 16.1, 14.8, 15.9, 15.6, 16.0, 15.5, 14.7, 15.3, 16.2]
no_music_group = [13.8, 13.5, 13.9, 14.1, 14.0, 13.7, 14.2, 13.6, 13.8, 13.9]

plt.plot(['Music'] * len(music_group), music_group, 'o', label='Music', color='green')
plt.plot(['No Music'] * len(no_music_group), no_music_group, 'o', label='No Music', color='orange')
plt.ylabel('Plant Height (cm)')
plt.title('Dot Plot of Plant Heights by Condition')
plt.legend()
plt.show()