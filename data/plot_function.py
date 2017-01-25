#!/usr/local/bin/python3
from matplotlib import pyplot

def plot(x,y,param,labelstr=""):
  pyplot.plot(x,y,param,label = labelstr)

def show():
  pyplot.xlabel('input data (x)')
  pyplot.ylabel('target (t)')
  pyplot.legend(loc='upper left')
  pyplot.grid(True)
  pyplot.ylim( (-10,10) )
  pyplot.show()

def setTitle(title):
  pyplot.title(title)


