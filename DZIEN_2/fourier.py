import numpy as np
import matplotlib.pyplot as plt

samplingFrequency = 100
samplingInterval =1/samplingFrequency

beginTime = 0
endTime = 10

signal1Frequency = 4 #4Hz
signal2Frequency = 7 #7Hz

time = np.arange(beginTime,endTime,samplingInterval)

amplitude1 = np.sin(2*np.pi*signal1Frequency*time)
amplitude2 = np.sin(2*np.pi*signal2Frequency*time)

figure, axis = plt.subplots(4,1)
plt.subplots_adjust(hspace=1)

#wykres pierwszej funkcji falowej
axis[0].set_title('funkcja falowa o częstotliwości 4Hz')
axis[0].plot(time,amplitude1)
axis[0].set_xlabel('Czas [s]')
axis[0].set_ylabel('Amplituda')


#wykres drugiej funkcji falowej
axis[1].set_title('funkcja falowa o częstotliwości 7Hz')
axis[1].plot(time,amplitude2)
axis[1].set_xlabel('Czas [s]')
axis[1].set_ylabel('Amplituda')

#złożenie funkcji falowych
amplitude = amplitude1 + amplitude2

#wykres złożenia funkcji falowych
axis[2].set_title('złożenie funkcji falowych o częstotliwościach 4Hz i 7Hz')
axis[2].plot(time,amplitude)
axis[2].set_xlabel('Czas [s]')
axis[2].set_ylabel('Amplituda')
