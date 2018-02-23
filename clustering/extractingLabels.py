__author__ = 'Haohan Wang'

def extractingLabels(filename):
    text = [line.strip() for line in open('/home/haohanw/metagenomics/Kaiju/'+filename+'.kaiju.assign')]

    m = {}

    f = open('/home/haohanw/metagenomics/Kaiju/'+filename+'.label', 'w')

    for line in text:
        items = line.split('\t')
        c = items[0]
        k = items[1]
        l = items[2]
        if c == 'C':
            if l not in m:
                m[l] = len(m)
            f.writelines(k + '\t' + str(m[l]) + '\n')

    f.close()

if __name__ == '__main__':
    filename = 'mellon_low_contamination_1'
    extractingLabels(filename)