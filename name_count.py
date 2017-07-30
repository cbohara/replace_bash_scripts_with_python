#!/usr/bin/python
import sys

# alternative to $ cat names.log | sort | uniq | wc -l
# we want the name of the users and the number of occurances
# $ cat data/names.log | python name_count.py

# we can then sort so most frequent users are printed first
# sort -rn (-r for reverse and -n for numeric)
# $ cat data/names.log | python name_count.py | sort -rn 


if __name__ == "__main__":
    # names = { name : count } 
    names = {}

    # sys.stdin is a file object
    for name in sys.stdin.readlines():
        # each line will have a newline on the end that should be removed
        name = name.strip()

        if name in names:
            names[name] += 1
        else:
            names[name] = 1

    # print the number of times the name appeared
    for name, count in names.iteritems():
        sys.stdout.write("%d\t%s\n" % (count, name))

