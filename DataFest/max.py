import csv

with open('costofliving.csv', 'r') as csvIn:
    reader = csv.reader(csvIn, delimiter=',')
    single = 0
    for row in reader:
        if(single == 0):
            macks = row
            macks[10] = 0
            single = 1
        elif(int(macks[10]) < int(row[10])):
            macks = row

    print(macks)
