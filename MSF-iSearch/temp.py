# read csv

import csv
import os

with open('your_table.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';',
                            lineterminator='\n',
                            quotechar='|',
                            quoting=csv.QUOTE_MINIMAL)
    line_count = 0
    for row in csv_reader:
        print(row)
