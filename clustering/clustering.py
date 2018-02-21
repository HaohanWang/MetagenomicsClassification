__author__ = 'Haohan Wang'

import sys
sys.path.append('../')

from sklearn.cluster import KMeans

from kmerCount.kmerCount import *

def clustering(filename):
    data, names = processingText(filename)

    km = KMeans(n_clusters=300)
    labels = km.fit_predict(data)

    f = open('/home/haohanw/metagenomics/clusteringResult_'+filename[:-6]+'.txt', 'w')
    for i in range(len(names)):
        f.writelines(names[i]+'\t'+str(labels[i])+'\n')
    f.close()

if __name__ == '__main__':
    filename = 'smith_low_contamination_25_filterMouse.fastq'
    clustering(filename)

