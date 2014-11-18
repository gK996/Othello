
"""
Short test file for Project 2, Othello. 

We do not claim that this file is a complete testing scheme: 
its primary purpose is to check the spelling of the function names. 
You should supplement the tests in this file with your own tests. 
The correctness of your program is your responsibility. 

Author: Lyndon While 
Date: 4/5/14
Version 1.03
"""


import copy
import Othello


def onesort(xs):
    xs.sort()
    return xs

def allsort(xs):
    for k in range(len(xs)):
        xs[k][2].sort()
    xs.sort()
    return xs


def test_initialiseBoard():
    b = [0,0,0,0,0,0]
    return [(project2.initialiseBoard(x), y) for (x, y) in 
            [(6, [b, b, [0,0,1,-1,0,0], [0,0,-1,1,0,0], b, b])]]

def test_drawBoard():
    return []

def test_move():
    b = [[2, -1, 0, 0], [0, -3, -2, -1], [0, 0, -1, 0], [0, -1, 2, 0]]
    c = [[2,  2, 1, 0], [0, -3,  3, -1], [0, 0,  2, 0], [0, -1, 2, 0]]
    project2.move(b, (0, 2, [(1, 0), (0, -1)]), 1)
    return [(b, c)]

def test_legalDirection():
    b = [[2, -1, 0, 0], [0, -3, -2, -1], [0, 0, -1, 0], [0, 0, 2, 0]]
    return [(project2.legalDirection(r, c, b, p, u, v), y) for (r, c, b, p, u, v, y) in 
            [(0, 2, b,  1,  0, -1, True),
             (3, 0, b, -1, -1,  1, False),
             (0, 3, b, -1,  1,  0, False),
             (0, 3, b, -1, -1,  0, False)]]

def test_legalMove():
    b = [[2, -1, 0, 0], [0, -3, -2, -1], [0, 0, -1, 0], [0, 0, 2, 0]]
    return [(onesort (project2.legalMove(r, c, b, p)), y) for (r, c, b, p, y) in 
            [(0, 2, b,  1, [(0, -1), (1, 0)]),
             (3, 0, b, -1, []),
             (0, 3, b,  1, []),
             (0, 3, b, -1, [])]]

def test_moves():
    b = [[0,1,-1,0], [-2,1,-2,0], [0,1,-2,0], [0,-1,-2,-2]]
    c = [[1] * 6, [1,1,-1,-1,-1,1], [1,1,-1,0,-1,1], [1,1,-1,-1,-1,1], [1] * 6, [1] * 6]
    return [(allsort (project2.moves(b, p)), y) for (b, p, y) in 
            [(b,  1, [(0, 3, [(0,-1), (1,-1)]), (1, 3, [(0,-1)]), (2, 3, [(-1,-1), (0,-1)])]),
             (b, -1, [(0, 0, [(0, 1), (1, 1)]), (2, 0, [(-1,1), (0,1)]), (3, 0, [(-1,1)])]),
             (c,  1, [(2, 3, [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)])]),
             (c, -1, [])]]

def test_selectMove():
    return []

def test_scoreBoard():
    return [(project2.scoreBoard(b), x) for (b, x) in
            [([[0,1,-3,1], [-2,0,2,-1], [1,3,4,-1], [0,-2,-2,1]], (13, 11))]]

def test_main():
    return []


def msg(f, z):
    bs = [x == y for (x, y) in z]
    if bs == []:
        s = "untested"
    elif all(bs):
        s = "all " + str(len(bs)) + " test(s) correct"
    else:
        zs = [k for k in range(len(bs)) if not bs[k]]
        s = "These tests incorrect: " + str(zs)[1:-1]
    print("%20s" % (f + ":"), s)

msg("initialiseBoard",    test_initialiseBoard())
msg("drawBoard",          test_drawBoard())
msg("move",               test_move())
msg("legalDirection",     test_legalDirection())
msg("legalMove",          test_legalMove())
msg("moves",              test_moves())
msg("selectMove",         test_selectMove())
msg("scoreBoard",         test_scoreBoard())
msg("main",               test_main())
print()
input("Hit Enter to finish: ")

