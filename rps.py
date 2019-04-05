import numpy as np
from sys import argv
from os.path import exists


def alpha(statistics):
    mu = statistics[0]
    var = statistics[1]
    return (((1-mu)/var)-(1/mu))*mu**2


def beta(statistics):
    mu = statistics[0]
    alpha = alpha(statistics)
    return alpha*((1/mu)-1)


def learning_bot():
    # Read in brain
    # Choose person
    pass


def deterministic_bot():
    # do rock, paper, scissor in that order
    pass


def stochastic_rps_bot(rock, paper, scissor):
    # Create sample from population probabilities
    # mean = alpha/(alpha+beta)
    rock_sample = np.random.beta(alpha(rock), beta(rock))
    paper_sample = np.random.beta(alpha(paper), beta(paper))
    scissor_sample = np.random.beta(alpha(scissor), beta(scissor))
    roll = np.array([rock_sample, paper_sample, scissor_sample])
    decision = np.max(roll)
    if decision == 0:
        return "rock"
    elif decision == 1:
        return "paper"
    elif decision == 2:
        return "scissor"


def stochastic_sample(args):
    pass
