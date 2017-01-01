#!/usr/local/bin/python3
from read_data import read_data

data = read_data()


from matplotlib import pyplot

x = list(map(lambda x: x[0],data))
y = list(map(lambda x: x[1],data))
pyplot.plot(x,y,'ro')

pyplot.show()

