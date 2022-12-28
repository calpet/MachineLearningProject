import csv
import random

def get_dataset(filename):
    # List of bad words to censor
    file = open(filename, 'r')
    dataset = []
    rows = csv.reader(file)
    for row in rows:
        dataset.extend(row)
    file.close()
    return dataset

def generate_labels(number):
    values = [random.randint(0, 1) for _ in range(number)]

    # Open the CSV file in write mode
    with open('ones.csv', 'w', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)
        
         # Write the list of 1s and 0s to the CSV file
        writer.writerows([[number] for number in values])

generate_labels(1617)