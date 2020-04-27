import csv
import operator

def stop(msg='continue'):
    r = input(msg)
# print some features about csvreader 
print('dialects',csv.list_dialects())
print('field size limit',csv.field_size_limit())

ifile =open('studentinfo.txt', 'r')
infile = csv.reader(ifile)
#print(infile.fieldnames)
#stop()
# Note that if you have a header, this is the header line
infields = infile.__next__()
print('infields',infields)

sortby = 'Id'  #Id, first_name, last_name, test1, test2 or test3
startindex = infields.index(sortby)  #find key in header line
print(startindex)
# Here you are creating the sorted list
sortedlist = sorted(infile, key=operator.itemgetter(startindex), reverse=True)
ifile.close
print(sortedlist)

# open the output file - it can be the same as the input file
outfile = open('myoutput.csv', 'w')
ofile = csv.writer(outfile)
ofile.writerow(infields)
# using writerow(), write one row at a time (see writerows in sort6.py)
for row in sortedlist:
    print(row)
    ofile.writerow(row)
outfile.close()