import time

#ILA Calculator
hourlyRate= float(input("Please enter the Attorny's Hourly Rate: "))
IntervalRate= hourlyRate/10
total= IntervalRate
print("You can start the timer by pressing t and stop the timer by clicking s.") 

key= input()
if key == "t" :
    starttime = time.time()
    print(f"Timer started at: {time.ctime(starttime)}")

key = input()
if key == "s":
    endtime =time.time()
    print(f"Timer ended at: {time.ctime(endtime)}")
    total = (round((endtime-starttime)/360))*IntervalRate
        
print(total)





    





#check timer every 6 minutes, then add interval rate 








