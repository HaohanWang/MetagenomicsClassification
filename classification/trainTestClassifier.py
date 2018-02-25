__author__ = 'Haohan Wang'

import sys

import numpy as np

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def constructData(dataset, dataCate, featureCate):
    data = None
    Ls = []
    for ind in dataset:
        if featureCate == 'kmer':
            features = np.load('/home/haohanw/metagenomics/kmer/'+dataCate + '_contamination_' + str(ind) + '.npy')
        else:
            features = np.load('/home/haohanw/metagenomics/ico/'+dataCate + '_contamination_' + str(ind) + '.npy')

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
        features = features[idx, :]
        if data is None:
            data = features
        else:
            data = np.append(data, features, 0)
        Ls.extend(label)

    Ls = np.array(Ls)

    return data, Ls

def trainValidate(dataCate, featureCate):
    if dataCate == 'mellon_high':
        trainSet = [1, 2]
        testSet = [3, 4]
    elif dataCate == 'mellon_low':
        trainSet = [1, 2, 3, 4]
        testSet = [5, 6, 7, 8, 9]
    elif dataCate == 'smith_low':
        trainSet = xrange(1, 11)
        testSet = xrange(11, 29)
    else:
        trainSet = []
        testSet = []

    data, label = constructData(trainSet, dataCate, featureCate)

    model = SVC(class_weight='balanced', max_iter=10000)
    model.fit(data, label)

    del data
    del label

    data, label = constructData(testSet, dataCate, featureCate)

    predL = model.predict(data)
    accu = accuracy_score(label, predL)

    f = open(dataCate + '_' + featureCate + '_result.txt', 'w')
    f.writelines(str(accu)+'\n')
    f.close()

if __name__ == '__main__':
    dataCate = sys.argv[1]
    featureCate = sys.argv[2]
    trainValidate(dataCate, featureCate)
