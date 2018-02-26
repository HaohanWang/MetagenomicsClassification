__author__ = 'Haohan Wang'

import numpy as np
import sys

def recoverMapping(dataCate):
    rd = np.load('/home/haohanw/metagenomics/Kaiju/'+dataCate + '_contamination.npy').item()
    d = {}
    for k in rd:
        d[int(rd[k])] = int(k)
    return d

def collectPredictionResults(dataCate):
    if dataCate == 'mellon_high':
        dataSet = xrange(1, 5)
    elif dataCate == 'mellon_low':
        dataSet = xrange(1, 10)
    elif dataCate == 'smith_low':
        dataSet = xrange(1, 30)
    else:
        dataSet = []

    mappingDic = recoverMapping(dataCate)

    for ind in dataSet:
        result = {}
        text = [line.strip() for line in open('predictionResult_'+ dataCate + '_ico_' + str(ind) + '.txt')]
        for line in text:
            items = line.split('\t')
            result[items[0]] = mappingDic[int(items[1])]

        text = [line.strip() for line in open('/home/haohanw/metagenomics/Kaiju/' + dataCate + '_contamination_' + str(ind) + '.kaiju.assign')]

        f = open('/home/haohanw/metagenomics/Kaiju/prediction_' + dataCate + '_' + str(ind) + '.txt', 'w')

        for line in text:
            written = False
            items = line.split('\t')
            c = items[0]
            k = items[1]
            l = items[2]
            if c == 'C':
                o = items[4]
                if len(o.split(',')) <= 2:
                    f.writelines(k + '\t' + l + '\n')
                    written = True
            if not written:
                f.writelines(k+'\t'+result[k]+'\n')

        f.close()

if __name__ == '__main__':
    dataCate = sys.argv[1]
    collectPredictionResults(dataCate)