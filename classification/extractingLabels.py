__author__ = 'Haohan Wang'

def extractingLabels():

    filenames = ['mellon_high_contamination_1', 'mellon_high_contamination_2', 'mellon_high_contamination_3', 'mellon_high_contamination_4']

    m = {}

    for filename in filenames:

        text = [line.strip() for line in open('/home/haohanw/metagenomics/Kaiju/'+filename+'.kaiju.assign')]

        f = open('/home/haohanw/metagenomics/Kaiju/'+filename+'.label', 'w')

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

if __name__ == '__main__':
    extractingLabels()