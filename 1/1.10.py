# AVG Speed
#? km to miles (Distance)
km = int(input("Enter how far the runner ran in KM: "))
miles = km / 1.6
# print(miles)

#? mins & sec to hours (TotalTime)
hours = int(input("Hours: "))
mins = int(input("Minutes: "))
sec = int(input("Seconds: "))
totalTime = (mins / 60) + (sec / 3600) + hours  
mph = miles / totalTime

print(f"The Average Speed of a runner is {mph:.2f} mph")
    