import numpy as  np
import pandas as pd

class RSA:
    """
    Parameters
    ----------
    lexicon : `np.array` or `pd.DataFrame`
        Messages along the rows, states along the columns.
    prior : array-like
        Same length as the number of colums in `lexicon`.
    costs : array-like
        Same length as the number of rows in `lexicon`.
    alpha : float
        The temperature parameter. Default: 1.0    
    """
    def __init__(self, lexicon, prior, costs, alpha=1.0):
        self.lexicon = lexicon
        self.prior = np.array(prior)
        self.costs = np.array(costs)
        self.alpha = alpha
        
    def literal_listener(self):
        return rownorm(self.lexicon * self.prior)
    
    def speaker(self):
        lit = self.literal_listener().T
#        lit = pd.DataFrame([[0.0, 1.0], [0.3, 0.7]], index=['h', 'g'], columns=['r1', 'r2']).T
        utilities = self.alpha * safelog(lit) - self.costs        
        return rownorm(np.exp(utilities))
        
    def listener(self):
        spk = self.speaker().T
#        spk = pd.DataFrame([[1.0, 0.0], [0.25, 0.75], [0, 1]], index=['r1', 'r2', 'r3'], columns=['h', 'g']).T
        return rownorm(spk * self.prior)    
    
def rownorm(mat):
    """Row normalization of np.array or pd.DataFrame"""
    return (mat.T / mat.sum(axis=1)).T

def safelog(vals):
    """Silence distracting warnings about log(0)."""
    with np.errstate(divide='ignore'):
        return np.log(vals)    



msgs = ['riot', 'violent', 'energetic']
states = ['pve', 'pv~e', 'pe~v']
lex = pd.DataFrame([[1., 0., 0.], [1., 1., 0.], [1., 0., 1.]], index=msgs, columns=states)
mod1 = RSA(
    lexicon=lex,
    prior=[0.95, 0.04, 0.01],
    costs=[0., 0., -5.],
    alpha=1)
print mod1.literal_listener()
print mod1.speaker()
#print mod1.listener()
quit()

# q1 
lex = pd.DataFrame([[1.0, 1.0], [1.0, 0.0]], index=msgs, columns=states)
mod1 = RSA(lexicon=lex, prior=[0.9, 0.1], costs=[0.0,0.0], alpha=5)
print mod1.speaker()


# q4
lex = pd.DataFrame(
    [[0,0], [0,0], [0,0]],
    index=[1,2,3],
    columns=['h','g'])

mod = RSA(lexicon=lex, prior=[0.7, 0.2, 0.1], costs=[0,0])
print mod.listener()
        





