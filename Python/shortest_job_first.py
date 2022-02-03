def sjf(dict):
    begHold, endHold = 0, 0
    sjfdict, tempdict, sortdict, pLine = {}, {}, {}, []
    for key, value in dict.items():
        at, bt = value[0], value[1]
        if (begHold == 0):
            endHold += bt
            sjfdict[key] = [begHold - at, bt - at]
            pLine.append([key, endHold])
            begHold = bt
        else:
            tempdict[key] = value[0], value[1]
    for key, value in sorted(tempdict.items(), key=lambda x: x[1][1]):
        sortdict[key] = value[0], value[1]
    for key, value in sortdict.items():
        at, bt = value[0], value[1]
        if begHold - at > 0:
            endHold += bt
            sjfdict[key] = [begHold - at, endHold - at]
            pLine.append([key, endHold])
            begHold += bt
        else:
            endHold += bt
            sjfdict[key] = [0, bt]
            pLine.append([key, endHold + 1])
            begHold += bt
    return sjfdict, pLine


def printData(gData, cData, pLine, Name):
    avgWT, avgTT = 0, 0
    plinestr = "0 -> "
    print(Name.upper())
    print('| Process | ArrivalTime | BurstTime | Waiting Time | TurnAround Time |')
    for key, value in sorted(cData.items()):
        print('{:>6}{:>11}{:>14}{:>16}{:>17}'.format(key, gData[key][0], gData[key][1], value[0], value[1]))
        avgWT += value[0]
        avgTT += value[1]
    print('Average Wait Time = {}    Average Turnaround Time = {}\n'.format(avgWT / len(cData), avgTT / len(cData)))
    for x in pLine:
        plinestr += ('{} -> {} -> '.format(x[0], x[1]))
    print('{}\n'.format(plinestr[:-3]))


gData = {'P1': [0, 10], 'P2': [1, 2], 'P3': [4, 4], 'P4': [5, 1], 'P5': [10, 3], 'P6': [21, 12]}
gQuant = 4
gContSwitch = 0.4

sjfScheduling, sjfLine = sjf(gData)
printData(gData, sjfScheduling, sjfLine, '--------------- Shortest Job First ---------------\n')
