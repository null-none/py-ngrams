import csv


class Ngrams(object):

    def __init__(self, number):
        self.number = number

    def result():
        result = []
        with open('ngrams{0}.csv'.format(self.number), 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                result.append(row[0].split(','))
        return result
