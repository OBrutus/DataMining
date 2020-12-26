For  a given data series 

A) Find 5 Number Summary and 

B) Draw Box Plot  for a data set

Week 3
## Aniket Vaishnav 
2017BTEIT00062

# Introduction
**Box Plot** is also known as **Whisker plot**. It provides a summary of 5 different quantities which are :

1. Minimum
1. Q1 
1. Median (also known as Q2)
1. Q3 
1. Maximum

IQR ( InterQuartile Range ) = Q3 - Q1

Upper = Q1 - 1.5 \* IQR

Lower = Q3 + 1.5 \* IQR

Box Plot are useful when

1. Handles Large Data Easily
1. Exact Values Not Retained
1. A clear summary
1. Displays outliers
# Code
Written in python can be found at [GitHub](https://github.com/OBrutus/DataMining/blob/master/3.BoxPlot/main.py)

import pandas as pd

import matplotlib.pyplot as plt

def display\_prompt(data):

`    `i = -1

`    `for key in data.keys():

`        `i += 1

`        `if i==0:

`            `print('key','\t', 'Attribute')

`            `continue

`        `print(i,'\t', key)

def gui\_plot(data):

`    `fig = plt.figure(figsize =(10, 7)) 

`    `# Creating plot 

`    `plt.boxplot(data) 

`    `# show plot 

`    `plt.show() 

def get\_quartile(X):

`    `N = len(X)

`    `Q = None

`    `if N%2 == 0:

`        `Q = (X[N//2] + X[N//2-1]) / 2

`    `else:

`        `Q = X[N//2] / 2

`    `return Q

if \_\_name\_\_ == '\_\_main\_\_':

`    `data = pd.read\_csv(open('dataset.csv'))

`    `display\_prompt(data)

`    `key = 'Chhattisgarh'

`    `# key = input('choose a attribue :\t ')

`    `# print(data[key])



`    `x=list(data[key])

`    `X=sorted(x) 

`    `# print((x))

`    `N = len(x)

`    `Q1 = None

`    `Q2 = None

`    `Q3 = None

`    `MIN = None

`    `MAX = None

`    `## for Q2

`    `Q2 = get\_quartile(X)

`    `## for Q1

`    `Q1 = get\_quartile(X[:N//2])

`    `## for Q3

`    `if N%2 == 0:

`        `Q3 = get\_quartile(X[N//2:])

`    `else:

`        `Q3 = get\_quartile(X[N//2+1:])


`    `IQR = Q3 - Q1

`    `MIN = Q1 - 1.5\*IQR

`    `MAX = Q3 + 1.5\*IQR    

`    `print('''

`        `N = {}

`        `IQR = {}



`        `MIN = {}

`        `Q1 = {}

`        `Q2 = {}

`        `Q3 = {}

`        `MAX = {}

`    `'''.format(N, IQR, MIN, Q1, Q2, Q3, MAX) )

`    `gui\_plot(data[key])
# Dependencies
Python 3+

Pandas

Matplotlib 

Run via python3 main.py
# Screenshots![](Image\_0)![](Image\_2)
# ![](Image\_1)
# References
[https](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[://](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[scikit](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[-](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[learn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[.](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[org](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[/](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[stable](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[/](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[modules](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[/](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[generated](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[/](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[.](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[linear](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[_](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[model](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[.](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[.](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)[html](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

[https](https://en.wikipedia.org/wiki/Box_plot)[://](https://en.wikipedia.org/wiki/Box_plot)[en](https://en.wikipedia.org/wiki/Box_plot)[.](https://en.wikipedia.org/wiki/Box_plot)[wikipedia](https://en.wikipedia.org/wiki/Box_plot)[.](https://en.wikipedia.org/wiki/Box_plot)[org](https://en.wikipedia.org/wiki/Box_plot)[/](https://en.wikipedia.org/wiki/Box_plot)[wiki](https://en.wikipedia.org/wiki/Box_plot)[/](https://en.wikipedia.org/wiki/Box_plot)[Box](https://en.wikipedia.org/wiki/Box_plot)[_](https://en.wikipedia.org/wiki/Box_plot)[plot](https://en.wikipedia.org/wiki/Box_plot)



