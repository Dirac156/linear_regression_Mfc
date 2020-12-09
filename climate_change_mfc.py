#!/usr/bin/env python
# coding: utf-8

# In[31]:


#get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
plt.rcParams['figure.figsize'] = (20.0, 10.0)

#load data
data = pd.read_csv("climate_change.csv")
print(data.shape)
data.tail()


# In[26]:


#collecting data
X = data['CO2'].values
Y = data['Temp'].values


# In[27]:


#Mean of independante and dependate variables

mean_x = np.mean(X)
mean_y = np.mean(Y)

#Total number of values
n = len(X)

#calculate slope and constante variables
numer = 0
denom = 0

for i in range(n):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2

b1 = numer /denom
b0 = mean_y - (b1 * mean_x)

print(b1, b0)


# In[28]:


#value of x and y

y = b0 + b1 * X

#ploting the regression line
plt.plot(X, y, color = 'red', label= 'Regresion Line')

#scatter plot
plt.scatter(X, Y, c = 'black', label = 'Temperatures')

plt.xlabel('CO2')
plt.ylabel('Temperature')
plt.legend()
plt.show()


# In[30]:


#Rsquare
ss_t = 0
ss_r = 0
for i in range(n - 1):
    y_pred = b0 + b1 * X[i]
    ss_t += (Y[i] - mean_y) ** 2
    ss_r += (Y[i] - y_pred) ** 2
r2 = 1 - (ss_r/ss_t)
print(r2)


# In[32]:


#value of CO2 in 2020 october attended 411. Let view what will happend when the Co2 emmission will be 450

expected = 450 * b1 + b0
print(expected)


# In[ ]:
