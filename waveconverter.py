##Packages##
import h5py as h5
import numpy as np
import pandas as pd
import os
import ewave

##Functions##
def wav_intervals(csv, sample_rate, hour_to_sample_rate):
    for row in csv.itertuples(): #iterates through each row in the csv file
        arf_file = row[0]
        start_time = row[1]*hour_to_sample_rate #takes the second column and calculates the start point
        duration = row[2]*sample_rate #takes the third column and calculates the sample duration (i.e. 7 seconds)
    return arf_file, start_time, duration        

def wavdata (sample, start_time, duration):
    subsample = np.zeros(duration) #creates a one dimensional array filled with zeros that is the length of duration
    for i in range(start_time,start_time + duration):  # sample a range from the start time to the start time + duration
        subsample[i - start_time] = sample[i]  # pulls the data and assigns it to subsample
        data = subsample  # Sets the data to be converted
    return data

##Script##
sample_rate = 48000
hour_to_sample_rate = 60*60*sample_rate
csv = pd.read_csv('Hour.csv',index_col = 0) #reads in the csv and indexes the first column
arf_file, start_time, duration = wav_intervals(csv, sample_rate, hour_to_sample_rate)
with h5.File(arf_file, 'r') as R1:  # takes the first column file path and imports the arf file
    ls = list(R1.keys())  # lists the keys
    name = ls[0]
    data = R1.get(ls[0])  # pulls the first key which has the data
    lsdata = list(data.keys())  # lists the keys in this shell
    sample = data.get(lsdata[0])  # pulls the data
    data = wavdata(sample, start_time, duration)
start_time_hour = int(start_time/hour_to_sample_rate)
duration_seconds = int(duration/sample_rate)
with ewave.open("{}_{}_{}.wav".format(name, start_time_hour, duration_seconds),"w+",sampling_rate=sample_rate,dtype='f') as fp: #sets the name of the file, sets the mode to open a file, the sampling rate, and the float datatype
    fp.write(data)
