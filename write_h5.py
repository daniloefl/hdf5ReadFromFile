
import numpy as np
import pandas as pd

N = 100000000
df = pd.DataFrame({'a': np.zeros(N), 'b':np.zeros(N), 'c': np.zeros(N), 'd': np.zeros(N)})
store = pd.HDFStore('test.h5', 'w')
store.put('df', df, format = 'table', data_columns = True)
store.close()



