import sys
import numpy as np

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    # Added assertion because I can
    assert filename[-3:] == 'csv', 'File not CSV'
    data = np.loadtxt(filename, delimiter=',')
    for row_mean in np.mean(data, axis=1):
        print(row_mean)

if __name__ == '__main__':
    main()