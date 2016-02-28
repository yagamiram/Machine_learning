'''
KNN Algorithm : Very simple algorithm if you use euclidean distance

Usually machine learning algorithms does classification the usually classification question is
“is the data linearly separable?”

Unlike other algorithms, KNN is different. 
k-nearest-neighbors and the axiom of neighborliness allow for datasets with many different geometric structures.
Its not needed to be linearly seperable all the time. 

Example: 
Think of datasets as concentric circles.

Link: https://github.com/j2kun/knn/blob/master/concentric-circles-knn.png

The problem is to find in which class a data point falls ?

you have to build a training model from a training data set and using that model
the new data point should be figured where it falls. Easiest way to find is to 
get the euclideam distance between the new data point and each data point in the training model.
Out of that pick the K points that are closer the new point. And from the class labels
of the K points get the label which occurred more.

Below is the running code.

The code is also a example of closure. Check front-end web question github page
to know what is closure in JS. Same goes for python.

Here in this code no training model is built.
Randomly points are picked and labeled to either class 0 or class 1.
To pick the points randomly gaussian distribution is used.
Then to get the K smallest element heap is used.

Code copied from: http://jeremykun.com/2012/08/26/k-nearest-neighbors-and-handwritten-digit-classification/

To know about KNN for hand written digits: https://github.com/j2kun/knn/blob/master/knn-digits.py
The description for the code is : http://jeremykun.com/2012/08/26/k-nearest-neighbors-and-handwritten-digit-classification/
'''
import math
import heapq
import random

'''
Returns the training data randomly picked using gaussian distribution
by passing mean and standard deviation
'''
def gaussCluster(center, stdDev, count=50):
    return [(random.gauss(center[0], stdDev),
             random.gauss(center[1], stdDev)) for _ in range(count)]
'''
The two training sets are combined together
'''
def makeDummyData():
    return gaussCluster((-4,0), 1) + gaussCluster((4,0), 1)

def euclideanDistance(x,y):
    return math.sqrt(sum([(a-b)**2 for (a,b) in zip(x,y)]))

'''
This function returns the classifier fn/object from which the label is found for the new data point.
This funtion returns the function classify [closure is achieved]
Why this has to done ?
What is the use of closure here ?
First closure means you can access the local variables of the funtion even 
when you are out the function.
Here if the function makeKNNClassifier is called with different arguments (arguments with different values)
each time it will return classify function which doesn't interfere the previous created classifier
and there is no big advanatge of this. You don't have to create the same classifier again.

Example:
Normal way :
'''
This fn returns the label for the class
'''
def makeKNNClassifier(data, labels, k, distance):
    closestPoints = heapq.nsmallest(k, enumerate(data), key=lambda y: distance(x, y[1]))
    closestLabels = [labels[i] for (i, pt) in closestPoints]
    return max(set(closestLabels), key=closestLabels.count)
    
When you want to find the label for a new data point you will call like this
makeKNNClassifier(data1, labels1, k1, distance) // with values substituted in the argumets
Now you want a label for the same data point again but with different set of training data, so u will call like this
makeKNNClassifier(data1, labels2, k2, distance2) // with different values substituted in the argumets
now you want to find the label for the same data point again for the first set of value one more time, so u will call the 
same function again which is not the efficient way. it means u are creating the classifier every time
to avoid this closure is used.
'''
def makeKNNClassifier(data, labels, k, distance):
    def classify(x):
        closestPoints = heapq.nsmallest(k, enumerate(data), key=lambda y: distance(x, y[1]))
        closestLabels = [labels[i] for (i, pt) in closestPoints]
        return max(set(closestLabels), key=closestLabels.count)

    return classify

if __name__ == "__main__":
   import sys

   k = sys.argv[1] if len(sys.argv) == 2 else 8

   trainingPoints = makeDummyData() # has 50 points from each class
   trainingLabels = [1] * 50 + [2] * 50  # an arbitrary choice of labeling
   # the funtion classify is returned back
   f = makeKNNClassifier(trainingPoints, trainingLabels, k, euclideanDistance)
   # pass the new data point to the classifier and get the labels
   print f((-3,0))
   print f((3,0))
   print f((0,0))
