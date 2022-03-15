# temp_convert_arr.py
# This program converts Celsius temperatures stored in a numpy array
# to Fahrenheit.

import numpy as np

celsius = np.random.randint(100, size=10)
fahrenheit = 9 * celsius / 5 + 32
print("Temperatures in Celsius degrees:\n", celsius)
print("Correponding temperatures in Fahrenheit degrees:\n", fahrenheit)
