import numpy as np
import gnuplotlib as gp # install from pip
from sys import argv

if len(argv) > 1:
    sup = float(argv[1])
    sip = (sup-1)/2
	x = np.arange(sup) - sip
else:
	x = np.arange(10) - 4.5

gp.plot((x,np.sin(x)), terminal='dumb 170 48', _with='lines')

