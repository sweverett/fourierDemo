## A quick Fourier transform demo to test out GitHub features
## Written by Spencer Everett
## June 20, 2015

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

## Make function y as the superposition of two sinusoidal functions y1 and y2 with different frequencies

pi = sp.pi;
freq1 = 1
freq2 = 3

x = sp.arange(0,2,.001)
y1 = sp.sin(2*pi*freq1*x)
y2 = 0.5*sp.sin(2*pi*freq2*x)

y = y1+y2

## Plot all functions

plt.plot(x,y1,'--g',x,y2,'--r',x,y,'b')

plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend([r'$\sin(2\pi x)$',r'$\sin(6\pi x)$',r'$\sin(2\pi x)+\sin(6\pi x)$'])

fig = plt.gcf()
fig.set_size_inches(10, 6)
plt.show()

## Fourier Transform of y

fs = 1/(x[1]-x[0])
N = x.size

freq = sp.arange(0,N)*fs/N

Y = sp.fft(y)
Ps = sp.sqrt(Y*sp.conj(Y))

plt.plot(freq,Ps)
plt.xlim([0,1.5*max(freq1,freq2)])
plt.title('Power Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

fig2 = plt.gcf()
fig2.set_size_inches(10, 6)
plt.show()

## Centered Fourier Transform of Y

if N%2 is 0:

    freq = sp.arange(-(N-1)/2,N/2)*fs/N

else:

    freq = sp.arange(-N/2,N/2)*fs/N

Yc = np.fft.fftshift(Y)

plt.plot(freq,sp.sqrt(Yc*sp.conj(Yc)))
plt.xlim([-2*max(freq1,freq2),2*max(freq1,freq2)])
plt.title('Centered Power Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

fig3 = plt.gcf()
fig3.set_size_inches(10, 6)
plt.show()