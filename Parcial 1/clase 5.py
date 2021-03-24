# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:33:42 2021

@author: RAYMUNDO
"""

import yfinance as yf
from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%
tickerSymbol= 'AMZN'
tickerData= yf.Tiker(tickerSymbol)
#print(tickerData.info)
data=tickerData.history(period='1d',start='2010-1-1',end='2021-01-01')

data=pd.DataFrame(data.Close)

data['R']=data.Colse.pct_change()
data['r']= np.log(data.Close)-np.log(data.Close.shift(1))

#%%
from scipy.stats import ttest_ind,ttest_ind_from_stats

data1=date.dropna()

meanR=data1.R.mean()
meanr=data1.r.mean()

alpha=0.05

#Supuesto en donde las varianzas son iguales
t,p=ttest_ind(a,b)

if p<alpha:
    print('Se rechaza la Ho, las medias no son iguales')
else:
    print('No se puede rechazar la Ho, *Las medias son iguales*')

#Validar si las varianzas con Levene
w,p_w=stats_levene(a,b)

if p_w<alpha:
    print('Se rechaza la Ho, las medias no son iguales')
else:
    print('No se puede rechazar la Ho, *Las medias son iguales*')
