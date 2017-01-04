#!/usr/local/bin/python3

import random
from math import sin
from config import func

def createData(x_min,x_max,noise_range,num):
  retArray = []
  print("  Machine Learning  ")
  print("===  Create data ===")
  print("x range from ",x_min," to ",x_max)
  print("noise range ",noise_range)
  print("data size ",num)
  for idx in range(num):
    x = random.uniform(x_min,x_max)
    y = func(x)
    t = y + random.gauss(0,noise_range)
    retArray.append([x,t])
  return retArray


from config import x_min,x_max
from config import noise
from config import num


data = createData(x_min,x_max,noise,num)

from save_data import save_data
save_data(data)


