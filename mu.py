# Implementation of the mu puzzle in Doublas Hofstadter's Godel Escher Bach

import re

# symbols
M, I, U = 'M', 'I', 'U'

symbols = M, I, U

# Axioms
axioms = ['MI']


def i0(s):
    '''Add U at the end of a string ending in I'''
    if s[-1] == I:
        return [s+U]
    else:
        return []

def i1(s):
    '''Double the string after the M'''
    if s[0] == M:
        return [M + s[1:]*2]
    else:
        return []

def i2(s):
    '''Replace any III with a U'''
    for match in re.finditer('(?=III)', s):
        start = match.start()
        end = start+3
        yield s[:start]+U+s[end:]

def i3(s):
    '''Remove any UU'''
    for match in re.finditer('(?=UU)', s):
        start = match.start()
        end = start+2
        yield s[:start]+s[end:]

rules = [i0, i1, i2, i3]

def explore(axioms, rules, max_depth=50):
    '''Breadth first exploration'''
    known_truths = set(axioms)
    edge = set(known_truths)
    for i in range(max_depth):
        working_edge = set(edge)
        edge.clear()
        while len(working_edge)>0:
            # pop a statement from the edge
            s = working_edge.pop()
            # move it to known truths
            known_truths.add(s)
            # get all sons of this statement
            sons = set()
            for rule in rules:
                for son in rule(s):
                    sons.add(son)
            # check if any of these are new
            for son in sons:
                if son not in known_truths:
                    if son not in working_edge:
                        edge.add(son)
        yield edge




for edge in explore(axioms, rules, 5):
    print(edge)
quit()



