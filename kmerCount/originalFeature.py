__author__ = 'Haohan Wang'

import numpy as np

import sys

def originalCalculate(s):
    d = {'A':[0,0], 'C':[0,1], 'G':[1,0], 'T':[1,1]}
    l = []
    for c in s:
        if c in d:
            l.extend(d[c])
        else:
            l.extend([-1, -1])
    return l


def processingText(filename):
    text = [line.strip() for line in open('/home/haohanw/metagenomics/'+filename)]

    # f = open('/home/haohanw/metagenomics/index2sampleID_'+filename[:-6]+'.txt', 'w')
    # names = []
    data = []

    c = -1
    for i in range(len(text)):
        if i % 4 == 0:
            c += 1
            # f.writelines(str(c) + '\t' + text[i]+'\n')
            # names.append(text[i])
        elif i%4 == 1:
            data.append(originalCalculate(text[i]))
    data = np.array(data).astype(int)
    np.save('/home/haohanw/metagenomics/original/'+filename[:-18], data)
    # return data, names

if __name__ == '__main__':
    filename = sys.argv[1]
    processingText(filename)