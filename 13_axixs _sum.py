"""
axis_sum
matrix me 2 dimensions hoti hain,
rows aur columns.
ek x=0 hota hai, to iska matlab hai ki hum rows ke hisab se sum karna chahte hain.
agar x=1 hota hai, to iska matlab hai ki hum columns ke hisab se sum karna chahte hain.
"""


import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
"""output:
[[1 2 3]
 [4 5 6]]

"""



b = np.sum(a, axis=0)
print(b)
"""output:
columns ke hisab se sum karne par hume har column ka sum milega, to output hoga:
1+4=5
2+5=7
3+6=9
like:

[5 7 9]
"""



c = np.sum(a, axis=1)
print(c)
"""output:
rows ke hisab se sum karne par hume har row ka sum milega, to output hoga:
1+2+3=6
4+5+6=15
like:

[ 6 15]
"""