# some windows powershell codes:

# pwd as print working directory : where i am
# ls : list the all files
# mkdir as make directory : make a new folder 
# touch : make a new file
# cd : you can enter in any file you want 
# cd .. : can back one file 

# python decorators:

import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970 

# Write your code below 👇

def speed_calc_decorator(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"{func.__name__} run speed: {end_time - start_time}s")
        return result
    return wrapper

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i
        
@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()
slow_function()