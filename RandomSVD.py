import numpy as np

def rsvd(A, r, q, p):
    A = np.array(A)
    ny = np.size(A, 1)
    P = np.random.randn(ny, r + p)
    Z = A.dot(P)
    for k in range(q):
        Z = A.dot(np.transpose(A).dot(Z))

    [Q, R] = np.linalg.qr(Z)
    Y = np.transpose(Q).dot(Z)
    [UY, S, V] = np.linalg.svd(Y)
    U = np.dot(Q,  UY)
    return [U, S, V]

