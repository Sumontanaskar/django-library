#!/usr/bin/python
import os
import csv
destpath = './media/'
elements = []
def data_sort(data):
    #Data Process
    print 'Starting Data Process'
    data = data.split('|')

    print data
    date_rx = data[0].strip().replace("/", "-")
    date = date_rx[0:8]

    rx = date_rx[8:].strip()
    tx = data[1].strip()
    tot = data[2].strip()
    print date, rx, tx, tot
    return date, rx, tx, tot


f = open('/tmp/data_east.txt', 'r')
for row in f:
    elements.append(row)
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

for row in elements:
    if row[0:8] == 'vpc-prod':
        host = row[0:-1]
        print host
        list1.append(host)
    else:
        date, rx, tx, tot = data_sort(row)
	print date,rx,tx,tot
        list2.append(date)
        list3.append(rx)
        list4.append(tx)
        list5.append(tot)
end = len(list2)

print 'File name:', list2[0]
fName = 'Data_in_out_'+list2[0]+'.csv'
# create CSV file
try:
    os.remove(fName)  # Remove old file to clear file
except Exception as e:
    print 'Warning:', e
fName_path= destpath+fName
f = open(fName_path, 'wb+')
fieldnames = ['DATE', 'Server Name', 'Data IN', 'Data OUT',	'Total']
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()

for i in range(end):
    print list1[i], list2[i], list3[i], list4[i], list5[i]
    #print list1[i]
    writer.writerow({'DATE': list2[i], 'Server Name': list1[i], 'Data IN': list3[i], 'Data OUT': list4[i], 'Total':list5[i]})
f.close()




