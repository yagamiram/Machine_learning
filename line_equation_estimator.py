'''
This python file will return a line equation (slope, intercept) with less error.
To understand the concept, check the notes or the below link.
Link: http://jeremykun.com/2013/08/18/linear-regression/
'''
avg = lambda L: 1.0* sum(L)/len(L)
 
def bestLinearEstimator(points):
   z = zip(*points)
   print z
   xAvg, yAvg = map(avg, zip(*points))
 
   aNum = 0
   aDenom = 0
   for (x,y) in points:
      aNum += (y - yAvg) * x
      aDenom += (x - xAvg) * x
 
   a = float(aNum) / aDenom
   b = yAvg - a * xAvg
   return (a, b), lambda x: a*x + b
# get a set of random points
# here the points are randomly generated very close to the slope 0.5 and intercept 7.0
import random
a = 0.5
b = 7.0
points = [(x, a*x + b + (random.random() * 0.4 - 0.2)) for x in [random.random() * 10 for _ in range(100)]]
# result of the funcion bestLinearEstimator will be (slope, intercept) and it will close to the
# value a and b declared above which means it has found a best line equation with less error.
print bestLinearEstimator(points)[0]

'''
Line equation estimator for multi variables X
X is matrix and w and y are coefficients

Link:http://jeremykun.com/2013/08/18/linear-regression/
'''
from numpy import array, dot, transpose
from numpy.linalg import inv
 
def bestLinearEstimatorMV(points):
   # input points are n+1 tuples of n inputs and 1 output
   X = array([[1] + list(p[:-1]) for p in points]) # add bias as x_0
   y = array([p[-1] for p in points])
 
   Xt = transpose(X)
   theInverse = inv(dot(Xt, X))
   w = dot(dot(theInverse, Xt), y)
   return w, lambda x: dot(w, x)
   
print(bestLinearEstimatorMV(points)[0])
trueW = array([-3,1,2,3,4,5])
bias, linearTerms = trueW[0], trueW[1:]
points = [tuple(v) + (dot(linearTerms, v) + bias + noise(),) for v in [numpy.random.random(5) for _ in range(100)]]
print(bestLinearEstimatorMV(points)[0])
