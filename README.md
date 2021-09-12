# Background_Colony_Noise
This repository is designed to help prepare .wav files for the McDermott synthesis algorithm. The algorithm requires short .wav files to synthesis noise from a gaussian distribution.

After you have cloned the respository to your desired location, you will need to pull the 24 hour recordings of colony-noise into your directory. 

You will need to create a .csv file with the first column being the name of the .arf file you want to pull the .wav files from. The second column should be the hour (in military time i.e. 22 for 10pm) you want to sample from. The third column will be the duration of the .wav file you want to sample in seconds. The waveconverter.py file ignores the first row and can be used as the headings for your columns. I recommend saving this .csv file as "Hour.csv" but the name can be flexibile as long as you change the waveconverter.py script to look for the name of the csv file you choose.

To run the waveconverter.py script you need to make sure you have the required packages installed. I recommend setting up a virtual environment to do this. Once you are ready you can run the script with `python waveconverter.py`

Finally, you will need to make a whitenoise .wav file for the McDermott synthesis package. To do this you can run the script `python whitenoise.py --sample-rate 48000 --time 7`. For more information you can run --help to see a discription of the arguments the whitenoise.py script takes.
