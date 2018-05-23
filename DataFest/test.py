import csv

with open('datafest2018-Updated-April12.csv', 'r') as csvIn:
    reader = csv.reader(csvIn, delimiter=',')
    job = ['','']
    for row in reader:
        if(row[2] == job[0]):
            if(row[5] != job[1]):
                print("MISMATCH")
                print(job)
                print('%s, %s' % (row[2], row[5]))
        else:
            job[0] = row[2]
            job[1] = row[5]
