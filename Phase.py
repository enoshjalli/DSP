#Phase
import matplotlib.pyplot as plt
import numpy as np
F1=10
F2=20
Fs=50
t=np.arange(0,10,0.01)
A=5*(np.sin((2*np.pi*F1/Fs*t)+30))
plt.subplot(221)
plt.plot(t,A)
plt.xlabel("------>time")
plt.ylabel("------>Amplitude")
B=np.sin((2*np.pi*F2/Fs*t)+75)
plt.subplot(222)
plt.plot(t,B)
plt.xlabel("------>time")
plt.ylabel("------>Amplitude")
plt.show()

