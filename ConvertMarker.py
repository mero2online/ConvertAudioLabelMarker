import os
import datetime


def readLocalFile(filename):
    f = open(filename, 'r')
    txt = f.read()
    f.close()

    return txt


def writeLocalFile(filename, txt):
    f = open(filename, 'w')
    f.write(txt)
    f.close()


def GetDataFromColumn(splitted):
    times = []
    numbers = []

    for v in splitted:
        for i, val in enumerate(v):
            if i == 1:
                times.append(val)
            if i == 5:
                numbers.append(val)
    return times, numbers


def getMilliSeconds(time):
    hours, minutes, seconds = (["0", "0"] + time.split(":"))[-3:]
    hours = int(hours)
    minutes = int(minutes)
    seconds = float(seconds)
    milliSeconds = round(float(3600 * hours + 60 * minutes + seconds), 6)
    return milliSeconds


filename = '002.csv'
txt = readLocalFile(filename)
pathOnly, file_extension = os.path.splitext(filename)

splitted = [i.split('\t') for i in txt.splitlines()]
times, numbers = GetDataFromColumn(splitted)

finalData = []

for idx, time in enumerate(times):
    if idx > 0:
        startTime = getMilliSeconds(time)

        name = numbers[idx]

        final = f'{startTime}\t{startTime}\t{name}'
        finalData.append(final)

writeLocalFile(f'{pathOnly}_out.txt', '\n'.join(finalData))
print(finalData)
