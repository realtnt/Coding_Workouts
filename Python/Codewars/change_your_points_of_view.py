'''
    
codewars

6 kyu

Change your Points of View
    
'''


def point(a, b):
    def func(): return (a, b)
    func.x = a
    func.y = b
    return func


def fst(pt):
    return pt.x


def snd(pt):
    return pt.y


def sqr_dist(pt1, pt2):
    return (fst(pt2)-fst(pt1))**2 + (snd(pt2)-snd(pt1))**2


def line(pt1, pt2):
    l = snd(pt1) - snd(pt2)
    m = fst(pt2) - fst(pt1)
    n = fst(pt1) * snd(pt2) - fst(pt2)*snd(pt1)
    return [l, m, n]
