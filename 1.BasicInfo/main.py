import csv
import glob
import pandas

def selectattribute(csv_file):
    print('Select an attribute you choose')
    for i in range(csv_file.keys().__len__()):
        print(i,' :  ',csv_file.keys()[i])
    attr = int(input())
    attr = csv_file.keys()[attr]
    print('attr is ', attr)
    return attr

if __name__ == '__main__':
    print('Choose one of the CSV from below :')
    dataset_dir = 'dataset'
    items = []
    items_size = 1
    for item in glob.glob(dataset_dir+'/*.csv'):
        print(str(items_size).ljust(4)+': '+item)
        items_size += 1
        items.append(item)

    csv_file = pandas.read_csv(items[int(input())-1])
    attr = selectattribute(csv_file)
    print(' main selected attr : ',attr)
    while True:
        print('''
            1: sum
            2: variance
            3: min
            4: max
            5: mode
            6: median
            7: mean
            8: count
            9: change attribute
            0: Exit
        choose an option : ''', end='')
        ch = int(input())
        if ch==0:
            break
        elif ch==1:
            print(csv_file[attr].sum())
        elif ch==2:
            print(csv_file[attr].var())
        elif ch == 3:
            print(csv_file[attr].min())
        elif ch==4:
            print(csv_file[attr].max())
        elif ch==5:
            print(csv_file[attr].mode())
        elif ch==6:
            print(csv_file[attr].median())
        elif ch==7:
            print(csv_file[attr].mean())
        elif ch==8:
            print(csv_file[attr].count())
        elif ch==9:
            attr = selectattribute(csv_file)
    print(''' *********** THANK YOU *********** ''')
