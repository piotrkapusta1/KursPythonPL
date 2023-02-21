ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

flightConnetions = ((start, end) for start in ports for end in ports )
i = 0
for (start, stop) in flightConnetions:
    i+=1
print(i)
i = 0
flightConnetions = ((start, end) for start in ports for end in ports if start != end )
for (start, stop) in flightConnetions:
    i+=1
print(i)
i = 0
flightConnetions = ((start, stop) for start in ports for stop in ports if start < stop)
for (start, stop) in flightConnetions:
    i+=1
print(i)

