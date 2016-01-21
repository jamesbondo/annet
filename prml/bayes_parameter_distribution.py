import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
from matplotlib import mlab


# reference
# https://github.com/jamt9000/prml/blob/master/3.3.1-parameter-distribution.ipynb

def gen_data():
    x = np.random.uniform(-1, 1, 20)
    a, b = -0.3, 0.5
    y = a + b*x
    y = y + np.random.normal(0, 0.04, 20)
    return x, y


def gaussian(x, u, sigma):
    demn = np.sqrt(2*np.pi)*np.sqrt(sigma)
    print demn*demn
    dima = np.exp(-1*np.power(x-u, 2)/(2*sigma**2))
    print dima
    return dima/demn


def gaussian2(w0, w1, x, y, sigma):
    z = w0 + w1*x
    demn = np.sqrt(2*np.pi)*sigma
    dima = np.exp(-1*np.power(z-y, 2)/(2*sigma**2))
    return dima/demn


def draw_sample(u, sigma):
    values = []
    flag = True
    while len(values) < 6:
        flag = True
        while flag:
            x1, x2 = np.random.uniform(-1, 1, 2)
            value = gaussian(x1, u, sigma)*gaussian(x2, u, sigma)
            if value > 0.3:
                values.append([x1, x2])
                flag = False
    return values


def caculate_posterior(x, y, a, b):
    f = np.array([1, x])
    f = f[np.newaxis, :]
    ff = np.dot(f.T, f)
    _a = a*np.eye(2, 2)
    s_n = _a + b*ff
    _s_n = np.linalg.inv(s_n)
    u = b*np.dot(_s_n, f.T)*y
    return u, s_n


def caculate_posterior_dim(x, y, sigma, b):
    f = np.array([1, x])
    f = f[np.newaxis, :]
    ff = np.dot(f.T, f)
    s_n = sigma + b*ff
    _s_n = np.linalg.inv(s_n)
    # u = b*np.dot(_s_n, f.T)*y
    u = b*np.dot(_s_n, np.dot(f.T, y))
    return u, s_n



def mult_gaussian(w, u, sigma):
    demn = 2*np.pi*np.sqrt(np.linalg.det(sigma))
    print '-------', demn
    u1 = w-u
    delt = np.dot(np.dot(u1.T, sigma), u1)
    dima = np.exp(-0.5*delt)
    print dima
    return dima/demn


if __name__ == '__main__':
    # x, y = gen_data()
    # _x = np.linspace(1, -1, 1000)
    # _y = -0.3 + 0.5*_x
    #
    # fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9), (ax10, ax11, ax12)) = plt.subplots(4, 3, figsize=(12, 12))
    # fig.subplots_adjust(hspace=0.3, wspace=0.3)
    # ax1.plot(_x, _y, 'r')
    # ax1.scatter(x, y)
    #
    prior_dist_w0 = np.linspace(1, -1, 1000)
    prior_w0, prior_w1 = np.meshgrid(prior_dist_w0, prior_dist_w0)
    # result = gaussian(prior_w0, 0, 0.5)*gaussian(prior_w1, 0, 0.5)
    # resultss = mlab.bivariate_normal(prior_w0, prior_w1, sigmax=0.5, sigmay=0.5, mux=0, muy=0, sigmaxy=0)
    # ax2.contourf(prior_w0, prior_w1, result)
    #
    # result3 = draw_sample(0, 0.2)
    # for (x0, x1) in result3:
    #     _y = x0 + x1*_x
    #     ax3.plot(_x, _y, 'r')
    #
    # result4 = gaussian2(prior_w0, prior_w1, x[0], y[0], 0.2)
    # ax4.contourf(prior_w0, prior_w1, result4)
    #
    # # caculate_posterior(x[0], y[0], 2.0, 0.2)
    # result5 = np.zeros((prior_w0.shape[0], prior_w0.shape[1]))
    # u, sigma = caculate_posterior(x[0], y[0], 2.0, 0.2)
    # # for i in range(19):
    # #     x1, y1 = x[i+1], y[i+1]
    # #     u, sigma = caculate_posterior_dim(x1, y1, sigma, 0.2)
    #
    # u[0, :] = 0
    # u[1, :] = 0
    # sigma[0, 0] = 0.5
    # sigma[1, 1] = 0.5
    # sigma[0, 1] = 0
    # sigma[1, 0] = 0
    # print u, sigma
    # sigma = np.linalg.inv(sigma)
    # # result_test = stats.multivariate_normal(np.array([0, 0]), sigma, (1000, 1000))
    # # print result_test
    #
    # # Z = mlab.bivariate_normal(prior_w0, prior_w1, sigmax=np.sqrt(sigma[0,0]), sigmay=np.sqrt(sigma[1,1]), mux=u[0], muy=u[1], sigmaxy=sigma[0,1])
    # for i in xrange(prior_w0.shape[0]):
    #     for j in xrange(prior_w0.shape[1]):
    #         data = np.array([prior_w0[i, j], prior_w1[i, j]])
    #         data = data[:, np.newaxis]
    #         result5[i, j] = mult_gaussian(data, u, sigma)
    # ax5.contourf(prior_w0, prior_w1, result5)
    #
    # ax6.contourf(prior_w0, prior_w1, resultss)
    # plt.show()

    u = np.zeros((2, 1))
    u[0, :] = 0
    u[1, :] = 0.9
    sigma = np.zeros((2, 2))
    sigma[0, 0] = 0.5
    sigma[1, 1] = 0.5
    sigma[0, 1] = 0
    sigma[1, 0] = 0
    t = np.zeros((2, 1))

    v1 = gaussian(0, 0, 0.5)*gaussian(0.9, 0, 0.5)
    v2 = mult_gaussian(t, u, sigma)
    print v1, v2

