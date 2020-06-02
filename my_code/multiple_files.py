import glob
import numpy as np
import matplotlib.pyplot as pyplot

filenames = sorted(glob.glob('../swc-python/data/inflammation*.csv'))
filenames = filenames[:3]
for filename in filenames:
    print(filename)

    data = np.loadtxt(fname=filename, delimiter=',')

    fig = pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(np.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(np.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(np.min(data, axis=0))

    fig.tight_layout()
    pyplot.show()

data0 = np.loadtxt(fname=filenames[0], delimiter=',')
data1 = np.loadtxt(fname=filenames[1], delimiter=',')

fig = pyplot.figure(figsize=(10.0, 3.0))

pyplot.ylabel('Differenence in average')
pyplot.plot(np.mean(data0, axis=0) - np.mean(data1, axis=0))

fig.tight_layout()
pyplot.show()

composite_data = np.zeros((60,40))
for filename in filenames:
    # sum each new file's data into composite_data as it's read
    data = np.loadtxt(fname=filename, delimiter=',')
    composite_data = composite_data + data
# and then divide the composite_data by number of samples
composite_data = composite_data / len(filenames)
fig = pyplot.figure(figsize=(10.0, 3.0))
axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)
axes1.set_ylabel('average')
axes1.plot(np.mean(data, axis=0))
axes2.set_ylabel('max')
axes2.plot(np.max(data, axis=0))
axes3.set_ylabel('min')
axes3.plot(np.min(data, axis=0))
fig.tight_layout()
pyplot.show()