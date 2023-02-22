ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ','LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

flightConnetions = [(start, end) for start in ports for end in ports ]
print(flightConnetions)
print(len(flightConnetions))

flightConnetions = [(start, end) for start in ports for end in ports if start != end ]
print(flightConnetions)
print(len(flightConnetions))

flightConnetions = [ (start, stop) for start in ports for stop in ports if start < stop] 
print(flightConnetions)
print(len(flightConnetions))