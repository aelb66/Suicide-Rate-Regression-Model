import pandas as pd #data manipulation
import numpy as np #data transformations

import matplotlib.pyplot as plt #visualisation
import seaborn as sns #visualisation

import sklearn # machine learning
from sklearn.model_selection import train_test_split #train and test split
from sklearn.linear_model import LinearRegression #Linear Regression
from sklearn.ensemble import RandomForestRegressor #Random Forest
from sklearn.tree import DecisionTreeRegressor #Decision Tree
from sklearn.metrics import mean_squared_error, r2_score #performance metrics
from sklearn.model_selection import GridSearchCV #cross-validation

import statsmodels.api as sm #one-way ANOVA
from statsmodels.formula.api import ols  #importing stats package
import scipy.stats as stats #statistics
from sklearn.preprocessing import MinMaxScaler #normalisations
from sklearn.preprocessing import StandardScaler #normalisations
