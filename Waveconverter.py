import h5py as h5
import numpy as np
import ewave
import pandas as pd
csv = pd.read_csv('Hour.csv',index_col = 0) #reads in the csv and indexes the first column
for row in csv.itertuples(): #iterates through each row in the csv file
    Start_Time = row[1]*60*60*48000 #takes the second column and calculates the start point
    Duration = row[2]*48000 #takes the third column and calculates the sample duration (i.e. 7 seconds)
    with h5.File(row[0],'r') as R1: #takes the first column file path and imports the arf file
        ls = list(R1.keys()) #lists the keys
        data = R1.get(ls[0]) #pulls the first key which has the data
        lsdata = list(data.keys()) #lists the keys in this shell
        sample = data.get(lsdata[0]) #pulls the data
        subsample = np.zeros(Duration) #creates a one dimensional array filled with zeros that is the length of duration
        for i in range(Start_Time,Start_Time+Duration): #sample a range from the start time to the start time + duration
            subsample[i-Start_Time] = sample[i] #pulls the data and assigns it to subsample
        data = subsample #Sets the data to be converted
        with ewave.open("{}_{}_{}.wav".format(ls[0],row[1],row[2]),"w+",sampling_rate=48000,dtype='f') as fp: #sets the name of the file, sets the mode to open a file, the sampling rate, and the float datatype
            fp.write(data)