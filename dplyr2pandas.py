# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:18:29 2018

@author: Thomas Brown
"""

#-----------------------------------------------------#
# Dplyr to Pandas
# Migrating fundamental data manipulation skills
# from R to Python
#
# Thomas Brown, 2018
#-----------------------------------------------------#

# Load a module

# R: library(dplyr)
import pandas as pd

# load the example dataset
data = pd.read_csv("filepath/survey.csv")


#------------------------------#
# Select
#------------------------------#

# Select Variables
new_data = data[["Age", "Gender", "Country"]]

# Drop Variables
new_data = data.drop(["state"], axis = 1)

# Starts/Ends with X
new_data = data.loc[:, data.columns.str.startswith("self")]
new_data = data.loc[:, data.columns.str.endswith("e")]

# Contains X
new_data = data.loc[:, data.columns.str.contains("health", regex = False)]

# Matches a regular expression
new_data = data.loc[:, data.columns.str.contains("^[A,G,s]")]


#------------------------------#
# Filter 
#------------------------------#

# Logical Filters
new_data = data[data['Age'] > 40]
new_data = data[data['state'] == 'CA']
new_data = data[data['state'] != 'CA']

# Multiple logical filters
new_data = data[(data['Age'] > 10) & (data['Age'] < 60)]

# Missing filters
new_data = data[data.state.notnull()]
new_data = data[data.state.isnull()]




#------------------------------#
# Arrange 
#------------------------------#

new_data = data.sort_values('state')
new_data = data.sort_values('state', ascending = False)

new_data = data.sort_values(['Age', 'state'], ascending = [False, True])



#------------------------------#
# Mutate
#------------------------------#

# Required to calculate various variables numerically
import numpy as np

new_data = data.copy()
new_data['indicator'] = 1

new_data['age2'] = np.array(data['Age'])*2




#------------------------------#
# Summarise
#------------------------------#

new_data = data['Age'].median()
new_data = data.Age.median()


new_data = data['Gender'].value_counts()
new_data = data.Gender.value_counts()

# For multiple columns
new_data = data[data.columns].mode()
new_data = data[['Country', 'state']].mode()



#------------------------------#
# Groupby / Summarise
#------------------------------#

new_data = data.groupby('Gender')['Age'].count()

new_data = data.groupby('Country')['Age'].mean()






