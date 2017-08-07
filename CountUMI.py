import sys, getopt
from collections import defaultdict
from collections import OrderedDict
sys.path.append("/ifs/scratch/c2b2/ac_lab/hd2326/Python3Lib")
import numpy
import scipy.sparse.csgraph

samFile = ''
umiFile = ''
countFile = ''
lenUMI = ''
hammingThreshold = ''
#define arguments
opt, args = getopt.getopt(sys.argv[1:], 'i:u:c:l:t', ['samFile=',
                                                'umiFile=',                  
                                                'countFile=',
                                                'lenUMI=',
                                                'hammingThreshold='])
#read arguments
for o, a in opt:
    if o in ('-i', '--samFile'):
        samFile = a
    elif o in ('-u', '--umiFile'):
        umiFile = a
    elif o in ('-c', '--countFile'):
        countFile = a
    elif o in ('-l', '--lenUMI'):
        lenUMI = a
    elif o in ('-t', '--hammingThreshold'):
        hammingThreshold = a
# pass arguments
print("-" * 20)
print("Job Infomation")
print("-" * 20)
print("samFile             : %s" % samFile)
print("umiFile             : %s" % umiFile)
print("countFile           : %s" % countFile)
print("lenUMI              : %s" % lenUMI)
print("hammingThreshold    : %s" % hammingThreshold)
print("\n")
########
#working directory and files
########

print("Reading samFile...")
print("\n")
umi_dict = defaultdict(list)
f = open(samFile)
for line in f:
    if not '@' in line:
        umi_dict[line.split()[2].split("_")[0]].append(line.split()[9][0:int(lenUMI)])
        #combine different transcripts from same gene
f.close()
########
#read UMI
########

print("Counting UMI...")
print("\n")
def hammingDistance(s1, s2):
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))
#define hammingDistance
f1 = open(umiFile, 'w')
f2 = open(countFile, 'w')
for k in umi_dict.keys():
    seq = umi_dict.get(k)
    seq = list(OrderedDict.fromkeys(seq))
    #all unique umi sequences
    dist = numpy.zeros(shape = (len(seq), len(seq)))
    for i in range(0, len(seq)):
        for j in range(0, len(seq)):
            if hammingDistance(seq[i], seq[j]) > int(hammingThreshold):
                dist[i, j] = 0
            else:
                dist[i, j] = 1
    #creat adjancency matrix
    umi = scipy.sparse.csgraph.connected_components(dist, directed=False, return_labels=False)
    #number of transcripts, number of disconnected subgraphs in umi sequence space
    count = len(umi_dict.get(k))
    #number of counts, number of unique umi sequences
    f1.write(k+'\t'+str(umi)+'\n')
    f2.write(k+'\t'+str(count)+'\n')
f1.close()
f2.close()
print("Finished")
##########
#count UMI
##########




