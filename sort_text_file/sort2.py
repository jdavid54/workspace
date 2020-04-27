import csv
import operator

print('sorted by last name, using key=lambda function')
with open("studentinfo.txt", "r") as f:
    reader = csv.reader(f)
    sorted_list = list(reader)  # turn the reader iterator into a list
    sorted_list.sort(key=lambda x: x[2])  # use the third column as a sorting key
    print("\n".join(str(row) for row in sorted_list))  # prettier print