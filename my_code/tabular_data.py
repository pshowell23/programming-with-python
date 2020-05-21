import numpy as np
import matplotlib.pyplot as pyplot

data = np.loadtxt(fname="../swc-python/data/inflammation-01.csv", delimiter=',')

image = pyplot.imshow(data)
pyplot.show()

ave_inflammation = np.mean(data, axis=0)
ave_plot = pyplot.plot(ave_inflammation)
pyplot.show()

max_plot = pyplot.plot(np.max(data, axis=0))
pyplot.show()

min_plot = pyplot.plot(np.min(data, axis=0))
pyplot.show()

# Grouping Plots
fig = pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(4, 1, 1)
axes2 = fig.add_subplot(4, 1, 2)
axes3 = fig.add_subplot(4, 1, 3)
axes4 = fig.add_subplot(4, 1, 4)

axes1.set_ylabel('average')
axes1.plot(np.mean(data, axis=0), drawstyle='steps-mid')

axes2.set_ylabel('max')
axes2.plot(np.max(data, axis=0), drawstyle='steps-mid')

axes3.set_ylabel('min')
axes3.plot(np.min(data, axis=0), drawstyle='steps-mid')

axes4.set_ylabel('standard diviation')
axes4.plot(np.std(data, axis=0))

fig.tight_layout()
pyplot.show()

