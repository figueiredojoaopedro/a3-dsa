def defineTempoReal(simulationTime, realTime, equivalentToOneHour):
    print(simulationTime);
    if ((simulationTime == 20
        or simulationTime == 40
        or simulationTime == 60
        or simulationTime == 80
        or simulationTime == 100
        or simulationTime == 120) and simulationTime % equivalentToOneHour == 0):
            realTime += 1  # add + 1 hour
            print("{}:00 Horas".format(realTime));

    return realTime;