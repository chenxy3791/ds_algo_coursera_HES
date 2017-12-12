# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 10:40:55 2017

binary_search test program

@author: chenxy
"""

# Random test    
import datetime
import time
import numpy as np
import matplotlib.pyplot as plt
import binary_search as bs

print("\n\n---Self random test start---\n")

#Generate random but ordered non-negative integer sequence in the range of [0,10**9].
#Each number in the sequence should unique.

#Test the format of datetime.now
#  According to the test result:
#  sleep() set the sleep time in unit of second
#  print(delta[=dt2-dt1]) shows the time difference in unit second
dt1 = datetime.datetime.now()
time.sleep(1)
dt2 = datetime.datetime.now()
delta = dt2 - dt1
print(delta)

#m = 50000
m_list  = []
dt_list = []
for m in np.linspace(5000,20000,10):
    m_int = int(m)
    a = np.random.randint(10**9,size = m_int)
    a_list = list(a)
    b = list(set(a_list))
    b.sort()
    n = len(b)    
    
    dt1 = datetime.datetime.now()
    for x_idx in range(-1,n+1):
        #x_idx = np.random.randint(n)
        if x_idx == -1:
            x = b[0] - 1
        elif x_idx == n:
            x = b[n-1] + 1
        else:    
        x     = b[x_idx]
        k     = bs.binary_search(b,x)     
        #k     = bs.linear_search(b,x)     
        assert k==x_idx or k==-1 or k==n,'k!=x_idx'
        
    dt2 = datetime.datetime.now()
    delta = dt2 - dt1
    
    m_list.append(m_int)
    dt_list.append(delta.total_seconds())
    print(len(a),len(b))
      
#print(m_list)
#print(dt_list)
m_array  = np.array(m_list)
dt_array = np.array(dt_list)

plt.figure()
plt.plot(m_array,dt_array)

plt.xlabel('input array size: m')
plt.ylabel('total time[seconds] for m search over array with size of m')

