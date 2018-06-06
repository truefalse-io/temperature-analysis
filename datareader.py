#TrueFalse
import pprint

# open a file
fo = open("data.txt", "r")

#read file
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
fo.close()


# determining absolute temperature
f = open("data.txt", "r")

data2 = []
for line in f:
    line = line.strip()
    data2.append(line)

# numbering lines
for i, line in enumerate(data2):
         if i == 23:
              line = line.strip()
              columns2 = line.split()
              jan = float(columns2[1])
              feb = float(columns2[2])
              mar = float(columns2[3])
              apr = float(columns2[4])
              may = float(columns2[5])
              jun = float(columns2[6])
              jul = float(columns2[7])
              aug = float(columns2[8])
              sep = float(columns2[9])
              okt = float(columns2[10])
              nov = float(columns2[11])
              dec = float(columns2[12])
              temp = (jan, feb, mar, apr, may, jun, jul, aug, sep, okt, nov, dec,)
              data2.append(temp)
f.close()


# adding average absolute temperature and anomaly

data3 = []
for i, line in enumerate(data):
    year1 = data[i][0]
    month1 = data[i][1]
    temp1 = data[i][2]
    if month1 == 1:
        temp1 = temp1+jan
        abstemp = (year1, month1, temp1,)
        data3.append(abstemp)
    elif month1 == 2:
        temp1 = temp1+feb
        abstemp = (year1, month1, temp1,)
        data3.append(abstemp)
    elif month1 == 3:
        temp1 = temp1+mar
        abstemp = (year1, month1, temp1,)
        data3.append(abstemp)
    elif month1 == 4:
        temp1 = temp1+apr
        abstemp = (year1, month1, temp1,)
        data3.append(abstemp)
    elif month1 == 5:
        temp1 = temp1+may
        abstemp = (year1, month1, temp1,)
        data3.append(abstemp)
    elif month1 == 6:
        temp1 = temp1+jun
        abstemp = (year1, month1, temp1,)
        data3.append(abstemp)
    elif month1 == 7:
        temp1 = temp1+jul
        abstemp = (year1, month1, temp1,)
        data3.append(abstemp)
    elif month1 == 8:
        temp1 = temp1+aug
        abstemp = (year1, month1, temp1,)
        data3.append(abstemp)
    elif month1 == 9:
        temp1 = temp1+sep
        abstemp = (year1, month1, temp1,)
        data3.append(abstemp)
    elif month1 == 10:
        temp1 = temp1+okt
        abstemp = (year1, month1, temp1,)
        data3.append(abstemp)
    elif month1 == 11:
        temp1 = temp1+nov
        abstemp = (year1, month1, temp1,)
        data3.append(abstemp)
    elif month1 == 12:
        temp1 = temp1+dec
        abstemp = (year1, month1, temp1,)
        data3.append(abstemp)

# determining  max value of anomaly

maximum = 0
for i, line in enumerate(data):
    year2 = data[i][0]
    month2 = data[i][1]
    anomaly = data[i][2]
    if anomaly > maximum:
         maximum = anomaly
         imax = i
         yearmax = year2
         monthmax = month2


# determining min value of anomaly

minimum = 0
for i, line in enumerate(data):
    year3 = data[i][0]
    month3 = data[i][1]
    anomaly = data[i][2]
    if anomaly < minimum:
         minimum = anomaly
         imin = i
         yearmin = year3
         monthmin = month3
