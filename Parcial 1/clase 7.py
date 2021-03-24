# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:32:33 2021

@author: RAYMUNDO
"""
import yfinance as yf
from scipy import stats
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%%  sample 1
co='AMZN'
tickerSymbol= co
tickerData= yf.Ticker(tickerSymbol)
#print(tickerData.info)
data1=tickerData.history(period='1d',start='2000-1-1',end='2008-1-1')

data1=pd.DataFrame(data1.Close)

data1["R"]=data1.Close.pct_change()
data1["r"]=np.log(data1.Close)-np.log(data1.Close.shift(1))

#%%  sample 2

tickerSymbol= co
tickerData= yf.Ticker(tickerSymbol)
#print(tickerData.info)
data2=tickerData.history(period='1d',start='2000-1-1',end='2008-1-1')

data2=pd.DataFrame(data2.Close)

data2["R"]=data2.Close.pct_change()
data2["r"]=np.log(data2.Close)-np.log(data2.Close.shift(1))

#%%  sample 1

tickerSymbol= co
tickerData= yf.Ticker(tickerSymbol)
#print(tickerData.info)
data3=tickerData.history(period='1d',start='2000-1-1',end='2008-1-1')

data3=pd.DataFrame(data3.Close)

data3["R"]=data3.Close.pct_change()
data3["r"]=np.log(data3.Close)-np.log(data3.Close.shift(1))

#%% plots

data1.Close.plot()
plt.show()

data2.Close.plot()
plt.show()

data3.Close.plot()
plt.show()


#%% check equal menas ttest
from scipy.stats import ttest_ind, ttest_ind_from_stats

#%% probar medias y varianzas"

a=data1.Close
b=data2.Close

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


#%% plot r

data1.r.plot()
plt.show()

data2.r.plot()
plt.show()

data3.r.plot()
plt.show()


#%% probar medias y var del stock son iguales

a=data1.r
b=data2.r

alpha=0.05

#Supuesto en donde las varianzas son iguales
t,p=ttest_ind(a,b)

if p<alpha:
    print('Se rechaza la Ho, las medias no son iguales(r)')
else:
    print('No se puede rechazar la Ho, *Las medias son iguales*(r)')

#Validar si las varianzas con Levene
w,p_w=stats_levene(a,b)

if p_w<alpha:
    print('Se rechaza la Ho, las medias no son iguales(r)')
else:
    print('No se puede rechazar la Ho, *Las medias son iguales*(r)')
