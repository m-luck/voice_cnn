from scipy import signal
import scipy.io.wavfile as wav
from matplotlib import pyplot as plt

fs, x = wav.read('voice_test.wav')

f, t, Sxx = signal.spectrogram(x, fs)
plt.pcolormesh(t, f, Sxx)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()