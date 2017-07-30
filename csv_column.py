#!/usr/bin/python
import sys
import csv


if __name__ == "__main__":
    # csv module exposes a reader object that takes a file object to read
    csvfile = csv.reader(sys.stdin)

    # defaults to first column but accepts command line argument to specify column
    column_num = 0
    if len(sys.argv) > 1:
        column_num = int(sys.argv[1])

    # each row in csv file is a list
    for row in csvfile:
        print row[column_num]
