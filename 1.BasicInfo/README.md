General Information Regarding Data.

Week 1
## Aniket Vaishnav 
2017BTEIT00062


# Introduction
A data set (or dataset) is a collection of data. In the case of tabular data, a data set corresponds to one or more database tables, where every column of a table represents a particular variable, and each row corresponds to a given record of the data set in question. The data set lists values for each of the variables, such as height and weight of an object, for each member of the data set. Each value is known as a datum. Data sets can also consist of a collection of documents or files. 


We perform various operations upon this group of data 

Such as:

`            `1: sum

`            `2: variance

`            `3: min

`            `4: max

`            `5: mode

`            `6: median

`            `7: mean

`            `8: count

`            `9: change attribute

Data Set chosen here is [nifty](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[50-](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[stock](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[-](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[market](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[-](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[data](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)
## Terminologies
### Sum
The Arithmetic addition of an attribute in a dataset is called sum of an attribute.

sum = ![](Image\_0)
### Variance
`	`It means the spread between the data sets itself. Denoted by symbol ![](Image\_1).

`	`![](Image\_2)
### Min / Max
`	`The Minimum / Maximum in attribute 
### Mode
`	`The most frequently appearing data value in data set is known as Mode.
### Median
`	`Within a sorted data the mid point of separation which can divide data set in two halves is known as median.

# Code
Written in python can be found at [GitHub](https://github.com/OBrutus/DataMining/blob/master/1.BasicInfo/main.py)

import csv

import glob

import pandas

def selectattribute(csv\_file):

`    `print('Select an attribute you choose')

`    `for i in range(csv\_file.keys().\_\_len\_\_()):

`        `print(i,' :  ',csv\_file.keys()[i])

`    `attr = int(input())

`    `attr = csv\_file.keys()[attr]

`    `print('attr is ', attr)

`    `return attr

if \_\_name\_\_ == '\_\_main\_\_':

`    `print('Choose one of the CSV from below :')

`    `dataset\_dir = 'dataset'

`    `items = []

`    `items\_size = 1

`    `for item in glob.glob(dataset\_dir+'/\*.csv'):

`        `print(str(items\_size).ljust(4)+': '+item)

`        `items\_size += 1

`        `items.append(item)

`    `csv\_file = pandas.read\_csv(items[int(input())-1])

`    `attr = selectattribute(csv\_file)

`    `print(' main selected attr : ',attr)

`    `while True:

`        `print('''

`            `1: sum

`            `2: variance

`            `3: min

`            `4: max

`            `5: mode

`            `6: median

`            `7: mean

`            `8: count

`            `9: change attribute

`            `0: Exit

`        `choose an option : ''', end='')

`        `ch = int(input())

`        `if ch==0:

`            `break

`        `elif ch==1:

`            `print(csv\_file[attr].sum())

`        `elif ch==2:

`            `print(csv\_file[attr].var())

`        `elif ch == 3:

`            `print(csv\_file[attr].min())

`        `elif ch==4:

`            `print(csv\_file[attr].max())

`        `elif ch==5:

`            `print(csv\_file[attr].mode())

`        `elif ch==6:

`            `print(csv\_file[attr].median())

`        `elif ch==7:

`            `print(csv\_file[attr].mean())

`        `elif ch==8:

`            `print(csv\_file[attr].count())

`        `elif ch==9:

`            `attr = selectattribute(csv\_file)

`    `print(''' \*\*\*\*\*\*\*\*\*\*\* THANK YOU \*\*\*\*\*\*\*\*\*\*\* ''')

# Dependencies
Python 3+

Pandas

Run via python3 main.py
# References
[https](https://en.wikipedia.org/wiki/Data_set)[://](https://en.wikipedia.org/wiki/Data_set)[en](https://en.wikipedia.org/wiki/Data_set)[.](https://en.wikipedia.org/wiki/Data_set)[wikipedia](https://en.wikipedia.org/wiki/Data_set)[.](https://en.wikipedia.org/wiki/Data_set)[org](https://en.wikipedia.org/wiki/Data_set)[/](https://en.wikipedia.org/wiki/Data_set)[wiki](https://en.wikipedia.org/wiki/Data_set)[/](https://en.wikipedia.org/wiki/Data_set)[Data](https://en.wikipedia.org/wiki/Data_set)[_](https://en.wikipedia.org/wiki/Data_set)[set](https://en.wikipedia.org/wiki/Data_set)

[https](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[://](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[www](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[.](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[kaggle](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[.](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[com](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[/](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[rohanrao](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[/](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[nifty](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[50-](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[stock](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[-](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[market](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[-](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)[data](https://www.kaggle.com/rohanrao/nifty50-stock-market-data)


