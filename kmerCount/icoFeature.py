__author__ = 'Haohan Wang'

import numpy as np

def icoCalculate(s):
    mer1 = {}
    mer3 = {}
    mer4 = {}
    for i in range(len(s)):
        k = s[i]
        if k not in mer1:
            mer1[s[i]] = 0.0
        mer1[s[i]] += 1
    for i in range(len(s)-3):
        k = s[i:i+3]
        if k not in mer3:
            mer3[k] = 0.0
        mer3[k] += 1
    for i in range(len(s)-4):
        k = s[i:i+4]
        if k not in mer4:
            mer4[k] = 0.0
        mer4[k] += 1

    for k in mer1:
        mer1[k] = mer1[k]/len(s)
    for k in mer3:
        mer3[k] = mer3[k]/(len(s) - 3)
    for k in mer4:
        mer4[k] = mer4[k]/(len(s) - 4)

    r = []
    for i in range(len(s)-4):
        k4 = s[i:i+4]
        k1 = s[i]
        k3 = s[i+1:i+4]
        if k4 in mer4:
            p4 = mer4[k4]
            p1 = mer1[k1]
            p3 = mer3[k3]
            r.append(p4/(p1*p3))
        else:
            r.append(0)
    return r

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
            data.append(icoCalculate(text[i]))
    data = np.array(data).astype(int)
    np.save('/home/haohanw/metagenomics/ico/'+filename[:-18], data)
    # return data, names

if __name__ == '__main__':
    filename = 'mellon_high_contamination_1_filterMouse.fastq'
    processingText(filename)