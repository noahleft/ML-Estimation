#!/usr/local/bin/python3

import shelve

def read_data():
  with shelve.open('raw') as db:
    data = db['data']
  return data

from data.config import x_min,x_max
from data.config import func
import numpy as np
def get_plot_data():
  t = np.arange(x_min,x_max,0.01)
  return t

def get_train_data():
  t = np.arange(x_min,x_max,0.01)
  s = list(map(func,t))
  return (t,s)

