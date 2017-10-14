from abc import ABCmeta, abstractproperty, abstractmethod

import numpy as np
import scipy.stats as ss

class MCMC(object):
    ''' MCMC is an abstract base class to define the methods
    and properties that any MCMC (Metropolis Hastings, NUTS, Gibbs)
    should have. It can be initialized/warmed up with an already trained
    MCMC in order to make copies.
    '''
    __metaclass__ = ABCMeta

    def __init__(self, dist, data=None, mcmc=None):
        self.dist = dist
        self.data = data
        self.mcmc = mcmc

    @abstractmethod
    def sample(self, n):
        pass

class MetropolisHastings(MCMC):
    ''' Metropolis Hastings MCMC implementation.
    '''
    def sample(self, n, verbose=True):
        D = len(self.data)
        samples = np.zeros((D, iters))

        # initialize state and log-likelihood
        state = init.copy()
        Lp_state = self.dist.nnlf(state)

        accepts = 0
        for i in np.arange(0, iters):        
        # propose a new state
            prop = np.random.multivariate_normal(state.ravel(), np.eye(10)).reshape(D, 1)

            Lp_prop = self.dist.nnlf(prop)
            rand = np.random.rand()
            if np.log(rand) < (Lp_prop - Lp_state):
                accepts += 1
                state = prop.copy()
                Lp_state = Lp_prop

            samples[:, i] = state.copy().ravel()
            if verbose & i % 10000 == 0:
                print i
        print 'Acceptance ratio', accepts/iters
        return samples
