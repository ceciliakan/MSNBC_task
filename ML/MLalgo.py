#!/usr/bin/env python

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import log_loss

# supervised KNN
def supvKNN(n_neighbours, trainData, trainLb, testData, testLb):
    neigh = KNeighborsClassifier(n_neighbours)
    neigh.fit(trainData, trainLb)
    confidnce = neigh.predict_proba(testData)
    mean_accur = neigh.score(testData, testLb)

    logLoss = log_loss(testLb, confidnce)

    print mean_accur
    print logLoss

    return logLoss, mean_accur

def supVectMach(trainData, trainLb, testData, testLb):
    clf = SVC()
    clf.fit(trainData, trainLb)
    mean_accur = clf.score(testData, testLb)
    print mean_accur

    return mean_accur