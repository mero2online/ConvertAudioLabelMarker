import os
import datetime

from HelperFunc import readLocalFile, writeLocalFile


def GetDataFromColumn(splitted):
    times = []
    numbers = []

    for v in splitted:
        for i, val in enumerate(v):
            if i == 1:
                times.append(val)
            if i == 2:
                numbers.append(val)
    return times, numbers


def getHrMinSec(time):
    return str(datetime.timedelta(seconds=time))


def ConvertLabel(filename):
    txt = readLocalFile(filename)
    pathOnly, file_extension = os.path.splitext(filename)

    splitted = [i.split('\t') for i in txt.splitlines()]
    times, numbers = GetDataFromColumn(splitted)

    finalData = []
    topRow = ['Name', 'Start', 'Duration',
              'Time Format', 'Type', 'Description']
    finalData.append('\t'.join(topRow))

    for idx, time in enumerate(times):
        name = f'{pathOnly} {numbers[idx]}'

        timeFloated = float(time)
        startTime = getHrMinSec(timeFloated)

        diff = float(times[idx+1])-timeFloated if idx < len(times)-1 else 0
        Duration = getHrMinSec(diff)

        final = f'{name}\t{startTime}\t{Duration}\tdecimal\tCue\t{numbers[idx]}'
        finalData.append(final)

    writeLocalFile(f'{pathOnly}_out.csv', '\n'.join(finalData))
    print(finalData)
