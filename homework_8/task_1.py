### PURPOSE: ASTP 720 (Computational Methods) HW #8

################################################################################
### Import Statements
################################################################################

import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
from scipy.signal import find_peaks



##############################################################################
## For Pretty Plotting later on
##############################################################################

params = {'font.family':  'serif',
         'legend.fontsize': 'large',
         'figure.figsize': (12, 8),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}

plt.rcParams.update(params)


################################################################################
### Open data file (strain.npy)
################################################################################

file = 'strain.npy'
array = np.load(file)

strain = array
time = np.linspace(0, len(strain), len(strain)) #units = minutes



################################################################################
### Plot strain vs. time
################################################################################

time_days = [t / 1440 for t in time]

plt.plot(time_days, strain)
plt.xlabel('Time (days)')
plt.ylabel('Strain, h')
plt.title('Simulated Strain from LISA')
#plt.savefig('fig1.eps')
#plt.show()



################################################################################
### Function to compute DFT manually (for small case sizes)
################################################################################

import numpy as np
def DFT(x):
    '''
    Computes Direct Fourier Transform (DFT) of 1d input time series array

    Accepts:
    x  -- input array of values

    Returns
    H  -- DFT of time series
    '''

    x = np.array(x) #enforce this is an array

    N = x.size

    n = np.arange(N)
    k = n.reshape((N, 1))

    e = np.exp(-2j * np.pi * k * n / N)
    H = e@x #@ is matrix multiplication in Python 3
    return(H)


################################################################################
### Function to compute FFT using Cooley-Tukey Algorithm
################################################################################

import numpy as np
def FFT(x, cutoff = 64):

    '''
    Recursive implementation of Cooley-Tukey Algorithm
    Computes Fast Fourier Transform (FFT) of 1d input time series array

    Accepts:
    x  -- input array of values

    Returns
    H  -- DFT of time series
    '''

    x = np.array(x)  #enforce this is an array

    N = int(x.size)


    if N % 2 != 0:
        raise ValueError("Length of signal array must be power of 2")

    elif N <= 1: #terminating base case
        return

    elif N < cutoff:  #small array case, compute direct using DFT function
        return(DFT(x))

    else: #recursive call

        w = np.exp(-2j * np.pi / N)

        even = FFT(x[0::2], cutoff)
        odd  = FFT(x[1::2], cutoff)

        print(len(even))
        print(len(odd))

        H_k = np.zeros((len(even)), dtype =  'complex_')
        for k in range(len(even)):
            H_k[k] = even[k] + w**k * odd[k]
        return(H_k)


out = FFT(strain)
out_np = np.fft.fft(strain)

################################################################################
### Plot Amplitude function
################################################################################
mpl.rcParams['agg.path.chunksize'] = 10000
sampling_freq = len(time) / (time[-1]*60 - time[0]*60)

freq = np.array([k*sampling_freq/len(time) for k in range(len(time))])
N = len(time)
time_hz = [1/(60*t) for t in time]
plt.plot(np.log10(freq[:N//2]), np.log10(out_np[:N//2]), color = 'k')
plt.xlabel('log(Frequency [Hz])')
plt.ylabel('log(Amplitude)')
plt.title('Result of FFT: Amplitude Spectrum')
plt.savefig('fig2.eps')


################################################################################
### Find the freq. and amplitude of peak
################################################################################

#Get the logs of the quantities
log_out = np.log10(out_np)
log_freq = np.log10(freq)

#Look at a window of data around where the peak is eye-balled to be
window_out = log_out[(log_freq > -3) & (log_freq < -2.5)]
window_freq = log_freq[(log_freq > -3) & (log_freq < -2.5)]

max_out = np.max(window_out)
max_freq = window_freq[np.argmax(window_out)]

print('Max Amplitude: ' + str(max_out))
print('Max Frequency: ' + str(max_freq * 2/ N))
