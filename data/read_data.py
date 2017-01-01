#!/usr/local/bin/python3

import shelve

def read_data():
  with shelve.open('raw') as db:
    data = db['data']
  return data

