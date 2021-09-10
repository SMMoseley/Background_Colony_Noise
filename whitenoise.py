########################Create White Noise###################
##Packages##
import numpy as np
import ewave
import argparse

##Arguments##
parser = argparse.ArgumentParser(description='Create Whitenoise')
parser.add_argument('--sample-rate', metavar='S', type=int, required=True,
        help='sample-rate for whitenoise file')
parser.add_argument('--time', type=int, required=True,
                    help='duration of output whitenoise in seconds')

args = parser.parse_args()

##Variables##
sample_rate = args.sample_rate
second = args.time
n =sample_rate*second
whitenoise = np.random.normal(0.0,  1.0, n)

##Script##
with ewave.open("whitenoise_{}.wav".format(second),"w+",sampling_rate=sample_rate,dtype='f') as fp: #sets the name of the file, sets the mode to open a file, the sampling rate, and the float datatype
    fp.write(whitenoise)
