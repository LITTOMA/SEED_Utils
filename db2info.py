from sys import *
from struct import pack,unpack
import os

if len(argv)<2:
    print 'Usage: db2info seeddb.bin'
    
tids = []
seeds = []
with open(argv[1],'rb')as seeddb:
    count = unpack('I',seeddb.read(4))[0]
    seeddb.seek(0x10,0)
    for i in range(count):
        tids.append(seeddb.read(8))
        seeds.append(seeddb.read(16))
        seeddb.seek(8,1)
with open(os.path.split(argv[1])[0]+'\\seedinfo.bin','wb')as seedinfo:
    seedinfo.write('SEED')
    seedinfo.write(pack('I',count))
    for tid in tids:
        seedinfo.write(tid)
    for seed in seeds:
        seedinfo.write(seed)
