#!/usr/local/bin/python3
from matplotlib import pyplot
from data.read_data import read_data

data = read_data()

from data.config import x_min,x_max
from data.config import func
import numpy as np
t = np.arange(x_min,x_max,0.01)
s = list(map(func,t))
actual = pyplot.plot(t,s, label='actual')


x = list(map(lambda x: x[0],data))
y = list(map(lambda x: x[1],data))
raw = pyplot.plot(x,y,'ro', label='raw data')

pyplot.xlabel('input data (x)')
pyplot.ylabel('target (t)')
pyplot.grid(True)
pyplot.title('Raw data and the actual function')

pyplot.legend(loc='upper left')

pyplot.show()



