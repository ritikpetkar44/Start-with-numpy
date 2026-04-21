"""
Add, Subtract, Multiply, and Divide

agar do matrices ya arrays ke beech me addition, subtraction, multiplication, 
aur division karna hai, to hum numpy ke built-in operators ka use kar sakte hain.


1. Addition
agar hum do arrays ko add karna chahte hain, to hum + operator ka use kar sakte hain.  
 dono arrays ka shape same hona chahiye."""

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)
"""output:
[5 7 9]
"""



"""2. Subtraction
agar hum do arrays ko subtract karna chahte hain, to hum - operator ka use
kar sakte hain. dono arrays ka shape same hona chahiye."""
d = a - b
print(d)
"""output:
[-3 -3 -3]
"""


"""3. Multiplication
agar hum do arrays ko multiply karna chahte hain, to hum * operator ka use kar sakte hain. 
dono arrays ka shape same hona chahiye.
ye element-wise multiplication karta hai, matlab har element ko uske corresponding element se multiply karta hai."""
e = a * b
print(e)
"""output:  
[ 4 10 18]
"""


"""4. Division  agar hum do arrays ko divide karna chahte hain, to hum / operator ka use kar sakte hain. 
dono arrays ka shape same hona chahiye."""
f = a / b   
print(f)
"""output:
[0.25 0.4 0.5 ]
"""