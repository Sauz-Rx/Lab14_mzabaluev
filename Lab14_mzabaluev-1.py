'''
Cosine function
Maksim Zabaluev 
8/2/2025
Plot a math formula of our choosing. I chose: cos(x) 
'''
import math
import matplotlib.pyplot as plt 


x = list(range(0,360))

# calculate the cosine for each x value  
y = [math.cos(math.radians(a)) for a in x]

plt.figure()
plt.plot(x, y, label ='cos(x)', color = 'blue', linewidth = 2)
plt.xlabel('degrees')
plt.ylabel('y')
plt.grid(True)
plt.show()
