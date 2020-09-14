import csv
import glob

if __name__ == '__main__':
    print('Choose one of the CSV from below :')
    dataset_dir = 'dataset'
    items = []
    items_size = 1
    for item in glob.glob(dataset_dir+'/*.csv'):
        print(str(items_size).ljust(4)+': '+item)
        items_size += 1
        items.append(item)

    csv_file = open(items[int(input())])   # Check requied
    reader = csv.reader(csv_file, delimiter=' ', quotechar='|')
    