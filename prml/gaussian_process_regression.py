import numpy as np
import matplotlib.pyplot as plt


def generate_data_regression():
    x = np.random.uniform(0, 1, 33)
    noise = np.random.normal(0, 0.3, 33)
    real_x = np.linspace(0, 1, 1000)
    x.sort()
    y = np.sin(x*2*np.pi)
    y += noise
    real_y = np.sin(real_x*2*np.pi)
    plt.plot(real_x, real_y, 'g-')
    plt.scatter(x, y, color='r', marker='*')
    plt.show()
    return x, y


def generate_data_classification():
    b0 = 2*np.random.normal(0, 0.3, 100)
    b1 = 2*np.random.normal(0, 0.4, 100)
    plt.scatter(b0, b1, color='b', marker='o', alpha=0.4)
    r0 = np.random.normal(1, 0.3, 100)
    r1 = np.random.normal(1, 0.5, 50)
    r2 = np.random.normal(-1, 0.5, 50)
    plt.scatter(r0[:50], r1, color='red', marker='*', alpha=0.4)
    plt.scatter(r0[50:], r2, color='red', marker='*', alpha=0.4)
    # r0 = 2*np.random.normal()

    plt.show()


def kernel(x, y, sigma=1.0):
    d = (x - y)**2 / sigma
    return np.exp(-0.5 * d)


class Gaussian():
    def __init__(self, kn, beta=0.1):
        self.kn = kn
        self.beta = beta

    # compute the gram matrix
    def gram(self, x1, x2):
        N = x1.shape[0]
        M = x2.shape[0]
        k = np.zeros((N, M), dtype=np.float32)
        for i in xrange(N):
            for j in xrange(M):
                k[i, j] = self.kn(x1[i], x2[j])
        return k

    def regression(self, x, y):
        self._x = x
        k = self.gram(x, y)
        #plus the noise
        k = k + self.beta*np.identity(k.shape[0])



if __name__ == '__main__':
    x, y = generate_data_regression()
    # generate_data_classification()

