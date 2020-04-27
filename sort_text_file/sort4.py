import csv
import operator

print('sorted by two keys, using key=lambda function')

with open("studentinfo.txt", "r") as f:
    reader = csv.reader(f)
    sorted_list = list(reader)  # turn the reader iterator into a list
    sorted_list.sort(key=lambda x: (x[3], x[4]))  # use fourth and fifth column
    print("\n".join(str(row) for row in sorted_list))  # prettier print