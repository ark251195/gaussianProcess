def posterior_calc( prior, likelihood,normalization_factor):
    return ((prior*likelihood)/normalization_factor)
