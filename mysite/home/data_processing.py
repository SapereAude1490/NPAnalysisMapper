import numpy as np
import pandas as pd
import scipy.signal as signal
import os
import poisson, detection

def process_file(file_path, convertToCounts=True):
    # Read the file into a pandas dataframe
    df = pd.read_csv(file_path, skiprows=4, skipfooter=3)

    # Convert the dataframe to a numpy array
    array = df.to_numpy()

    # Convert the cps column to counts if necessary
    if convertToCounts:
        array[:,1] = array[:,1] * 0.0001

    # Filter the data using a median filter with a window size of 50
    filtered_array = signal.medfilt(array, 51)

    # Check if the background is less than 10 counts. If it is, use epsilon of 0.5
    # If the background is greater than 10 counts, use epsilon of 0 
    if np.mean(filtered_array) < 10:
        epsilon = 0.5
    else:
        epsilon = 0

    # Calculate the Sc and Sd values for the data set using the currie function. Use the epsilon value calculated above.
    # Each row in the Sc and Sd arrays corresponds to a row in the data set
    Sc, Sd = poisson.currie(filtered_array[:,1], epsilon=epsilon)

    # Use the Sc and Sd values to detect the peaks in the data
    detections, labels, regions = detection.accumulate_detections(array[:,1], Sc, Sd, integrate=True)

    # Obtain the peak areas for each peak
    peak_areas = np.zeros(regions.shape[0])

    for i in range(regions.shape[0]):
        peak_areas[i] = np.sum(array[regions[i,0]:regions[i,1],1])

    return (detections, labels, regions)

def process_data(experiment, experiment_folder, numpy_file):
    # Create a list of all the files in the experiment folder
    files = os.listdir(experiment_folder)
    
    # Sort the files in the experiment folder
    files.sort()

    # Create a list to hold the results for each line scan
    all_results = []

    # Loop over each file in the experiment folder
    for file_name in files:
        # Process the current file
        file_path = os.path.join(experiment_folder, file_name)
        results = process_file(file_path)

        # Append the results to the output list
        all_results.append(results)

    return all_results