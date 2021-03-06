
from SEgli_01_Fibonacci import *
print( get_best_iteration_runtime(2) )

#print( get_best_iteration_runtime(1000000) )

#print( get_best_recursion_runtime(25) )

#print( fib( 4 ) )

#print(fib_recursion_count(4))

from SEgli_01_Measurement import *

show_measurement_formula_vs_iterative(0,300)

"""
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(4*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()





print("Measurement start")
elapsed = {}
#elapsed['recursion'] = {}
elapsed['iteration'] = {}
elapsed['formula'] = {}
for i in range(1000):
    t_start = time.time()
    print(fib_recursive(i))
    t_end = time.time()
    elapsed['recursion'][i] = t_end - t_start
    t_start = time.time()
    #print(fib_iterative(i))
    t_end = time.time()
    elapsed['iteration'][i] = t_end - t_start

    t_start = time.time()
    #print(fib_formula(i))
    t_end = time.time()
    elapsed['formula'][i] = t_end - t_start

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

elapased_ms = pd.DataFrame(elapsed) * 1000
elapased_ms.plot(title='time taken to compute the n-th Fibonaccis number')
plt.ylabel('time taken (ms)')
plt.xlabel('n')
plt.grid(True)
plt.savefig("test.png")
plt.show()
      
"""