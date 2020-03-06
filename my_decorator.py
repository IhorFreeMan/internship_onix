# -*- coding: utf-8 -*-

def start_and_end_function(fn):
   def wrapper(*args, **kwargs):
       print("--------Run function: " + str(fn.__name__) + str(help(fn)))
       fn(*args, **kwargs)
       print("--------End function: " + str(fn.__name__))
   return wrapper

