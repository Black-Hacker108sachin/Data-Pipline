import csv

# Open the CSV file
with open('sample.csv', mode='r', newline='') as file:
    csv_reader = csv.reader(file)

    # Read and print each row in the CSV file
    for row in csv_reader:
        print(row)
