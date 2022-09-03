# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 11:14:04 2022


@author: USER
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
#from sklearn.processing import StandardScaler
from scipy import stats
import warnings

#'' % \
datos_exel = pd.read_csv('train.csv')

def psitos():
    

    #.head(20)  para mostrarnos los primeros 20 filas
    print(datos_exel.head(20))

    # .shape    Para mostrarnos cuantas filas y comumnas son
    print(datos_exel.shape)
    
    #           Para mostrar las primeras y ultimas 5 filas de una columna 
    print(datos_exel['SalePrice'])

    #           Para ver dos columas 
    print(datos_exel[['Id','SalePrice']])

    # .mean()   Para ver el promedio de uuna columna
    print(datos_exel['SalePrice'].mean())

    # .describe()  Para que se cree un resumen de todo
    # .min() y  .max() valor minimo y valor maximo
    # .count() Para contar cuantas filas hay
    print(datos_exel.describe())

def grafica():
    #Grafica de SalePrice
    print(datos_exel['SalePrice'].describe())
    print(sns.distplot(datos_exel['SalePrice']))
    # Skew "Skewness" y Kurt "Kurtosis"
    print(datos_exel['SalePrice'].skew())
    print(datos_exel['SalePrice'].kurt())

def grafica2():
    var = 'GrLivArea'
    var2 = datos_exel['SalePrice']
    var3 = datos_exel['GrLivArea']
    varo = pd.concat([datos_exel[var],datos_exel['SalePrice']], axis=1)
    print(varo.head(20))
    #print(sns.distplot(varo))
    plt.scatter(var3, var2, color='red')
    
    
    #print(varo.plot.scatter(x=var, y=var2, ylim=(0,1000000)))
    #plt.plot(x = var, y = var2, ylim=(0,800000))
def grafica3():
    var = 'TotalBsmtSF'
    var1 = datos_exel[var]
    var2 = datos_exel['SalePrice']
    varo = pd.concat([datos_exel['SalePrice'], datos_exel[var]], axis=1)
    print(varo.head(20))
    plt.scatter(var1, var2, color='blue')
    
def dh():
    x=[1,2,3,4,5]
    y = [2.3, 3.4, 1.2, 6.6, 7.0]
    plt.scatter(x, y, color='red')
    plt.show()

#Relaciones Categoricas
#grafica de caja y bigote o BoxPlos
def cajaBigote():
    var= datos_exel['OverallQual']
    var1 = datos_exel['SalePrice']
    varo = pd.concat([var,var1], axis=1)
    print(varo.head(20))
    #
    f, ax = plt.subplots(figsize=(8,6))     #Primero se crea el tamaño adecuado
    fig = sns.boxplot(x = var, y = var1)    #Se crea la grafica con los datos adquiridos
    fig.axis(ymin=0, ymax=800000)           #Se personaliza el eje Y
    
    car = datos_exel['YearBuilt']
    varo2 = pd.concat([car, var1], axis=1)
    print(varo2.head(20))
    #
    f, ax = plt.subplots(figsize=(20,8))
    fig = sns.boxplot(x=car, y=var1 )
    fig.axis(ymin=0, ymax=800000)
    plt.xticks(rotation=90)
    
# Matrix de cooorexion
def correlacion():
    corre = datos_exel.corr()
    print(corre)
    f,ax = plt.subplots(figsize=(12,9))
    sns.heatmap(corre, vmax=.8, square=True)
def matrixRela():
    k = 10
    corre = datos_exel.corr()
    cols = corre.nlargest(k, "SalePrice")['SalePrice'].index
    print(cols)
    cm = np.corrcoef(datos_exel[cols].values.T)
    print(cm)
    sns.set(font_scale=1.25)
    hm = sns.heatmap(cm, cbar=True,annot = True, square = True, fmt = ".2f", annot_kws={"size":10,}, yticklabels=cols.values, xticklabels = cols.values)
    plt.show()
def ScaterPlot():
    sns.set()
    k = 10
    corre = datos_exel.corr()   
    cols = ['SalePrice','OverallQual','GrLivArea','TotalBsmtSF','1stFlrSF','FullBath','TotRmsAbvGrd','YearBuilt']
    sns.pairplot(datos_exel[cols], height=2.5)
    plt.show()

correlacion()


























