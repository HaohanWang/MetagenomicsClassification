__author__ = 'Haohan Wang'

from sklearn.metrics import adjusted_rand_score as ars

def matchClusteringLabels(filename):
    text = [line.strip() for line in open('/home/haohanw/metagenomics/clusteringResult_'+filename+'_filterMouse.txt')]

    result = {}
    for line in text:
        items = line.split('\t')
        result[items[0][1:]] = int(items[1])

    rs1 = []
    rs2 = []
    text = [line.strip() for line in open('/home/haohanw/metagenomics/Kaiju/'+filename+'.label')]
    for line in text:
        items = line.split('\t')
        rs1.append(int(items[1]))
        rs2.append(result[items[0]])

    print 'organizing results, now calculating'

    a = ars(rs1, rs2)
    print 'final score', abs(a)

if __name__ == '__main__':
    filename = 'mellon_high_contamination_1'
    matchClusteringLabels(filename)
