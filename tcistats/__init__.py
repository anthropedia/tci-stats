import numpy


def cronbach_alpha(scores):
    scores = numpy.asarray(scores)
    itemvars = scores.var(axis=1, ddof=1)
    total = scores.sum(axis=0)
    nitems = len(scores)
    alpha = nitems / (nitems-1.) * (1 - itemvars.sum() / total.var(ddof=1))
    return round(alpha, 10)
