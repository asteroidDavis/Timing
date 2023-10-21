from abc import ABC, abstractmethod
from functools import lru_cache
from typing import List
from uuid import uuid4


class Timing():

    def __init__(self, npts, sps, observation_name: str = None):
        """
        Timing - Create a timing struct with everything necassary for a frequency
        spectrum plot
        PARAMETERS
           npts - number of points in the time vector
           SPS - samples per second,sampling frequency
        Returns a struct with
           delta_frequency - change in frequency between elements of the frequecy vector
           delta_time - change in time between elements of the time vector
           frequency - the frequency vector
           nyquist_frequency - nyquist frequency
           number_of_points - number of points in the time vector
           samples_per_second - samples per second
           Tmax - the highest time element in the time vector
           time - the time vector
        EXAMPLE
           timing = Timing(512, 256);
           generate a wave TODO: fix this example
           wave = sin(2*pi*timing.t);
        VERSION
           0.1(First release)
        """
        self.number_of_points = npts
        self.samples_per_second = sps
        self.nyquist_frequency = sps/2.0
        self.delta_time = 1.0/sps
        self.max_time = npts*self.delta_time - self.delta_time
        self.delta_frequency = 1.0/self.max_time
        if observation_name is None:
            self.observation_name = str(uuid4())

    @property
    def time(self) -> List[float]:
        """The vector of the signals time domain"""
        return [0.0 + self.delta_time * i for i in self.number_of_points ]

    @property
    def frequency(self) -> List[float]:
        """The vector of the signals' frequency domain"""
        frequency_domain_size = self.nyquist_frequency/self.delta_frequency
        return [0.0 + self.delta_frequency * i for i in range(frequency_domain_size)] \
            + [-self.nyquist_frequency - self.delta_frequency * i for i in range(frequency_domain_size)]

"""
Timing - Create a timing struct with everything necassary for a frequency
spectrum plot
PARAMETERS
npts - number of points in the time vector
SPS - samples per second,sampling frequency
Returns a struct with
    deltaF - change in frequency between elements of the frequecy vector
    dt - change in time between elements of the time vector
    F - the frequency vector
    Fn - nyquist frequency
    npts - number of points in the time vector
    SPS - samples per second
    Tmax - the highest time element in the time vector
    t - the time vector
EXAMPLE
timing = Timing(512, 256);
generate a wave
wave = sin(2*pi*timing.t);
VERSION
1.0
    python client
    python Timing inteface

VERSION HISTORY 0.1(First release)
"""