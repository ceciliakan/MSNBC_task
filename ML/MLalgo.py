#!/usr/bin/env python

import numpy as np
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import log_loss, confusion_matrix
from sklearn.utils.class_weight import compute_sample_weight
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier

np.set_printoptions(suppress=True)

# supervised KNN
def supvKNN(n_neighbours, trainData, trainLb, testData, testLb):
    neigh = KNeighborsClassifier(n_neighbours, p=2)
    neigh.fit(trainData, trainLb)
    confidence = neigh.predict_proba(testData)
    mean_accur = neigh.score(testData, testLb)

    sampleW = genSampWeight(testLb)
    logLoss = log_loss(testLb, confidence, sample_weight=sampleW)
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

def randForest(trainData, trainLb, testData, testLb):
    sampleW = genSampWeight(testLb)

    clf = RandomForestClassifier(n_estimators=60, criterion="entropy", max_depth=1000, \
     min_samples_leaf=5, class_weight='balanced')
    clf.fit(trainData, trainLb)
    mean_accur = clf.score(testData,testLb, sample_weight = sampleW)
    confidence = clf.predict_proba(testData)
    logLoss = log_loss(testLb, confidence)
    confusMat = confusion_matrix( testLb, clf.predict(testData), sample_weight=sampleW )

    print mean_accur
    print logLoss
    print confusMat
    '''
    ada_clf = AdaBoostClassifier(clf)
    ada_clf.fit(trainData, trainLb)
    ada_mean_accur = ada_clf.score(testData,testLb, sample_weight = sampleW)
    ada_confidence = ada_clf.predict_proba(testData)
    ada_logLoss = log_loss(testLb, ada_confidence)
    ada_confusMat = confusion_matrix( testLb, ada_clf.predict(testData), sample_weight=sampleW )
    '''
    return logLoss, mean_accur, confusMat, confidence