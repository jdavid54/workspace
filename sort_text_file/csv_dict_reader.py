import csv
with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print('reader.__next__', reader.__next__())
    print('next(reader)', next(reader))
    for row in reader:
        print(row['first_name'], row['last_name'])

#print some features about dictreader
print(reader.fieldnames)
print(reader.dialect)
print(reader.line_num)
