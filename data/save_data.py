#!/usr/local/bin/python3

import shelve

def save_data(data):
  with shelve.open('raw') as db:
    db['data'] = data

