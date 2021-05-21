import numpy as np
ndarray = np.ndarray
def sigma(val) -> float:
    sum_sigma = 0
    for i in range(val):
        sum += i
    return sum_sigma


def multiple_inputs_add(x: ndarray,y:ndarray) -> float:
    a = 0
    if x.shape == y.shape:
        a = x + y
    return sigma(a)

print(multiple_inputs_add(np.ndarray([1,2,3]),np.ndarray([2,3,4])))