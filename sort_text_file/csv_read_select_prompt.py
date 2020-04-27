import csv

with open("studentinfo.txt") as fh:
    reader = csv.reader(fh)
    student_id = input("Enter Id:")
    for row in reader:
        if row[0] == student_id:
            print(row[1] + " " + row[2])