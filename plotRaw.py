import os
from pathlib import Path as P
from pathlib import PurePath as PP
from readDataFile import read
from filterReal import isdigit

import PIL
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as mpl

from matplotlib import rc
plt.style.use(['science'])
rc('text.latex', preamble=r'\usepackage{cmbright}')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.linewidth'] = 1
plt.rcParams['xtick.major.size'] = 5
plt.rcParams['xtick.major.width'] = 1
plt.rcParams['xtick.minor.size'] = 2
plt.rcParams['xtick.minor.width'] = 1
plt.rcParams['ytick.major.size'] = 5
plt.rcParams['ytick.major.width'] = 1
plt.rcParams['ytick.minor.size'] = 2
plt.rcParams['ytick.minor.width'] = 1
plt.rcParams['lines.linewidth'] = 2
lw = 2

import ast
import os
from pathlib import Path as P
from pathlib import PurePath as PP
from readDataFile import read

import PIL
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
plt.style.use(['science'])
rc('text.latex', preamble=r'\usepackage{cmbright}')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.linewidth'] = 1
plt.rcParams['xtick.major.size'] = 5
plt.rcParams['xtick.major.width'] = 1
plt.rcParams['xtick.minor.size'] = 2
plt.rcParams['xtick.minor.width'] = 1
plt.rcParams['ytick.major.size'] = 5
plt.rcParams['ytick.major.width'] = 1
plt.rcParams['ytick.minor.size'] = 2
plt.rcParams['ytick.minor.width'] = 1
plt.rcParams['lines.linewidth'] = 2



def main(filename):
    d = pd.read_csv(filename, skiprows=4)
    d['time'] = np.linspace(0, 2e-9*len(d['time']), len(d['time']))
    fig, ax = plt.subplots()
    d['y'] = (d[' Y[0]'] - np.min(d[' Y[0]']))
    d['y'] /= np.max(d['y'])
    t = d['time'].to_numpy()
    y = d['y'].to_numpy()
    l = 3.5e-6
    h = 6e-6
    ax.plot(t[np.logical_and(t > l, t < h)], y[np.logical_and(t > l, t < h)], c='blue')
    ax.set_ylabel('Signal (arb. u)')
    ax.set_xlabel('Time (s)')
    ax.set_yticks([0,1])
    ax.text(6e-6, 0.7, 'LiPC crystal\n10,000 scans\n4.3 s acquisition', horizontalalignment='right')
    fig.savefig(P(filename).parent.joinpath('raw.png'), dpi=400, transparent=True)


if __name__ == "__main__":
    filename = ''
    main(filename)
    plt.show()
