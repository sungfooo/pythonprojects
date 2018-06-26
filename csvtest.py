import csv
import matplotlib.pyplot as plt
import datetime

def numberfier(new_number):
    return int(new_number.strip("$"))

def date_format(new_date):
    return datetime.datetime.strptime(new_date,"%m/%d/%y")

col1 = []
col2 = []

with open('revenue.csv') as csvfile:

    csvdata = csv.reader(csvfile,delimiter=',')

    #loop
    rows = 0
    for row in csvdata:
        if rows == 0:
            rows = rows + 1
            continue
        col1.append(numberfier(row[0]))

        col2.append(date_format(row[1]))

print col1
print col2

fig, ax = plt.subplots()

ax.plot(col2, col1)

plt.show()
