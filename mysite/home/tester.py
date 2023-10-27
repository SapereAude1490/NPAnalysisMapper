# # Q: Create a plotly scatter plot of the of a sine wave where I can change the frequency and amplitude of the wave using sliders.

# import plotly.graph_objects as go

# import numpy as np

# from scipy import signal

# import dash

# import dash_core_components as dcc

# import dash_html_components as html

# from dash.dependencies import Input, Output

# app = dash.Dash()

# app.layout = html.Div([
#     dcc.Graph(id="graph"),
#     html.Label([
#         "Frequency",
#         dcc.Slider(
#             id="freq-slider",
#             min=1,
#             max=10,
#             step=0.5,
#             value=1,
#             marks={i: str(i) for i in range(10)},
#         ),
#     ]),

#     html.Label([
#         "Amplitude",
#         dcc.Slider(
#             id="amp-slider",
#             min=1,
#             max=10,
#             step=0.5,
#             value=1,
#             marks={i: str(i) for i in range(10)},
#         ),
#     ]),
# ])

# @app.callback(
#     Output("graph", "figure"),
#     [Input("freq-slider", "value"),
#      Input("amp-slider", "value")])
# def display_sine(freq, amp):
#     x = np.linspace(0, 10, 1000)
#     y = amp * np.sin(freq * x)
#     fig = go.Figure(data=go.Scatter(x=x, y=y, mode="lines"))
#     return fig


# if __name__ == "__main__":
#     app.run_server(debug=True)



# import numpy as np
# from lib import spcalext

# # Create a sample dataset
# x = np.array([1.0, 2.0, 3.0, 2.0, 1.0, 4.0, 5.0, 4.0, 3.0, 2.0])

# # Define the regions of interest
# regions = np.array([[0, 5], [5, 10]])

# # Call the maxima function from the spcalext module
# maxima = spcalext.maxima(x, regions)

# # Print the results
# print("Input array:", x)
# print("Regions:", regions)
# print("Maxima:", maxima)

# Here we're going to test the data_processing.py file funcions and their output

import numpy as np
import matplotlib.pyplot as plt
from data_processing import process_file

# Create a numpy array with 1000 rows and 2 columns
# The first column will go from 0 to 1000
# Second column will be all ones
array = np.ones((1000,2))
array[:,0] = np.linspace(0,1000,1000)
# Pick a few random numbers in the second column and add a random number from 10 to 100 to them
array[np.random.randint(0,1000,10),1] += np.random.randint(10,100,10)
# Define a simple 1D kernel
kernel = np.array([0.05,0.15,0.4,0.3,0.1])
# Convolve the second column of the array with the kernel
array[:,1] = np.convolve(array[:,1],kernel,mode='same')

# Save this array as a .csv file. This is the file that will be read in by the process_file function
np.savetxt('test.csv', array, delimiter=',')

# Get the path to the file
file_path = 'test.csv'

# Call the process_file function
detections, labels, regions = process_file(file_path, convertToCounts=False)

# Display the results
print("Detections:", detections)
print("Regions:", regions)
print(len(labels))

# Crop the array. Remove the top 4 rows and the bottom 3 rows
array = array[4:-3,:]

plt.plot(array[:, 0], array[:, 1])
plt.plot(array[regions[:, 0], 0], array[regions[:, 0], 1], 'ro')
plt.plot(array[regions[:, 1], 0], array[regions[:, 1], 1], 'go')

plt.show()

print("Detections:", detections)
print("Regions:", regions)