class Theorem(object):

    def __init__(self, string, parent):
        self.s = string
        self.parent = parent

    def __eq__(self, other):
        return self.s == other.s

    def __le__(self, other):
        if self.s == self.other:
            return True
        else self < other 
    
    def __lt__(self, other):
        return self in proof(other)

    def __ge__(self, other):
        return other <= self

    def __gt__(self, other):
        return  other < self

    def proof(self):
        proof = []
        current = self
        while type(current.parent) is not None:
            current = current.parent
            proof.append(current.s)
        return proof[::-1]

    def sons(self, rules):
        ''' Generator of all sons'''
        for rule in rules:
            for son in rule(self.s):
                yield Theorem(son, self)

class Axiom(Theorem):

    def __init__(self, string):
        Theorem.__init__(self, string, None)

    def __repr__(self):
        return 'Axiom({})'.format(self.s)