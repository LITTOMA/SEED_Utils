from sys import *
from struct import pack,unpack
import os

if len(argv)<2:
    print 'Usage: info2db seedinfo.bin'

tids = []
seeds = []
with open(argv[1],'rb')as seedinfo:
    if not seedinfo.read(4) == 'SEED':
        print 'Input file invalid.'
        exit()
    count = unpack('I',seedinfo.read(4))[0]
    for i in range(count):
        tids.append(seedinfo.read(8))
    for i in range(count):
        seeds.append(seedinfo.read(16))

with open(os.path.split(argv[1])[0]+'\\seeddb.bin','wb')as seeddb:
    seeddb.write(pack('I',count))
    while not seeddb.tell()%16 == 0:
        seeddb.write('\x00')
    for i in range(count):
        seeddb.write(tids[i])
        seeddb.write(seeds[i])
        while not seeddb.tell()%16 == 0:
            seeddb.write('\x00')
