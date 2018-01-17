#!/usr/bin/env python

import numpy as np
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import log_loss, confusion_matrix
from sklearn.utils.class_weight import compute_sample_weight

np.set_printoptions(suppress=True)

# supervised KNN
def supvKNN(n_neighbours, trainData, trainLb, testData, testLb):
    neigh = KNeighborsClassifier(n_neighbours, p=2)
    neigh.fit(trainData, trainLb)
    confidnce = neigh.predict_proba(testData)
    mean_accur = neigh.score(testData, testLb)

    sampleW = genSampWeight(testLb)
    logLoss = log_loss(testLb, confidnce, sample_weight=sampleW)
    confusMat = confusion_matrix(testLb, neigh.predict(testData), sample_weight=sampleW)

    print mean_accur
    print logLoss
    print confusMat

    return logLoss, mean_accur, confusMat

def supVectMach(trainData, trainLb, testData, testLb):
    clf = SVC() #probability='True')
    clf.fit(trainData, trainLb)
    mean_accur = clf.score(testData, testLb)
    #confidnce = clf.predict_proba(testData)
    logLoss = 1 #log_loss(testLb, confidnce)
    print mean_accur

    return logLoss, mean_accur

def genSampWeight(tData_lb):
    sample_weight_vect = compute_sample_weight(class_weight='balanced', y=tData_lb)
    return sample_weight_vect