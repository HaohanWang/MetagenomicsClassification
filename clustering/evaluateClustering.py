__author__ = 'Haohan Wang'

from sklearn.metrics import adjusted_rand_score as ars

import operator

def matchClusteringLabels(filename):
    text = [line.strip() for line in open('/home/haohanw/metagenomics/clusteringResult_'+filename+'_filterMouse.txt')]

    result1 = {}
    for line in text:
        items = line.split('\t')
        result1[items[0][1:]] = int(items[1])

    rs1 = []
    rs2 = []
    text = [line.strip() for line in open('/home/haohanw/metagenomics/Kaiju/'+filename+'.label')]
    result2 = {}
    for line in text:
        items = line.split('\t')
        rs1.append(int(items[1]))
        rs2.append(result1[items[0]])
        result2[items[0]] = int(items[1])

    print 'organizing results, now calculating'

    a = ars(rs1, rs2)
    print 'final score', abs(a)

    f = open('/home/haohanw/metagenomics/clusteringCompare_'+filename+'.txt', 'w')

    sorted_result1 = sorted(result1.items(), key=operator.itemgetter(1))
    for (n, v) in sorted_result1:
        if n in result2:
            f.writelines(n+'\t'+str(v)+'\t'+str(result2[n]) + '\n')
    f.close()

if __name__ == '__main__':
    filename = 'mellon_high_contamination_1'
    matchClusteringLabels(filename)
