import csv
import operator

print('sorted using defined function')

def get_third_column(x):
    return x[2]

with open("studentinfo.txt", "r") as f:
    reader = csv.reader(f)
    sorted_list = list(reader)  # turn the reader iterator into a list
    sorted_list.sort(key=get_third_column)  # use the third column as a sorting key
    print("\n".join(str(row) for row in sorted_list))  # prettier print