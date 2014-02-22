#!/bin/env python

import math

samples = 1024
amplitudes = (63000, 0, 20000, 0, 20000)

max = 0
min = 0

for i in range(samples):
    sample = 0.0
    for harmonic, amplitude in enumerate(amplitudes):    
        sample += math.sin(math.pi*2*i*(harmonic+1)/samples) * amplitude / 2
    sample = int(sample)
    if sample > max:
        max = sample
    elif sample < min:
        min = sample
    print "%d," % sample,
    if i % 10 == 9:
        print

print
print 'Range is:', min, max

if max > 32767 or min < -32768:
    print "Invalid range!"
        
