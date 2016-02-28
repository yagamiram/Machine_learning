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
