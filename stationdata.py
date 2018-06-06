#TrueFalse
'''
Small program to read single weather station data from Berkeley Earth's data set.
'''

def read_file(filename):
    '''
    Read a single data file given by filename.
    '''
    data = []
    fo = open(filename, "r")
    for line in fo:
        if line.startswith('%'):
            continue
        line = line.strip()
        if len(line) == 0:
            continue
        columns = line.split()
        year = int(columns[0])
        month = int(columns[1])
        temp = float(columns[2])
        anomaly = float(columns[3])
        t = (year, month, temp, anomaly,)
        data.append(t)
    return data

if __name__ == '__main__':
    filenames = [
        '18497-TAVG-Data.txt',
        '24859-TAVG-Data.txt',
        '156164-TAVG-Data.txt',
        '167589-TAVG-Data.txt',
    ]

    for filename in filenames:
        data = read_file(filename)
        print 'File %s contains %d data entries' % (filename, len(data))
