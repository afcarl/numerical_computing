import matplotlib
matplotlib.rcParams = matplotlib.rc_params_from_file('../../matplotlibrc')

import matplotlib.pyplot as plt
import numpy as np

def plotabs(f, domain):
    f = plt.plot(domain, f(np.absolute(domain)))
    return f

def sinesquared():
    s = np.linspace(-4, 4, 500)
    p = plotabs(np.sin, s)
    plt.savefig('sinesquared.pdf')
    plt.clf()
    
def derivativeplot():
    s = np.linspace(-10, 10, 500)
    plt.plot(s, s**3, label=r'$f(x)$')
    
    #plot the derivative
    plt.plot(s, 3*s**2, label=r'$\frac{dy}{dx}(x)$')
    plt.plot(s, 6*s, label=r'$\frac{d^2y}{dx^2}(x)$')
    
    #add the legend
    plt.legend(loc='upper left')
    plt.ylabel(r'$f(x)$')
    plt.xlabel(r'$x$')
    plt.axis([-3, 3, -10, 10])
    plt.title(r"$x^3$ and its derivatives")
    plt.savefig('derivativeplot.pdf')
    plt.clf()
    
if __name__ == "__main__":
    sinesquared()
    derivativeplot()
