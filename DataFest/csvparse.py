import csv

with open('cityIndexStates.csv', 'w') as csvOut:
    writer = csv.writer(csvOut, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['City'] + ['Type'] + ['Index'])
    with open('ODN_Cost_of_Living.csv', 'r') as csvIn:
        reader = csv.reader(csvIn, delimiter=',')
        for row in reader:
                if(row[3] == '2015' and row[2] == 'state' and row[4] == 'all' and row[5] == 'index'):
                    #temp = row[1][:-11]
                    writer.writerow([row[1]] + [row[2]] + [row[6]])
    
