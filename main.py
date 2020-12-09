#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

def get_rsquare(x, y):
    model = LinearRegression()
    model = LinearRegression().fit(x, y)
    r_sq = model.score(x, y)
    print('coefficient of determination:', r_sq)

#load the data tem vs Co2
data = pd.read_csv("climate_change.csv")
#print(data)

x_co2 = data['CO2']
x_co2 = np.array(x_co2).reshape((-1, 1))
y_tmp = data['Temp']

x_ch4 = data['CH4']
x_ch4 = np.array(x_ch4).reshape((-1, 1))

x_n20 = data['N2O']
x_n20 = np.array(x_n20).reshape((-1, 1))

x_cfc = data['CFC-11']
x_cfc = np.array(x_cfc).reshape((-1, 1))

x_cfc2 = data['CFC-12']
x_cfc2 = np.array(x_cfc2).reshape((-1, 1))

x_tsi = data['TSI']
x_tsi = np.array(x_tsi).reshape((-1, 1))

x_Ae = data['Aerosols']
x_Ae = np.array(x_Ae).reshape((-1, 1))

x_mei = data['MEI']
x_mei = np.array(x_mei).reshape((-1, 1))

get_rsquare(x_co2, y_tmp)
get_rsquare(x_ch4, y_tmp)
get_rsquare(x_n20, y_tmp)
get_rsquare(x_cfc, y_tmp)
get_rsquare(x_cfc2, y_tmp)
get_rsquare(x_tsi, y_tmp)
get_rsquare(x_Ae, y_tmp)
get_rsquare(x_mei, y_tmp)
# model = LinearRegression()
#
# model = LinearRegression().fit(x, y)
#
# #print(model)
#
# r_sq = model.score(x, y)
# print('coefficient of determination:', r_sq)
