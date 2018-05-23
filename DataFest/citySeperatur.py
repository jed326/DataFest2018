import csv

with open('cityIndexSep.csv', 'w') as csvOut:
    writer = csv.writer(csvOut, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['City'] + ['Type'] + ['Index'])
    with open('cityIndex.csv', 'r') as csvIn:
        reader = csv.reader(csvIn, delimiter=',')
        for row in reader:
            if(row[0] != 'City'):
                city, state = row[0].split(",")
                city = city.split("-")
                state = state.split("-")
                if(len(city) == 1):
                    if(len(state) == 1):
                        writer.writerow([row[0]] + [row[1]] + [row[2]])
                    else:
                        for s in state:
                            writer.writerow(['%s, %s' % (city[0].strip(), s.strip())] + [row[1]] + [row[2]])
                else:
                    if(len(state) == 1):
                        for c in city:
                            writer.writerow(['%s, %s' % (c, state[0].strip())] + [row[1]] + [row[2]])
                    else:
                        for c in city:
                            for s in state:
                                writer.writerow(['%s, %s' % (c, s.strip())] + [row[1]] + [row[2]])
