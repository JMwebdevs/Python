population = 119791551
oneDay = (24 * 60) * 60
secAYear = oneDay * 365

birthAYear = secAYear // 7
deathsAYear = secAYear // 13
immigrants = secAYear //45  
for i in range(1,6):
   netChange = birthAYear - deathsAYear + immigrants
   population = population + netChange

   print(f"Year {i}: {population}")
   
