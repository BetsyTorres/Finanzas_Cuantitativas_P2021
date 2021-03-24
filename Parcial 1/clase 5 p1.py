# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 21:25:50 2021

@author: RAYMUNDO
"""

import numpu as np
import pandas as pd


'''
FORMULA DE CAPM 
donde r es el retorno
r=alpha + beta(m-rf)+rf
E(r)= CLASE MUNUTO 78

asumimos que alpha~N(7%,5%)
asumimos que le mercado~N(15%,20%)

beta=0.8
rf=3%
R^2~-0.00
'''
#%%

n=100
beta=0.8
rf=0.03

alpha=pd.DataFrame(np.randonm.normal(loc=0.07, scale=np.sqrt(0.2), size=n))
alpha.columns=['Alpha']

m=pd.DataFrame(np.zeros())