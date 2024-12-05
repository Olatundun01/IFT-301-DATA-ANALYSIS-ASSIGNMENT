# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:56:55 2024

@author: ESTHER OLATUNDUN
"""
import matplotlib.pyplot as plt

music_group = [15.2, 16.1, 14.8, 15.9, 15.6, 16.0, 15.5, 14.7, 15.3, 16.2]
no_music_group = [13.8, 13.5, 13.9, 14.1, 14.0, 13.7, 14.2, 13.6, 13.8, 13.9]
plt.hist(music_group, bins=5, alpha=0.5, label='Music', color='green', edgecolor='black')
plt.hist(no_music_group, bins=5, alpha=0.5, label='No Music', color='orange', edgecolor='black')
plt.xlabel('Plant Height (cm)')
plt.ylabel('Frequency')
plt.title('Histogram of Plant Heights by Condition')
plt.legend()
plt.show()