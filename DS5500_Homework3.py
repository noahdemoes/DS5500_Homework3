# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:51:39 2019

@author: noahd
"""

import pandas as pd
import numpy as np
fiscal_data=pd.read_csv('Sdf16_1a.txt',sep='\t',header=0,low_memory=False)
math_performance_data=pd.read_csv('math-achievement-lea-sy2015-16.csv',low_memory=False)
RLA_performance_data=pd.read_csv('rla-achievement-lea-sy2015-16.csv',low_memory=False)


##### Problem 1 ##################

## explore District level data
fiscal_data.describe()

### Rank and Visualize States by Total Federal Revenue 

state_fiscal_data=fiscal_data.groupby(['STABBR']).sum()
state_fedrevenue_data_ranked=state_fiscal_data[['TFEDREV']].sort_values('TFEDREV',ascending=False).reset_index()

import plotly.graph_objects as go

# Load data frame and tidy it.
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df['total exports'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Millions USD",
))

fig.update_layout(
    title_text = '2011 US Agriculture Exports by State',
    geo_scope='usa', # limite map scope to USA
)

fig.show()