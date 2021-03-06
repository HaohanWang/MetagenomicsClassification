__author__ = 'Haohan Wang'

import numpy as np

def extractingLabels():
    # filenames = ['mellon_low_contamination_1', 'mellon_low_contamination_2', 'mellon_low_contamination_3',
    #              'mellon_low_contamination_4', 'mellon_low_contamination_5', 'mellon_low_contamination_6',
    #              'mellon_low_contamination_7', 'mellon_low_contamination_8', 'mellon_low_contamination_9']

    filenames = ['mellon_high_contamination_1', 'mellon_high_contamination_2', 'mellon_high_contamination_3',
                 'mellon_high_contamination_4']

    m = {}

    for filename in filenames:

        text = [line.strip() for line in open('/home/haohanw/metagenomics/Kaiju/' + filename + '.kaiju.assign')]

        f = open('/home/haohanw/metagenomics/Kaiju/' + filename + '.label', 'w')

        for line in text:
            items = line.split('\t')
            c = items[0]
            k = items[1]
            l = items[2]
            if c == 'C':
                o = items[4]
                if len(o.split(',')) <= 2:
                    if l not in m:
                        m[l] = len(m)
                    f.writelines(k + '\t' + str(m[l]) + '\n')

        f.close()
    np.save('/home/haohanw/metagenomics/Kaiju/'+filenames[0][:-2], m)


if __name__ == '__main__':
    extractingLabels()
