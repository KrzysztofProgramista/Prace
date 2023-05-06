import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
numpy.random.seed(2)
x = numpy.random.normal(4,1,100)
y = numpy.random.normal(150,50,100)/x
t_x = x[:80]
t_y = y[:80]
plt.scatter(t_x,t_y)
plt.show()
te_x = x[80:]
te_y = y[80:]
plt.scatter(te_x,te_y)
plt.show()
mml = numpy.poly1d(numpy.polyfit(t_x,t_y,4))
ml = numpy.linspace(0,6,100)
plt.scatter(t_x,t_y)
plt.plot(ml,mml(ml))
plt.show()
r2T = r2_score(t_y,mml(t_x))
print(r2T)
r2Te = r2_score(te_y,mml(te_x))
print(r2Te)
print(mml(0.5))