import math

def binomial_probability(n, k, p):
    """
    Calculate the probability of k successes in n independent Bernoulli trials with success probability p.
    """
    comb = math.comb(n, k)
    return comb * (p ** k) * ((1 - p) ** (n - k)) 