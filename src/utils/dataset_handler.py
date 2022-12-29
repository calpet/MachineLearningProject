import csv

def get_dataset(filename):
    file = open(filename, 'r')
    dataset = []
    rows = csv.reader(file)
    for row in rows:
        dataset.extend(row)
    file.close()
    return dataset