# A first attempt at coding a proof assistant.

#special operator symbols

implies = '→'
neg = '¬'
#truth = '⊤'

l,r = '(', ')'

# axioms

# x0→(x1→x0)
a0 = 'x0'+implies+l+'x1'+implies+'x0'+r

# (x0→(x1→x2))→((x0→x1)→(x0→x2))
a1 = l+'x0'+implies+l+'x1'+implies+'x2'+r+r+implies+l+l+'x0'+implies+'x1'+r+implies+l+'x0'+implies+'x2'+r+r

# (¬x0→¬x1)→(x0→x1)
a2 = l+neg+'x0'+implies+neg+'x1'+r+implies+l+'x0'+implies+'x1'+r

# inference
follows = '⊢'

i0 = '['+'x0'+ ','+ 'x0'+implies+'x1'+']'+follows+'x1'


# sugar

conj = '∧'
disj = '∨'

sugar = {
    neg+'x0'+implies+'x1' : 'x0'+disj+'x1', 
    neg+l+'x0'+implies+neg+'x1'+r : 'x0'+conj+'x1'} 


def extract_variables(string, var_names):
    pass