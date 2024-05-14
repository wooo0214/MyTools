# Galaxy Multi-Image Classification with LeNet-5
# https://www.kaggle.com/code/tenzinmigmar/galaxy-multi-image-classification-with-lenet-5/notebook

# load with astroNN: astroNN is a python package to do various kinds of neural networks with targeted application in astronomy by using Keras API as model and training prototyping, but at the same time take advantage of Tensorflow’s flexibility.
# https://astronn.readthedocs.io/en/latest/galaxy10.html

# Importing Dependencies

'''
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from tensorflow import keras

from keras.models import Sequential
from keras.layers import Conv2D, AveragePooling2D, Flatten, Dense, Dropout
from keras.callbacks import ReduceLROnPlateau
from keras.optimizers import Adam

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from tensorflow.keras import utils

from astroNN.datasets import galaxy10
from astroNN.datasets.galaxy10 import galaxy10cls_lookup'''

'''
stuck at 
failed to import these two components on kaggle: 
from astroNN.datasets import galaxy10 
from astroNN.datasets.galaxy10 import galaxy10cls_lookup
'''

# 由于环境问题无法导入astroNN包，决定在d盘创建虚拟环境再安装所需包。通过h5py,下载Galaxy10_DECals.h5来导入Galaxy10 DECals Dataset
# 创建虚拟环境：https://code.visualstudio.com/docs/python/environments

''' 
在命令行中，cd至目标文件夹下，运行python -m venv '目录名'，来创建虚拟环。创建完成后，目标文件夹下会生成子文件夹'目录名'
https://python-forum.io/thread-39414.html
'''

# check pip version and install packages in cmd. Activate the virtual environment in cmd: .\'venv_galaxyclas'\Scripts\activate.bat

import h5py
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from tensorflow import keras

from keras.models import Sequential
from keras.layers import Conv2D, AveragePooling2D, Flatten, Dense, Dropout
from keras.callbacks import ReduceLROnPlateau
from keras.optimizers import Adam

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from tensorflow.keras import utils

with h5py.File("D:/py/venv_galaxyclas/'venv_galaxyclas'/Lib/site-packages", 'r') as F:
    images = np.array(F['images'])
    labels = np.array(F['ans'])

## getting Permission denied error 