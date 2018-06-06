#TrueFalse
import pprint

#OPEN A FILE
fo = open("data.txt", "r")

#READ FILE
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


# CALCULATING ANUAL AVERAGES

data2 = []
for year0 in range(1750,2015):
    sum = 0
    sum1= 0
    counter = 0
    counter1 = 0
    for i, line in enumerate(data):
        year1 = data[i][0]
        if year1 == year0:
            nan = float('nan')
            anomaly = data[i][2]
            anomalyunc = data[i][3]
            if  anomaly == anomaly:
                sum = anomaly + sum
                counter = counter + 1
            if anomalyunc == anomalyunc:
                sum1 = sum1 + anomalyunc
                counter1 = counter1 + 1
        elif year1 != year0:
            pass
    average = sum / counter
    if counter1 == 0:
        averageunc = 0
    elif counter1 != 0:
        averageunc = sum1 / counter1
    ave = (year0, average, averageunc,)
    data2.append(ave)


# WRITING DATA TO FILE

fw =  open('newdata.text', 'wb')
fw.write("Year Anomaly Uncertainty\n")
fw.write(" \n")
for t in data2:
    line = ' '.join(str(x) for x in t)
    fw.write(line + '\n')
fw.close()
