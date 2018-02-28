__author__ = 'Haohan Wang'

from matplotlib import pyplot as plt
import numpy as np

def loadData():
    featureNames = ['original', 'kmer', 'ico']
    modelNames = ['nb', 'svc']
    names = {'original':'seq', 'kmer':'kMer', 'ico':'ICO', 'nb':'NB', 'svc':'SVM'}

    result = {}
    for fn in featureNames:
        for mn in modelNames:
            data = []
            text = [line.strip() for line in open('../results/mellon_high_'+fn+'_'+mn+'_result.txt')]
            for line in text:
                items = line.split()
                q1 = float(items[-3][1:])
                q2 = float(items[-2])
                q3 = float(items[-1][:-1])
                d  =[q1, q2, q3]
                data.append(d)

            result[names[fn]+'_'+names[mn]] = data

    return result

def visualize():
    fns = ['seq', 'kMer', 'ICO']
    mns = ['NB', 'SVM']

    result = loadData()

    colors = ['b', 'c', 'navy', 'violet', 'm', 'r']
    ecolors = ['y', 'darkorange', 'yellow', 'greenyellow', 'springgreen', 'g']
    fig = plt.figure(dpi=350, figsize=(12, 9))

    axs = [0 for i in range(4)]

    c = -1

    for j in [1, 0]:
        for i in [0, 1]:
            c += 1
            axs[c] = fig.add_axes([0.1+i*0.45, 0.05+j*0.42, 0.4, 0.37])

            colorCount = -1
            for mi in range(2):
                for fi in range(3):
                    colorCount += 1
                    d = result[fns[fi]+'_'+mns[mi]][c]
                    m = np.mean(d)
                    s = np.std(d)
                    axs[c].bar(colorCount, m, width=1, color=colors[colorCount], yerr=s, label=fns[fi]+'_'+mns[mi], ecolor=ecolors[colorCount])


            axs[c].title.set_text('mellon_high_contamination_' + str(c+1))

            # axs[c].set_xlim(-0.01, 1)
            axs[c].set_ylim(0, 1)

            axs[c].set_ylabel('Accuracy')
            axs[c].get_xaxis().set_visible(False)

    plt.legend(loc="upper center", bbox_to_anchor=(-0.1,2.5), fancybox=True, ncol=6)
    # plt.show()
    plt.savefig('fig.pdf', dpi=350, format='pdf')

if __name__ == '__main__':
    visualize()
