runtimes = ['local', 'hosted-colab']
runtime = runtimes[1]

from pathlib import Path
if runtime == 'hosted-colab':
  from google.colab import files
  from google.colab import drive
  drive.mount('/content/gdrive')
  rootPath = Path('gdrive/My Drive/VibeAnalytics')
  dataPath = rootPath / 'DataSets/GT_Imobiliario'
  projectPath = rootPath / 'banpara-data-grind/Analise_PoliciaisMilitares'
elif runtime == 'local':
  dataPath = Path('DataSets')
  projectPath = Path('./')


# config
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import HTML

# show numbers without scientific notation (123e9)
pd.set_option('display.float_format', lambda x: format(x, ',.2f'))

if runtime == 'hosted-colab':
  exportPath = rootPath / 'DataSets/GT_Imobiliario/Prep_out'
else:
  exportPath = projectPath / 'GT_Imobiliario/Prep_out'
  
%matplotlib inline