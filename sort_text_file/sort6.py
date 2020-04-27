import csv
import operator

print('read, sort on first column and save to file with writerows()')
with open("input.csv") as fh:
    reader = csv.reader(fh)
    rows = sorted(reader, key=operator.itemgetter(0), reverse=True)

for n, row in enumerate(rows):
    print('row',n,row)

#write to file
print('\nall rows',rows)
with open("output.csv", "w") as fh:
    csv.writer(fh).writerows(rows)