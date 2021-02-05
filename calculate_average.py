def calc_average(x):
    if len(x) == 0:
        raise ZeroDivisionError("Zero division error")
    else:
        total = sum(map(float,x))
        return (total / float(len(x)))