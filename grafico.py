import numpy as np
import pylab as pl
x=[5000, 6000, 7000, 8000, 9000]
y=[65, 78, 88, 89, 93]
pl.plot(x, y, 'ro')
x1=[7000, 8000, 9000, 1000, 11000]
y2=[65, 75, 85, 86, 90]
pl.plot(x1, y2, 'b*')
pl.xlabel ('Voltaje [V]')
pl.ylabel ('Efficiencia [%]')
pl.savefig('tempt.png')
