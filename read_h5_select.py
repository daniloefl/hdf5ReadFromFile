
from memory_profiler import memory_usage

def f():
  import numpy as np
  import pandas as pd
  import gc
  
  store = pd.HDFStore('test.h5', 'r')
  print(store.info())
  print()
  count = 0
  N = int(0.01*store.get_storer('df').nrows)
  n_batch = 1000
  for i in range(int(N/n_batch)):
    if ((i*n_batch)%1000) == 0: print(i*n_batch)
    batch = store.select('df', start = i*n_batch, stop = (i+1)*n_batch)
    count += batch.loc[:,'d'].sum()
    del batch
    gc.collect()
  store.close()

mem_usage = memory_usage(f)
print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
print('Maximum memory usage: %s' % max(mem_usage))
