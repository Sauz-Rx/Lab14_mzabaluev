'''
Cosine function
Maksim Zabaluev 
8/2/2025
Plot a math formula of our choosing. I chose: x + 10 * 2
'''

import matplotlib.pyplot as plt 

x_val = []
y_val = []

for i in range(10):
    x_val.append(i)
    y_val.append(i)

x_val.append(10)
y_val.append(y_val[-1]* 2)


plt.figure()
plt.plot(x_val, y_val, label ='x + 10 *2', color = 'red', linewidth = 3)    
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
