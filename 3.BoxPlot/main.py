import pandas as pd
import matplotlib.pyplot as plt

def display_prompt(data):
    i = -1
    for key in data.keys():
        i += 1
        if i==0:
            print('key','\t', 'Attribute')
            continue
        print(i,'\t', key)

def gui_plot(data):
    fig = plt.figure(figsize =(10, 7)) 
    # Creating plot 
    plt.boxplot(data) 
    # show plot 
    plt.show() 

def get_quartile(X):
    N = len(X)
    Q = None
    if N%2 == 0:
        Q = (X[N//2] + X[N//2-1]) / 2
    else:
        Q = X[N//2] / 2
    return Q

if __name__ == '__main__':
    data = pd.read_csv(open('dataset.csv'))
    display_prompt(data)

    key = 'Chhattisgarh'
    # key = input('choose a attribue :\t ')
    # print(data[key])
    
    x=list(data[key])
    X=sorted(x) 
    # print((x))

    N = len(x)
    Q1 = None
    Q2 = None
    Q3 = None
    MIN = None
    MAX = None

    ## for Q2
    Q2 = get_quartile(X)

    ## for Q1
    Q1 = get_quartile(X[:N//2])

    ## for Q3
    if N%2 == 0:
        Q3 = get_quartile(X[N//2:])
    else:
        Q3 = get_quartile(X[N//2+1:])


    IQR = Q3 - Q1
    MIN = Q1 - 1.5*IQR
    MAX = Q3 + 1.5*IQR    

    print('''
        N = {}
        IQR = {}
        
        MIN = {}
        Q1 = {}
        Q2 = {}
        Q3 = {}
        MAX = {}
    '''.format(N, IQR, MIN, Q1, Q2, Q3, MAX) )

    gui_plot(data[key])