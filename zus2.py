import matplotlib.pyplot as plt
from scipy import stats
x = [1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965]

y= [7188,7824,11040,11700,12096,13416,15348,16176,17436,18720,19500,20160,21156,21792,22404]

slope,intercept,r,p,std_err = stats.linregress(x,y)
def myfu(x):
    return slope * x + intercept
mymodel = list(map(myfu, x))
plt.scatter(x, y)
plt.plot(x,mymodel)

plt.show()
