import numpy
import matplotlib.pyplot as plt
x = numpy.random.uniform(0.0,20.0,200)
print (x)
plt.hist(x,20)
plt.show()