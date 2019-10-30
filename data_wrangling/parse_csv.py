import os
import csv

DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        
        i = 0
        
        for line in f:
            dictionary = {}
            if i == 0:
                heading = line.split(',')
            elif i<=10:
                values = line.split(',')
                
                for index, item in enumerate(values):
                    dictionary[heading[index].strip()] = item.strip()
                data.append(dictionary)
            else:
                break
            i = i + 1

    return data

def parse_file_with_csv(datafile):
    data = []
    with open(datafile) as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

    d2 = parse_file_with_csv(datafile)
    assert d2[0] == firstline
    assert d2[9] == tenthline

    
test()
