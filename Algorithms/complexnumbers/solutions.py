import numpy as np
import cmath as cm
from sympy import mpmath as mp

# Import mayavi if possible
# otherwise, fall back to matplotlib's 3d plotting.
try:
    from mayavi import mlab as ml
    use_mayavi = True
except:
    use_mayavi = False
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

# A helper function for the plots
def get_vals(f, xbounds, ybounds, res):
    x = np.linspace(xbounds[0], xbounds[1], res)
    y = np.linspace(ybounds[0], ybounds[1], res)
    X, Y = np.meshgrid(x, y, copy=False)
    return X, Y, f(X + 1.0j * Y)

# polynomial real part plot (mayavi)
def plot_real_mayavi(f, xbounds=(-1, 1), ybounds=(-1, 1), res=401):
    """ Make a surface plot of the real part
    of the function 'f' given the bounds and resolution. """
    X, Y, vals = get_vals(f, xbounds, ybounds, res)
    ml.mesh(X, Y, vals.real)
    ml.show()

# polynomial imaginary part plot (mayavi)
def plot_imag_mayavi(f, xbounds=(-1, 1), ybounds=(-1, 1), res=401):
    """ Plot the imaginary part of the function 'f'
    given the bounds and resolution. """
    X, Y, vals = get_vals(f, xbounds, ybounds, res)
    ml.mesh(X, Y, vals.imag)
    ml.show()

# polynomial real and imaginary plot (mayavi)
def plot_both_mayavi(f, xbounds=(-1, 1), ybounds=(-1, 1), res=401):
    """ Plot the real and imaginary parts of
    the function 'f', given the bounds and resolution. """
    X, Y, vals = get_vals(f, xbounds, ybounds, res)
    ml.mesh(X, Y, vals.real)
    ml.mesh(X, Y, vals.imag)
    ml.show()

# Riemann surface for real part of n'th root (mayavi)
def nroot_real_mayavi(n, res=401):
    """ Plot the Riemann surface for the real part
    of the n'th root function. """
    x = np.linspace(-1, 1, res)
    X, Y = np.meshgrid(x, x, copy=False)
    Z = X + 1.0j * Y
    r = np.absolute(Z)
    theta = np.angle(Z)
    rroot = r**(1./n)
    theta /= n
    real = rroot * np.cos(theta)
    ml.mesh(X[x>=0], Y[x>=0], real[x>=0], colormap='Blues')
    ml.mesh(X[x<0], Y[x<0], real[x<0], colormap='Blues')
    for i in xrange(1, n):
        theta += 2. * np.pi / n
        real = rroot * np.cos(theta)
        ml.mesh(X[x>=0], Y[x>=0], real[x>=0], colormap='Blues')
        ml.mesh(X[x<0], Y[x<0], real[x<0], colormap='Blues')
    ml.show()

# Riemann surface for imaginary part of n'th root (mayavi)
def nroot_imag_mayavi(n, res=401):
    """ Plot the Riemann surface for the imaginary part
    of the n'th root function. """
    x = np.linspace(-1, 1, res)
    X, Y = np.meshgrid(x, x, copy=False)
    Z = X + 1.0j * Y
    r = np.absolute(Z)
    theta = np.angle(Z)
    rroot = r**(1./n)
    theta /= n
    imag = rroot * np.sin(theta)
    ml.mesh(X[x>=0], Y[x>=0], imag[x>=0], colormap='Blues')
    ml.mesh(X[x<0], Y[x<0], imag[x<0], colormap='Blues')
    for i in xrange(1, n):
        theta += 2. * np.pi / n
        imag = rroot * np.sin(theta)
        ml.mesh(X[x>=0], Y[x>=0], imag[x>=0], colormap='Blues')
        ml.mesh(X[x<0], Y[x<0], imag[x<0], colormap='Blues')
    ml.show()

# polynomial real plot (matplotlib)
def plot_real_matplotlib(f, xbounds=(-1, 1), ybounds=(-1, 1), res=401):
    """ Make a surface plot of the real part
    of the function 'f' given the bounds and resolution. """
    X, Y, vals = get_vals(f, xbounds, ybounds, res)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, vals.real)
    plt.show()

# polynomial imaginary plot (matplotlib)
def plot_imag_matplotlib(f, xbounds=(-1, 1), ybounds=(-1, 1), res=401):
    """ Plot the imaginary part of the function 'f'
    given the bounds and resolution. """
    X, Y, vals = get_vals(f, xbounds, ybounds, res)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, vals.imag)
    plt.show()

# polynomial real and imaginary plot (matplotlib)
def plot_both_matplotlib(f, xbounds=(-1, 1), ybounds=(-1, 1), res=401):
    """ Plot the real and imaginary parts of
    the function 'f', given the bounds and resolution. """
    X, Y, vals = get_vals(f, xbounds, ybounds, res)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, vals.real)
    ax.plot_surface(X, Y, vals.imag)
    plt.show()

# Riemann surface for real part of n'th root (matplotlib)
def nroot_real_matplotlib(n, res=101):
    """ Plot the Riemann surface for the real part
    of the n'th root function. """
    x = np.linspace(-1, 1, res)
    X, Y = np.meshgrid(x, x, copy=False)
    Z = X + 1.0j * Y
    r = np.absolute(Z)
    theta = np.angle(Z)
    rroot = r**(1./n)
    theta /= n
    real = rroot * np.cos(theta)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X[x>=0], Y[x>=0], real[x>=0])
    ax.plot_surface(X[x<0], Y[x<0], real[x<0])
    for i in xrange(1, n):
        theta += 2. * np.pi / n
        real = rroot * np.cos(theta)
        ax.plot_surface(X[x>=0], Y[x>=0], real[x>=0])
        ax.plot_surface(X[x<0], Y[x<0], real[x<0])
    plt.show()

# Riemann surface for imaginary part of n'th root (matplotlib)
def nroot_imag_matplotlib(n, res=101):
    """ Plot the Riemann surface for the imaginary part
    of the n'th root function. """
    x = np.linspace(-1, 1, res)
    X, Y = np.meshgrid(x, x, copy=False)
    Z = X + 1.0j * Y
    r = np.absolute(Z)
    theta = np.angle(Z)
    rroot = r**(1./n)
    theta /= n
    imag = rroot * np.sin(theta)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X[x>=0], Y[x>=0], imag[x>=0])
    ax.plot_surface(X[x<0], Y[x<0], imag[x<0])
    for i in xrange(1, n):
        theta += 2. * np.pi / n
        imag = rroot * np.sin(theta)
        ax.plot_surface(X[x>=0], Y[x>=0], imag[x>=0])
        ax.plot_surface(X[x<0], Y[x<0], imag[x<0])
    plt.show()

# Integral of f along contour c
def contour_int(f, c, t0, t1):
    """ Evaluate the integral of the function 'f'
    parameterized by the function 'c' with initial
    and final parameter values 't0' and 't1'. """
    return complex(mp.quad(lambda t: f(c(t)) * mp.diff(c, t), (t0, t1)))

# Compute the integral in Cauchy's formula
def cauchy_formula(f, c, z0, t0, t1):
    """ Compute the integral in Cauchy's Integral formula.
    'f' is a callable function parameterized by the contour 'c'.
    't0' and 't1' are the initial and final parameter values.
    This should return a callable function that evaluates the
    integral in the function at any given `z0`. """
    return lambda z0: contour_int(lambda z: f(z) / (z - z0), c, t0, t1) / (2.0j * np.pi)

if use_mayavi:
    plot_real = plot_real_mayavi
    plot_imag = plot_imag_mayavi
    plot_both = plot_both_mayavi
    nroot_real = nroot_real_mayavi
    nroot_imag = nroot_imag_mayavi
else:
    plot_real = plot_real_matplotlib
    plot_imag = plot_imag_matplotlib
    plot_both = plot_both_matplotlib
    nroot_real = nroot_real_matplotlib
    nroot_imag = nroot_imag_matplotlib

if __name__ == '__main__':
    p = np.poly1d([1, 0, 0, 0, 1])
    # use mayavi if possible.
    # otherwise, fall back to matplotlib.
    if use_mayavi:
        plot_both_mayavi(p)
        nroot_real_mayavi(5)
        nroot_imag_mayavi(5)
    else:
        plot_both_matplotlib(p)
        nroot_real_matplotlib(5)
        nroot_imag_matplotlib(5)
    
    # All the different integration examples.
    f1 = lambda z: z.conjugate()
    f2 = lambda z: mp.exp(z)
    c1 = lambda t: mp.cos(t) + 1.0j * mp.sin(t)
    c2 = lambda t: t + 1.0j * t
    c3 = lambda t: t
    c4 = lambda t: 1 + 1.0j * t
    c5 = lambda t: mp.cos(t) + 1.0j + 1.0j * mp.sin(t)
    print "z conjugate counterclockwise along the unit ball starting and ending at 1."
    print contour_int(f1, c1, 0, 2 * np.pi)
    print "z conjugate along a straight line from 0 to 1+1j."
    print contour_int(f1, c2, 0, 1)
    print "z conjugate along the real axis from 0 to 1, then along the line from 1 to 1+1j."
    print contour_int(f1, c3, 0, 1) + contour_int(f1, c4, 0, 1)
    print "z conjugate along the unit ball centered at 1j from 0 to 1+1j."
    print contour_int(f1, c5, -np.pi / 2, 0.)
    print "e^z counterclockwise along the unit ball starting and ending at 1."
    print contour_int(f2, c1, 0, 2 * np.pi)
    print "e^z along a straight line from 0 to 1+1j."
    print contour_int(f2, c2, 0, 1)
    print "e^z along the real axis from 0 to 1, then along the line from 1 to 1+1j."
    print contour_int(f2, c3, 0, 1) + contour_int(f2, c4, 0, 1)
    print "e^z along the unit ball centered at 1j from 0 to 1+1j"
    print contour_int(f2, c5, -np.pi / 2, 0.)
