#TrueFalse
import pprint
import matplotlib
import os

from matplotlib import pyplot

path = 'datafiles-week-4-group-a'

def parse_location_data(filename):
    ''' Reads file, returns year, month, anomaly and uncertainty'''
    fo = open(filename, "r")
    data = []
    for line in fo:
        if line.startswith('%'):
            continue
        line = line.strip()
        if len(line) == 0:
            continue
        columns = line.split()
        year = int(columns[0])
        month = int(columns[1])
        monthanomaly = float(columns[2])
        monthanomalyunc = float(columns[3])
        t = (year, month, monthanomaly, monthanomalyunc,)
        data.append(t)
    return data
    fo.close()

def plot_histogram(path):
    '''Plot histogram of the temperature anomalies in all locations in Jan 2000'''
    anomaly = []
    for fn in os.listdir(path):
        fullpath = os.path.join(path, fn)
        data = parse_location_data(fullpath)
        for i, line in enumerate(data):
            year = data[i][0]
            month = data[i][1]
            temp = data[i][2]
            if year == 2000 and month == 1:
                t_val = (temp,)
                anomaly.append(t_val)
    temp_anomaly = [x[0] for x in anomaly]
    pyplot.hist(temp_anomaly, 20, histtype='step', color='k', label='jan 2000')
    pyplot.legend()
    pyplot.xlabel('Temperature Anomaly')
    pyplot.ylabel('Amount')
    pyplot.title('Temperature Anomaly in all 95 locations')
    pyplot.show()
    return;

if __name__ =='__main__':
    pprint.pprint(parse_location_data("datafiles-week-4-group-a/0.80N-103.66E-TAVG-Trend.txt"))
