#!/usr/bin/env python
# Command-line vertical plot
# source: https://github.com/carmeloc/vPlot 
# history, date format ISO 8601:
#  2017-10-16 1.1 added spacer and basic scaling
#  2017-10-15 1.0 initial version

from __future__ import print_function # future statement definitions
import sys                            # system-specific parameters and functions

# Version number
__version__ = 1.1
__build__ = 171016

'''
inOri contains the CLI arguments as a list of strings, inListNum will contain the input,
except for index=0 (which is the script's name), map-ped to their numerical values
rows is used to span the graph's heigth while cols is the number of data points
'''
inOri = sys.argv[1:]
inListNum = map(float, inOri)
rows = max(inListNum) # 'rows' is a float
cols = len(inListNum)
# the maximum value converted to a string will be used as a reference for spacing
spacer = len(str(rows)) - 2
# scaling, initial version
if rows < 1:
  rows = rows * 10
  inListNum[:] = [x * 10 for x in inListNum]
  spacer += 1
rows = int(rows) # 'rows' is converted to int

'''
L1 will contain a temporary output array-of-arrays, initially containing strings made of blank spaces
its length equals the number of rows while its elements' lengths equal the number of data points
L2 instead will contain the input transformed into 2-tuples in the traditional
cartesian format, (x, y) where y's are taken from inListNum
'''
L1 = [[' ' * (spacer + 1) for i in range(cols)] for j in range(rows)]
L2 = [ i for i in enumerate(inListNum) ]

print("datapoints: " + str(cols) + "\trange: " + str(int(min(inListNum))) + "-" + str(rows))

'''
Here we `scan` the output from top to down, if for each of L2 elements one of them
has a value that corresponds to the index then we change the inner element in L1
to plot a meaningful point
'''
for i in range(rows, 0, -1):
   for data in L2:
     if data[1] >= i:
       L1[rows-i][data[0]] = (' ' *  spacer) + '#'

# Finally L1 has to be iterated through to display it on screen
for i in range(rows):
   print(''.join(L1[i]))

# At the bottom we add the initial values, right-justified
for j in inOri:
  print(''.join(j.rjust(spacer + 1)), end = '')

print('\n')
