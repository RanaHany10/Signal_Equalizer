
import numpy as np
from scipy.io import wavfile

sampleRate = 44100

length = 5

t = np.linspace(0, length, sampleRate * length)  #  Produces a 5 second Audio-File
y1 =100*np.sin(500 * 2 * np.pi * t)  #  Has frequency of 440Hz

y3 =100*np.sin(1500 * 2 * np.pi * t)

y5 =100*np.sin(2500 * 2 * np.pi * t)

y7 =100*np.sin(3500* 2 * np.pi * t)

y9 =100*np.sin(4500 * 2 * np.pi * t)

y11=100*np.sin(5500 * 2 * np.pi * t)

y13=100*np.sin(6500 * 2 * np.pi * t)

y15=100*np.sin(7500 * 2 * np.pi * t)  

y17=100*np.sin(8500 * 2 * np.pi * t)

y19=100*np.sin(9500 * 2 * np.pi * t)

y21=100*np.sin(10000 * 2 * np.pi * t)


Y_Total = y1 + y3+ y5 + y7 + y9 + y11 + y13  + y15 + y17 + y19 + y21 
# wavfile.write('Sine.wav', sampleRate, Y_Total)
wavfile.write('Sine1.wav',sampleRate, np.int16(Y_Total))