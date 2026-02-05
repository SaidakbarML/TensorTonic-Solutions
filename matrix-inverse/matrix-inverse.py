import numpy as np

def matrix_inverse(A):
    A = np.array(A)

    # Check 2D and square
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return None

    # Check singular
    if np.linalg.det(A) == 0:
        return None

    return np.linalg.inv(A)
