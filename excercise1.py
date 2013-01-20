from __future__ import division
import math

def nth(f, t, n):
    if n <= 1: return f(t)
    return f(nth(f, t, n - 1))
   
def ex(ro, Rnot, I, zeta, d, f, alpha):
    """
                I                   d    2       4
        ro * ______ * cos(zeta) * (_____)   * cos (alpha)
             4 R^2                  f           
    """
    return ro * (I / (4 * Rnot**2)) * math.cos(zeta) * (d / f)**2 * nth(math.cos, alpha, 4)


if __name__ == '__main__':
    bulb = dict(ro=0.7, Rnot=1, I=5/(4 * math.pi), zeta=0, d=1, f=11, alpha=0) 
    print ex(**bulb)

    spotlight = dict(ro=0.7, Rnot=12**0.5, I=20, zeta=math.atan(2 / float(8**0.5)), d=1, f=11, alpha=0) 
    print ex(**spotlight)
