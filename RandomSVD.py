import numpy as np

def rsvd(A, r, q, p):
    A = np.array(A)
    ny = A.shape[1]
    P = np.random.randn(ny, r + p)
    Z = A.dot(P)
    for k in range(q):
        Z = A.dot(np.transpose(A).dot(Z))

    [Q, R] = np.linalg.qr(Z, mode="reduced")
    Y = np.transpose(Q).dot(A)
    [UY, S, V] = np.linalg.svd(Y, full_matrices=0)
    U = np.dot(Q,  UY)
    return [U, S, V]
