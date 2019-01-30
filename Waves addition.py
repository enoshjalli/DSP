#waves addition
import matplotlib.pyplot as plt
import numpy as m
F1=10
F2=20
Fs=50
t=m.arange(0,10,0.01)
A=m.sin(2*m.pi*F1/Fs*t)
plt.subplot(221)
plt.plot(t,A)
plt.xlabel("------>time")
plt.ylabel("------>Amplitude")
B=m.sin(2*m.pi*F2/Fs*t)
plt.subplot(222)
plt.plot(t,B)
plt.xlabel("------>time")
plt.ylabel("------>Amplitude")
C=A+B
plt.subplot(223)
plt.plot(t,C)
plt.xlabel("------>time")
plt.ylabel("------>Amplitude")
D=A-B
plt.subplot(224)
plt.plot(t,D)
plt.xlabel("- - - - - ->time")
plt.ylabel(" - - - - ->Amplitude")
plt.show()
