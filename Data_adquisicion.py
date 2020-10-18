# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import re 
import seaborn as sns
import matplotlib.pyplot as plt

#testing the best way to import the data

signal=pd.read_csv('Signals/1-1-post bipolar_P657_ECG_Export.txt', header=3, delimiter=r"\s+")



graf=sns.lineplot(data=signal[['I(110)','II(111)','III(112)']])

fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
fig.subplots_adjust(hspace=0.4)
ax1.set_title('I')
ax2.set_title('II')
ax3.set_title('III')
ax1.plot(signal['I(110)'])
ax2.plot(signal['II(111)'])
ax3.plot(signal['III(112)'])

