import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# sampling rate
sr = 2000
# sampling interval
ts = 0.8/sr
t = np.arange(0,1,ts)

# x = 3*np.sin(2*np.pi*freq*t)

# Load the data from the CSV file, ignoring the first row
for picture in range(13):
    file_path = 'Erdnuss_Holz_{}.csv'.format(picture)
    # data = pd.read_csv(file_path, skiprows=1)

    # Reload the data with the correct delimiter
    data = pd.read_csv(file_path, delimiter=';', skiprows=1)


    # Replace commas with dots in the dataframe and convert to float
    data = data.apply(lambda x: x.str.replace(',', '.').astype(float))


    x = data.iloc[:, 2]
    t = data.iloc[:, 0] / 1000
    sr = 1/t[0]

    # print(x)

    for value in range(len(x)):
        if x[value] == "":
            x.pop(value)

    plt.figure(figsize = (8, 6))
    plt.plot(t, x, 'r')
    plt.ylabel('Amplitude')


    from numpy.fft import fft, ifft

    X = fft(x)
    N = len(X)
    n = np.arange(N)
    T = N/sr
    freq = n/T
    #print(sr)
    #print('\n\n',t[:5])

    #stop()
    #print(freq)
    #print('\n\n')

    taron = plt.figure(figsize = (12, 6))

    #plt.stem(freq, np.abs(X), 'b', \
    #         markerfmt=" ", basefmt="-b")
    # plt.loglog(freq,np.abs(X),)
    plt.plot(freq,np.abs(X),)
    plt.xlabel('Freq (Hz)')
    plt.ylabel('FFT Amplitude |X(freq)|')
    plt.xlim(0, sr/2)
    plt.ylim(0.005, 1000)

    # plt.subplot(122)
    # plt.plot(t, ifft(X), 'r')
    # plt.xlabel('Time (s)')
    # plt.ylabel('Amplitude')
    # plt.tight_layout()
    # plt.show()
    # plt.plot(freq, np.angle(X)/np.pi*180, 'r')
    # plt.xlabel('Freq (Hz)')
    # plt.ylabel('FFT phase angle ')
    # plt.xlim(0, sr/2)
    # plt.tight_layout()
    try:
        plt.savefig('results/fft_test_lin/Test_{}.png'.format(picture))
    except:
        try:  
            os.mkdir("results/fft_test_lin") 
            plt.savefig('results/fft_test_lin/Test_{}.png'.format(picture)) 
        except OSError as error:  
            print(error)