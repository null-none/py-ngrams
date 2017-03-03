import csv


class Ngrams(object):

    def __init__(self):
        pass

    def result(self, number):
        result = []
        with open('ngrams{0}.csv'.format(number), 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                result.append(row[0].split(','))
        return result
