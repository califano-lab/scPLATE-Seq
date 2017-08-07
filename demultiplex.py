import sys, getopt
from collections import defaultdict


workDir = ''
barcodeInfo = ''
seqFastq = ''
barcodeFastq = ''
prefix=''
#define arguments
opt, args = getopt.getopt(sys.argv[1:], 'd:i:s:b:p', ['workDir=',
                                                    'barcodeInfo=',
                                                    'seqFastq=',
                                                    'barcodeFastq=',
                                                    'prefix='])
#read arguments
for o, a in opt:
    if o in ('-d', '--workDir'):
        workDir = a
    elif o in ('-i', '--barcodeInfo'):
        barcodeInfo = a
    elif o in ('-s', '--seqFastq'):
        seqFastq = a
    elif o in ('-b', '--barcodeFastq'):
        barcodeFastq = a
    elif o in ('-p', '--prefix'):
        prefix = a
# pass arguments
print("-" * 20)
print("Job Infomation")
print("-" * 20)
print("workDir      : %s" % workDir)
print("barcodeInfo  : %s" % barcodeInfo)
print("seqFastq     : %s" % seqFastq)
print("barcodeFastq : %s" % barcodeFastq)
print("prefix       : %s" % prefix)
print("\n")
########
#working directory and files
########

print("Reading barcodeInfo...")
print("\n")
BARCODE = []
SAMPLE = []
f = open(barcodeInfo)
for line in f:
    BARCODE.append(line.split()[0])
    SAMPLE.append(line.split()[1])
f.close()
########
#barcodeInfo
########

print("Reading .fastq...")
print("\n")
barcode_dict = defaultdict(list)
bf = open(barcodeFastq)
sf = open(seqFastq)
while True:
    bl1 = bf.readline()
    sl1 = sf.readline()
    if not bl1: break #EOF
    bl2 = bf.readline()
    sl2 = sf.readline()
    bl3 = bf.readline()
    sl3 = sf.readline()
    bl4 = bf.readline()
    sl4 = sf.readline()
    if bl2[0:8] in BARCODE:
        barcode_dict[SAMPLE[BARCODE.index(bl2[0:8])]].append(sl1.rstrip()+'\n'+bl2[8:16].rstrip()+sl2.rstrip()+'\n'+sl3.rstrip()+'\n'+bl4[8:16].rstrip()+sl4.rstrip()+'\n')
bf.close()
sf.close()
#########
#.fastq files
#########
print("Demultiplexing .fastq...")
print("\n")
for f in SAMPLE:
    o = open(workDir+prefix+f+'.fastq', 'w')
    if barcode_dict.get(f):
        for i in barcode_dict.get(f):
            o.write(i)
    o.closed
print("Finished")
#########
#demultiplexing
#########
