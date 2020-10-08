#!/usr/bin/python
import random

pB = 0.9          # model parameters: P(B)
pRB = 0.9         # P(R|B)
pIB = 0.95        # P(I|B)
pG = 0.95         # P(G)
pSIG = 0.99       # P(S|I,G)
pMS = 0.99        # P(M|S)

N = 100000        # number of generated tuples

class Monikko:
    [B, R, I, G, S, M] = [False, False, False, False, False, False]
    
heap = []           # generated tuples are collected to this heap
for i in range(N):
    m = Monikko()
    if random.random() < pB: m.B = True
    if m.B and random.random() < pRB: m.R = True
    if m.B and random.random() < pIB: m.I = True
    if random.random() < pG: m.G = True
    if m.I and m.G and random.random() < pSIG: m.S = True
    if m.S and random.random() < pMS: m.M = True
    heap.append(m)

# calculate tuples, where following conditions hold ('and')
cnotM = len([m for m in heap if not m.M]) # S = 0
cnotBnotM = len([m for m in heap if not m.B and not m.M]) # S = 0, B = 0
cnotGnotM = len([m for m in heap if not m.G and not m.M]) # M = 0, G = 0

# print the approximate values of conditional probabilities
print 'P[not B | not M]: %.1f%%' % (100. * cnotBnotM / cnotM)
print 'P[not G | not M]: %.1f%%' % (100. * cnotGnotM / cnotM)

# and continue and the same way with the next conditions
cnotS = len([m for m in heap if not m.S]) # S = 0
cBnotS = len([m for m in heap if m.B and not m.S])
cGnotS = len([m for m in heap if m.G and not m.S])
cBGnotS = len([m for m in heap if m.B and m.G and not m.S])
cGRIS = len([m for m in heap if m.G and m.R and m.I and m.S])
cGRI = len([m for m in heap if m.G and m.R and m.I])
cBG = len([m for m in heap if m.B and m.G])

print 'P[B | not S]: %.1f%%' % (100. * cBnotS / cnotS)
print 'P[B | not S, G]: %.1f%%' % (100. * cBGnotS / cGnotS)
print 'P[not S | B, G]: %.1f%%' % (100. * cBGnotS / cBG)
print 'P[S | R, I, A]: %.1f%%' % (100. * cGRIS / cGRI)

cBRGnotS = len([m for m in heap if m.B and m.R and m.G and not m.S])
cRGnotS = len([m for m in heap if m.R and m.G and not m.S])
cSnotRIG = len([m for m in heap if m.S and not m.R and m.I and m.G])
cnotRIG = len([m for m in heap if not m.R and m.I and m.G])

print '1.\nP[B | R, G, not S]: %d / %d ~= %.1f%%' % \
    (cBRGnotS, cRGnotS, (100. * cBRGnotS / cRGnotS))
print '2.\nP[S | R, I, G]: %d / %d ~= %.1f%%' % (cGRIS, cGRI, (100. * cGRIS / cGRI))
print '3.\nP[S | not R, I, G]: %d / %d ~= %.1f%%' % \
    (cSnotRIG, cnotRIG, (100. * cSnotRIG / cnotRIG))
