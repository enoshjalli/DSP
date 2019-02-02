#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:21:13 2019

@author: apiiit-rkv
"""

import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs1,data1=wav.read('enosh.wav')
print(fs1,len(data1),data1)
plt.subplot(211)
plt.plot(data1)
t=np.arange(0,len(data1)/fs1,1.0/fs1)
plt.subplot(212)
plt.plot(t,data1)
plt.show()
wav.write('enosh-fast.wav',2*fs1,data1)
wav.write('enosh-slow.wav',0.5*fs1,data1)