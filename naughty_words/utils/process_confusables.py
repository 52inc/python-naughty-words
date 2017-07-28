import csv

confusables = {}
with open('confusables.txt') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    for row in reader:
        try:
            row[0] and row[1]
        except IndexError:
            continue
        try:
            confusables[row[1].strip(' \t\n\r')].append(row[0].strip(' \t\n\r'))
        except KeyError:
            confusables[row[1].strip(' \t\n\r')] = [row[0].strip(' \t\n\r')]

print(confusables)
