__author__ = 'Haohan Wang'

import sys

import numpy as np

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def trainingEnsemble(data, label):
    batchSize = 10000
    s = data.shape[0]
    nb = s/batchSize
    l = []
    for i in range(nb):
        model = SVC(class_weight='balanced', max_iter=10000)
        dataTmp = data[i*batchSize:(i+1)*batchSize,:]
        labelTmp = label[i*batchSize:(i+1)*batchSize]
        model.fit(dataTmp, labelTmp)
        l.append(model)
    return l

def predictingEnsemble(data, lm):
    from scipy import stats

    result = None
    for i in range(len(lm)):
        if i == 0:
            result = np.array(lm[i].predict(data))
        else:
            result = np.append(result, np.array(lm[i].predict(data), 1))
    predict = stats.mode(result, 1)[0].reshape(result.shape[0])
    return predict



def constructData(ind, dataCate, featureCate):
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

    s2label = {}
    sample2label = [line.strip() for line in open('/home/haohanw/metagenomics/Kaiju/'+dataCate+'_contamination_'+str(ind)+'.label')]
    for line in sample2label:
        items = line.split('\t')
        label.append(int(items[1]))
        idx.append(sample2ind[items[0]])
        s2label[items[0]] = 0

    idx = np.array(idx)
    data = features[idx, :]

    label = np.array(label)

    remainingLabels = []
    remainingIdx = []
    for line in ind2sample:
        items = line.split('\t')
        k = items[1][1:]
        ind = items[0]
        if k not in s2label:
            remainingIdx.append(ind)
            remainingLabels.append(k)

    reData = features[np.array(remainingIdx),:]

    return data, label, reData, remainingLabels

def trainValidate(dataCate, featureCate):
    if dataCate == 'mellon_high':
        dataSet = xrange(1, 5)
    elif dataCate == 'mellon_low':
        dataSet = xrange(1, 10)
    elif dataCate == 'smith_low':
        dataSet = xrange(1, 30)
    else:
        dataSet = []

    for ind in dataSet:
        f = open('predictionResult_'+ dataCate + '_' + featureCate + '_' + str(ind) + '.txt', 'w')
        data, label, reData, reLabels = constructData(ind, dataCate, featureCate)

        lm = trainingEnsemble(data, label)

        predL = predictingEnsemble(reData, lm)

        for i in range(len(reLabels)):
            f.writelines(reLabels[i]+'\t' + str(predL[i]) + '\n')

        f.close()

if __name__ == '__main__':
    dataCate = sys.argv[1]
    featureCate = sys.argv[2]
    trainValidate(dataCate, featureCate)
