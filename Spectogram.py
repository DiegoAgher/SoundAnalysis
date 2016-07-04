import numpy as np
import scipy
from scipy.io import wavfile
from scipy import signal
import pandas as pd
import matplotlib.pyplot as plt


print "version: ", scipy.__version__

class Signal(object):
    def __init__(self, file):
        self.file = file
        self.sampFreq, self.raw_signal = self.read_file_to_signal()
        self.define_channels()

    def read_file_to_signal(self):
        if self.file:
            return wavfile.read(self.file)
        else:
            print "no file to read"
            raise Exception

    def define_channels(self):
        channels = self.raw_signal.shape[1]
        self.channels = {}
        for i in range(0, channels):
            self.channels["channel_{0}".format(i)] = self.raw_signal[:, i]

    def show_plot(self,channel):
        channel_name = "channel_"+str(channel)
        plt.plot(self.channel_name)
        plt.show()


class AudioSpectrogram(object):
    def __init__(self, signal_data):
        self.signal = signal_data
        self.freq = signal_data.sampFreq
        self.spectograms = {}
        for i, channel in enumerate(self.signal.channels):
            self.spectograms["channel_{0}".format(i)] = signal.spectrogram(self.signal.channels[channel], self.freq)








wav_file = ('bach/onclassical_demo_elysium_anonymous-elysium_the-young-false-man_small-version_live-and_restored.wav')

first_song = Signal(wav_file)
spectogram_1 = AudioSpectrogram(first_song)

print " look ", spectogram_1.spectograms['channel_1']

print "end"


# number of seconds for signal = sampFreq * seconds

