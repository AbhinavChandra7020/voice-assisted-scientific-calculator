from scipy import stats

# normal distribution
def normal_pdf(x, mu=0, sigma=1):

    return stats.norm.pdf(x, mu, sigma)

def normal_cdf(x, mu=0, sigma=1):

    return stats.norm.cdf(x, mu, sigma)

def normal_inv(p, mu=0, sigma=1):

    return stats.norm.ppf(p, mu, sigma)

# binomial distribution
def binomial_pmf(k, n, p):

    return stats.binom.pmf(k, n, p)

def binomial_cdf(k, n, p):

    return stats.binom.cdf(k, n, p)

# poisson distribution
def poisson_pmf(k, lam):

    return stats.poisson.pmf(k, lam)

def poisson_cdf(k, lam):

    return stats.poisson.cdf(k, lam)

# chi-square distribution
def chi2_pdf(x, df):

    return stats.chi2.pdf(x, df)

def chi2_cdf(x, df):

    return stats.chi2.cdf(x, df)

# t-Distribution
def t_pdf(x, df):

    return stats.t.pdf(x, df)

def t_cdf(x, df):

    return stats.t.cdf(x, df)

def t_inv(p, df):

    return stats.t.ppf(p, df)

# f-distribution
def f_pdf(x, dfn, dfd):

    return stats.f.pdf(x, dfn, dfd)

def f_cdf(x, dfn, dfd):

    return stats.f.cdf(x, dfn, dfd)


PROBABILITY_FUNCTIONS = {
    # normal distribution
    'norm_pdf': normal_pdf,
    'norm_cdf': normal_cdf,
    'norm_inv': normal_inv,
    'invnorm': normal_inv,  
    
    # binomial
    'binom_pmf': binomial_pmf,
    'binom_cdf': binomial_cdf,
    
    # poisson
    'poisson_pmf': poisson_pmf,
    'poisson_cdf': poisson_cdf,
    
    # chi-square
    'chi2_pdf': chi2_pdf,
    'chi2_cdf': chi2_cdf,
    
    # t-distribution
    't_pdf': t_pdf,
    't_cdf': t_cdf,
    't_inv': t_inv,
    
    # f-distribution
    'f_pdf': f_pdf,
    'f_cdf': f_cdf,
}

def get_function(name):
    if name in PROBABILITY_FUNCTIONS:
        return PROBABILITY_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown probability function: {name}")