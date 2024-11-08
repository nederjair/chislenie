import math
import matplotlib.pyplot as plt
import numpy as np
#### function definition
def fx(x):
    return math.log(x)**(12/11)
def polyLag(x):
    a = ((x**2-26*x+168)/8)*(math.log(10)**(12/11))
    b = ((x**2-24*x+140)/4)*(math.log(12)**(12/11))
    c = ((x**2-22*x+120)/8)*(math.log(14)**(12/11))
    return a - b + c
#parameter definition
a = 13.5
x = [10, 12, 14]
ya = fx(a)
y  = []
####dont change
samples = 1000
x_ = np.linspace(x[0], x[-1], samples)
y_ = np.full_like(x_, 0)

for i in range(len(x_)):
    y_[i] = polyLag(x_[i])
    y.append(fx(x_[i]))
yaprox = polyLag(a)
for i in range(len(x_)):
    y_[i] = fx(x_[i])
    y_[i] = polyLag(x_[i])

# plotting the points   
plt.plot(x_, y, '--r', linewidth='2')  
plt.plot(x_, y_, '-b', linewidth='2')  
# naming the x axis  
plt.xlabel('x')  
# naming the y axis  
plt.ylabel('f(x)')  
# giving a title to my graph  
plt.title('Lagrange Polynom Approximation')  
plt.legend(['Exact', 'Approx'], loc="lower right")

# function to show the plot  
plt.savefig('fig1.svg')
#plt.show()  
