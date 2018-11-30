
from memory_profiler import memory_usage

def f():
  import numpy as np
  import pandas as pd

  store = pd.HDFStore('test.h5', 'r')
  print(store.info())
  print()
  count = 0
  df = store['df']
  N = int(0.01*len(df))
  for i in range(N):
    if i%1000 == 0: print(i)
    #count += store.get('df').loc[i, 'd']
    #count += store['df'].loc[i, 'd']
    count += df.loc[i, 'd']
  store.close()

mem_usage = memory_usage(f)
print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
print('Maximum memory usage: %s' % max(mem_usage))

