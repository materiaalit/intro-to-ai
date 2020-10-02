#!/usr/bin/python
import random

pE = 0.009
pB = 0.0027
pAnotEnotB = 0.0095
pAEnotB = 0.81
pAnotEB = 0.92
pAEB = 0.97

N = 10000000

class Tuple:
    [E, B, A] = [False,False,False]
    
heap = []
for i in range(N):
    m = Tuple()
    if random.random() < pE: m.E = True
    if random.random() < pB: m.B = True
    if not m.E and not m.B and random.random() < pAnotEnotB: m.A = True
    if m.E and not m.B and random.random() < pAEnotB: m.A = True
    if not m.E and m.B and random.random() < pAnotEB: m.A = True
    if m.E and m.B and random.random() < pAEB: m.A = True
    heap.append(m)

cH = len([m for m in heap if m.A])
cRH = len([m for m in heap if m.B and m.A])
cMH = len([m for m in heap if m.E and m.A])
cMRH = len([m for m in heap if m.E and m.B and m.A])

print 'P[B | A]: %d / %d ~= %.1f%%' % (cRH, cH, 100. * cRH / cH)
print 'P[B | E, A]: %d / %d ~=  %.1f%%' % (cMRH, cMH, 100. * cMRH / cMH)
