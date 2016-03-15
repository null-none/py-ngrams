import csv

for index in range(1, 6):
    with open('ngrams{0}.csv'.format(index), 'rb') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
      for row in spamreader:
        print row[0].split(',')[0]
