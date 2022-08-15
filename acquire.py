#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import opendatasets as od
import os

def acquire_admissions():
    """ Acquire Graduate-Admissions-Predictions Data for """
    
    if os.path.exists('admission_data.csv'):
        admin = pd.read_csv('admission_data.csv')
        return admin
    
    else:
        od.download("https://www.kaggle.com/datasets/mukeshmanral/graduates-admission-prediction")
        admin = pd.read_csv('./graduates-admission-prediction/admission_data.csv')
        admin.to_csv('admission_data.csv', index=False)
        
        return admin

def summary_info(df): 
    # Summarize data (shape, info, summary stats, dtypes, shape)
    print('--- Shape: {}'.format(df.shape))
    print('--- Descriptions')
    print(df.describe(include='all'))
    print('--- Info')
    return df.info()