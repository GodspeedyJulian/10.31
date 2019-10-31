DailyHoursWorked=[5,10,10]
ProductionData=[[10,11,10,14],[20,16,24,20],[9,11,13,17]]
WorkerTotal=[]

for WorkerNum in range (3):
    WorkerTotal.append(0)
for WorkerNum in range (3):
    for DayNum in range (4):
        WorkerTotal[WorkerNum] = WorkerTotal[WorkerNum]+ProductionData[WorkerNum][DayNum]
for WorkerNum in range(1,3):
    WorkerAverage = WorkerTotal[WorkerNum]/(4*DailyHoursWorked[WorkerNum])
    if WorkerAverage <2:
        print("Investigate", str(WorkerNum))

