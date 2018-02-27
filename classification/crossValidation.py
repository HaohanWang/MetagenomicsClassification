__author__ = 'Haohan Wang'

import sys

import numpy as np

from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

def constructData(ind, dataCate, featureCate):
    if featureCate == 'kmer':
        features = np.load('/home/haohanw/metagenomics/kmer/'+dataCate + '_contamination_' + str(ind) + '.npy')
    elif featureCate == 'ico':
        features = np.load('/home/haohanw/metagenomics/ico/'+dataCate + '_contamination_' + str(ind) + '.npy')
    else:
        features = np.load('/home/haohanw/metagenomics/original/'+dataCate + '_contamination_' + str(ind) + '.npy')

    sample2ind = {}
    ind2sample = [line.strip() for line in open('/home/haohanw/metagenomics/index2sampleID_'+dataCate + '_contamination_'+str(ind)+'_filterMouse.txt')]
    for line in ind2sample:
        items = line.split('\t')
        sample2ind[items[1][1:]] = int(items[0])

    idx = []
    label = []

    sample2label = [line.strip() for line in open('/home/haohanw/metagenomics/Kaiju/'+dataCate+'_contamination_'+str(ind)+'.label')]
    for line in sample2label:
        items = line.split('\t')
        label.append(int(items[1]))
        idx.append(sample2ind[items[0]])

    idx = np.array(idx)
    data = features[idx, :]

    label = np.array(label)

    return data, label

def crossValidate(dataCate, featureCate, modelCate):
    if dataCate == 'mellon_high':
        dataSet = xrange(1, 5)
    elif dataCate == 'mellon_low':
        dataSet = xrange(1, 10)
    elif dataCate == 'smith_low':
        dataSet = xrange(1, 30)
    else:
        dataSet = []

    if modelCate == 'nb':
        model = GaussianNB()
    elif modelCate == 'lr':
        model = LogisticRegression(class_weight='balanced')
    else:
        model = SVC(class_weight='balanced', max_iter=10000)


    f = open(dataCate + '_' + featureCate + '_' + modelCate + '_result.txt', 'w')
    for ind in dataSet:
        data, label = constructData(ind, dataCate, featureCate)

        scores = cross_val_score(model, data, label, cv=5)

        f.writelines(str(ind) + '\t' + str(scores)+'\n')

    f.close()

if __name__ == '__main__':
    dataCate = sys.argv[1]
    featureCate = sys.argv[2]
    modelCate = sys.argv[3]
    crossValidate(dataCate, featureCate, modelCate)
