#TrueFalse
import pprint
import matplotlib
import weather_parser

from matplotlib import pyplot
from weather_parser import parse_location_data

filename = "datafiles-week-4-group-a/0.80N-103.66E-TAVG-Trend.txt"
data = parse_location_data(filename)

def main():
    ''' call plotting functions'''
    pt = plot_timeseries(filename)
    pc = plot_scatter(filename)
    return;

def plot_timeseries(filename):
    '''plot year vs temperature anomaly'''
    x_val = [x[0] for x in data]
    month_val = [x[1] for x in data]
    year_val = [x[0] + ((x[1]*(1./12.))-(1./12)) for x in data]
    temp_val = [x[2] for x in data]
    unc_val = [x[3] for x in data]
    uncertainty = []
    for i, line in enumerate(data):
        t1 = data[i][2]
        u1 = data[i][3]
        max_anomaly = t1+u1
        min_anomaly = t1-u1
        unc1 = (min_anomaly, max_anomaly)
        uncertainty.append(unc1)
    unc_min = [x[0] for x in uncertainty]
    unc_max = [x[1] for x in uncertainty]
    pyplot.plot(year_val, unc_min, '0.5', label='Uncertainty')
    pyplot.plot(year_val, unc_max, '0.5')
    pyplot.plot(year_val, temp_val, 'k-', label='Anomaly')
    pyplot.legend()
    pyplot.title('Timeseries')
    pyplot.xlabel('Year')
    pyplot.ylabel('Temperature Anomaly [Celsius]')
    return pyplot.show()


def plot_scatter(filename):
    '''plot year vs uncertainty'''
    x_val = [x[0] for x in data]
    month_val = [x[1] for x in data]
    year_val = [x[0] + ((x[1]*(1./12.))-(1./12)) for x in data]
    unc_val = [x[3] for x in data]
    pyplot.scatter(year_val, unc_val, color='k', marker='+', label='uncertainty')
    pyplot.legend()
    pyplot.title('Scatter')
    pyplot.xlabel('Year')
    pyplot.ylabel('Uncertainty [Celsius]')
    return pyplot.show()

main()
