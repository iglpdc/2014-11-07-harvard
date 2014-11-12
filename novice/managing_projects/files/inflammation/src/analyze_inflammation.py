import os
import sys
import numpy as np
from matplotlib import pyplot as plt

def make_filename_for_plot(filename):
    '''Makes a filename for the plot given the data filename
    
    Parameters
    ----------
        filename: str
             Path to the file for data to analyze. Can be relative or absolute.
    '''    
    filename = os.path.abspath(filename)
    plot_filename = os.path.basename(filename)[:-4] + '.pdf'
    data_dir = os.path.dirname(os.path.dirname(os.path.abspath(filename)))
    results_dir = os.path.join(os.path.dirname(data_dir), 'results')
    return os.path.join(results_dir, plot_filename)

def analyze_inflammation(filename):
    '''Makes a plot of average, min, and max
    
    Parameters
    ----------
        filename: str
             Path to the file for data to analyze. Can be relative or absolute.
    '''
    filename = os.path.abspath(filename)
    data = np.loadtxt(fname=filename, delimiter=',')

    plt.figure(figsize=(10.0, 3.0))

    plt.subplot(1, 3, 1)
    plt.ylabel('average')
    plt.plot(data.mean(0))

    plt.subplot(1, 3, 2)
    plt.ylabel('max')
    plt.plot(data.max(0))

    plt.subplot(1, 3, 3)
    plt.ylabel('min')
    plt.plot(data.min(0))

    plt.tight_layout()
    
    filename_for_plot = make_filename_for_plot(filename)
    plt.savefig(filename_for_plot)
    
    print('Plotting result in ' + filename_for_plot)
    
filename = sys.argv[1]
analyze_inflammation(filename)
