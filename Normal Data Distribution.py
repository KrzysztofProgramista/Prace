import NumPy
import matplotlib.pyplot as plt
x = numpy.random.normal(20.0,2.0,200000)

plt.hist(x,200)
plt.show()