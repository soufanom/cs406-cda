# Objective:
# Create a scatter plot to explore the relationship between two variables in the palmerpenguins dataset. You will visualize the correlation between the flipper length and the culmen length of penguins, differentiated by species.
#
# Requirements:
# Make sure you have the necessary libraries installed:
#
# palmerpenguins for the dataset
# matplotlib.pyplot for plotting
# Load the penguins dataset using the load_penguins() function from the palmerpenguins library.
#
# Prepare your data by filtering out any rows with missing values in the variables of interest ('flipper_length_mm' and 'culmen_length_mm').
#
# Create a scatter plot using Matplotlib, where:
#
# The x-axis represents the bill length ('bill_length_mm')
# The y-axis represents the flipper length ('flipper_length_mm')
# Each point represents a penguin observation
# Differentiate the data points by penguin species using the color aesthetic. Assign a unique color to each species. (Hint: You may use a dictionary to map species to colors or the c parameter in plt.scatter to set colors.)
#
# Add appropriate labels to the x-axis and y-axis, and a title to the plot.
#
# Include a legend to identify the species based on color.

import matplotlib.pyplot as plt
from palmerpenguins import load_penguins

# Load the dataset
penguins = load_penguins()

# Filter out rows with missing data for the variables of interest
filtered_penguins = penguins.dropna(subset=['flipper_length_mm', 'bill_length_mm'])

