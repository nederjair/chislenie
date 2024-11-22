import math
import matplotlib.pyplot as plt
import numpy as np
#### function definition
def fx(x):
    # change according your variant
    return math.log(x)**(12/11)

def polyLag(x):
    # change according your variant
    a = ((x**2-26*x+168)/8)*(math.log(10)**(12/11))
    b = ((x**2-24*x+140)/4)*(math.log(12)**(12/11))
    c = ((x**2-22*x+120)/8)*(math.log(14)**(12/11))
    return a - b + c
#parameter definition (change according your variant)
a = 13.5
x = [10, 12, 14]

####################dont change##############################
ya = fx(a)
y  = []
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

plt.plot(x_, y, '--r', linewidth='2')  
plt.plot(x_, y_, '-b', linewidth='2')  
plt.xlabel('x')  
plt.ylabel('f(x)')  
plt.title('Lagrange Polynom Approximation')  
plt.legend(['Exact', 'Approx'], loc="lower right")

plt.savefig('fig1.svg')
#plt.show()  
