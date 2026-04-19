"""
in python we have two functions to create arrays with equally spaced values:
1. numpy.arange()
2. numpy.linspace()
    1. numpy.arange() function is used to create an array with equally spaced values within a specified range. The syntax for this function is:
    numpy.arange(start, stop, step)
    """
import numpy as np
a = np.arange(15)
print(a)
"""output:
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
"""
a = np.arange(1, 10, 2)
print(a)

"""output:
[1 3 5 7 9]
"""
"""linspace() function is used to create an array with equally spaced values between a specified start and stop value. The syntax for this function is:
numpy.linspace(start, stop, num)"""

b=np.linspace(1, 10, 10)
print((int)b)
"""output:
[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
"""