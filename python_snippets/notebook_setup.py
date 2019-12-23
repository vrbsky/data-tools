runtimes = ['local', 'hosted-colab']
runtime = runtimes[1]

from pathlib import Path
if runtime == 'hosted-colab':
    from google.colab import files
    from google.colab import drive
    drive.mount('/content/gdrive')
    rootPath = Path('gdrive/My Drive/myRoot')
    projectPath = rootPath / 'path_to/projectFolder'
    dataPath = projectPath / 'DataSets'
elif runtime == 'local':
    dataPath = Path('DataSets')
    projectPath = Path('./')

if runtime == 'hosted-colab':
    exportPath = projectPath
else:
    exportPath = projectPath

# doing `%cd SwitchFrequencyAnalysis` to change directories is another way,
# as suggested [here](https://stackoverflow.com/questions/48298146/changing-directory-in-google-colab-breaking-out-of-the-python-interpreter)


# ========================================

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import HTML
import datetime
from dateutil.relativedelta import *
import seaborn as sns
import re
import sys, os

# plotly stuff - might not work in colab notebooks
#import plotly.plotly as py
#import plotly.tools as tls
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#import plotly.plotly as py
import plotly.graph_objs as go
import cufflinks as cf
print("Plotly version needs to be >= 1.9.0. Imported version:",__version__) # requires version >= 1.9.0
# For Notebooks
init_notebook_mode(connected=True)
# For offline use
cf.go_offline()

# Use this plotting style
plt.style.use('ggplot')
%matplotlib inline

# config
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# show numbers without scientific notation (123e9)
pd.set_option('display.float_format', lambda x: format(x, ',.2f'))

#!pip install line_profiler
#%load_ext line_profiler


# ========================================

print(f'Python version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}\n')
print('Python version: ' + sys.version)

if runtime == 'hosted-colab':
    !cat /proc/cpuinfo
    !cat /proc/meminfo

    import tensorflow as tf
    device_name = tf.test.gpu_device_name()
    if device_name != '/device:GPU:0':
        raise SystemError('GPU device not found')
    print(f'\nFound GPU at: {device_name}\n')

    from tensorflow.python.client import device_lib
    device_lib.list_local_devices()
    

# ========================================