#!/usr/bin/python

import random
import collections
import math
import sys
from util import *

############################################################
# Problem 1: binary classification
############################################################

############################################################
# Problem 1a: feature extraction

def extractWordFeatures(x):
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    pass
    # ### START CODE HERE ###
    wD=collections.defaultdict(float)
    for w in x.split():
        wD[w]+=1
    return wD
    # ### END CODE HERE ###

############################################################
# Problem 1b: stochastic gradient descent

def learnPredictor(trainExamples, testExamples, featureExtractor, numIters, eta):
    '''
    Given |trainExamples| and |testExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of iterations to
    train |numIters|, the step size |eta|, return the weight vector (sparse
    feature vector) learned.

    You should implement stochastic gradient descent.

    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and testExamples
    to see how you're doing as you learn after each iteration.
    '''
    weights = {}  # feature => weight
    # ### START CODE HERE ###
    def predict(x):
        phi=featureExtractor(x)
        if dotProduct(weights,phi)<0.0:
            return -1
        else:
            return 1
    for i in range(numIters):
        for it in trainExamples:
            x,y=it
            phi=featureExtractor(x)
            temp=dotProduct(weights,phi)*y
            if temp < 1:increment(weights,-eta*-y,phi)
        print("Iteration:%s, Training error:%s, Test error:%s"%(i,evaluatePredictor(trainExamples,predict),evaluatePredictor(testExamples,predict)))
    # ### END CODE HERE ###
    return weights

############################################################
# Problem 1c: generate test case

def generateDataset(numExamples, weights):
    '''
    Return a set of examples (phi(x), y) randomly which are classified correctly by
    |weights|.
    '''
    random.seed(42)
    # Return a single example (phi(x), y).
    # phi(x) should be a dict whose keys are a subset of the keys in weights
    # and values can be anything (randomize!) with a nonzero score under the given weight vector.
    # y should be 1 or -1 as classified by the weight vector.
    def generateExample():
        phi = None
        y = None
        # ### START CODE HERE ###
        phi={}
        for item in random.sample(list(weights),random.randint(1,len(weights))):
            phi[item]=random.randint(1,100)
        y=1 if dotProduct(weights,phi)>1 else 0
        # ### END CODE HERE ###
        return (phi, y)
    return [generateExample() for _ in range(numExamples)]

############################################################
# Problem 1e: character features

def extractCharacterFeatures(n):
    '''
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces mapped to their n-gram counts.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that n >= 1.
    '''
    def extract(x):
        pass
        # ### START CODE HERE ###
        rD=collections.defaultdict(int)
        x=x.replace(' ','')
        for i in range(0,len(x)-(n-1)):
            rD[x[i:i+n]]+=1
        return rD
        # ### END CODE HERE ###
    return extract