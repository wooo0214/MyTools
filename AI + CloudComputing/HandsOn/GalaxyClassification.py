# Galaxy Multi-Image Classification with LeNet-5
# https://www.kaggle.com/code/tenzinmigmar/galaxy-multi-image-classification-with-lenet-5/notebook

# Overview
'''
- Load the Galaxy10 dataset
- Build baseline model
- Build LeNet-5 model
- Evaluation (confusion matrix, accuracy, recall, f1 score)
   - accuracy, Precision = True Positive (TP) / True Positive (TP) + False Positive (FP)
   - recall, Recall = True Positive (TP) / True Positive (TP) + False Negative (FN)
   - f1 score, evaluate the accuracy of a binary classification system. It is the harmonic mean (调和平均数) of precision and recall.

'''
'''
[Done]

Model Summary

1. At the 3rd epoch, compared to the baseline modelzz : accuracy: 0.1488 - loss: 2.2392, the model7 has accuracy: 0.5092 and loss: 1.3635. The accuracy was improved 242% and the loss was reduced 39%.
2. With higher epochs (10), model7 has accuracy: 0.7445 - loss: 0.7295. Fit time < 10 mins.
3. Model 7 has 0.9 recall for type 2 (smooth, completely round) and 0.82 recall for type 9 (disk, face-on, loose spiral), meaning it has a strong ability to distinguish positive samples in these two types of galaxies.
4. Type 2 has the highest f1 score 0.83 indicating higher accuracy levels; while type 0 (disk, face-on, no spiral) only has 0.2 f1 score and 0.14 recall meaning model 7's ability to recognize type 0 is weak and it classifies most type 0 into other types incorrectly.
5. Types that have f1 score >=0.7:
- smooth, completely round
- smooth, in-between round
- disk, face-on, medium spiral
- disk, face-on, loose spiral

'''

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

'''with h5py.File("D:/py/venv_galaxyclas/'venv_galaxyclas'/Lib/site-packages", 'r') as F:
    images = np.array(F['images'])
    labels = np.array(F['ans'])'''

## use / instead of \ in file path
## getting Permission denied error:
'''
{
	"name": "PermissionError",
	"message": "[Errno 13] Unable to synchronously open file (unable to open file: name = 'D:/py/venv_galaxyclas/'venv_galaxyclas'/Lib/site-packages', errno = 13, error message = 'Permission denied', flags = 0, o_flags = 0)",
	"stack": "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[1;31mPermissionError\u001b[0m                           Traceback (most recent call last)\nFile \u001b[1;32md:\\xy\\MyFiles\\GitLocal Repository\\wooo\\MyTools\\MyTools\\AI + CloudComputing\\HandsOn\\GalaxyClassification.py:65\u001b[0m\n\u001b[0;32m     62\u001b[0m \u001b[39mfrom\u001b[39;00m \u001b[39msklearn\u001b[39;00m\u001b[39m.\u001b[39;00m\u001b[39mmetrics\u001b[39;00m \u001b[39mimport\u001b[39;00m classification_report,confusion_matrix\n\u001b[0;32m     63\u001b[0m \u001b[39mfrom\u001b[39;00m \u001b[39mtensorflow\u001b[39;00m\u001b[39m.\u001b[39;00m\u001b[39mkeras\u001b[39;00m \u001b[39mimport\u001b[39;00m utils\n\u001b[1;32m---> 65\u001b[0m \u001b[39mwith\u001b[39;00m h5py\u001b[39m.\u001b[39;49mFile(\u001b[39m\"\u001b[39;49m\u001b[39mD:/py/venv_galaxyclas/\u001b[39;49m\u001b[39m'\u001b[39;49m\u001b[39mvenv_galaxyclas\u001b[39;49m\u001b[39m'\u001b[39;49m\u001b[39m/Lib/site-packages\u001b[39;49m\u001b[39m\"\u001b[39;49m, \u001b[39m'\u001b[39;49m\u001b[39mr\u001b[39;49m\u001b[39m'\u001b[39;49m) \u001b[39mas\u001b[39;00m F:\n\u001b[0;32m     66\u001b[0m     images \u001b[39m=\u001b[39m np\u001b[39m.\u001b[39marray(F[\u001b[39m'\u001b[39m\u001b[39mimages\u001b[39m\u001b[39m'\u001b[39m])\n\u001b[0;32m     67\u001b[0m     labels \u001b[39m=\u001b[39m np\u001b[39m.\u001b[39marray(F[\u001b[39m'\u001b[39m\u001b[39mans\u001b[39m\u001b[39m'\u001b[39m])\n\nFile \u001b[1;32md:\\py\\venv_galaxyclas\\'venv_galaxyclas'\\Lib\\site-packages\\h5py\\_hl\\files.py:562\u001b[0m, in \u001b[0;36mFile.__init__\u001b[1;34m(self, name, mode, driver, libver, userblock_size, swmr, rdcc_nslots, rdcc_nbytes, rdcc_w0, track_order, fs_strategy, fs_persist, fs_threshold, fs_page_size, page_buf_size, min_meta_keep, min_raw_keep, locking, alignment_threshold, alignment_interval, meta_block_size, **kwds)\u001b[0m\n\u001b[0;32m    553\u001b[0m     fapl \u001b[39m=\u001b[39m make_fapl(driver, libver, rdcc_nslots, rdcc_nbytes, rdcc_w0,\n\u001b[0;32m    554\u001b[0m                      locking, page_buf_size, min_meta_keep, min_raw_keep,\n\u001b[0;32m    555\u001b[0m                      alignment_threshold\u001b[39m=\u001b[39malignment_threshold,\n\u001b[0;32m    556\u001b[0m                      alignment_interval\u001b[39m=\u001b[39malignment_interval,\n\u001b[0;32m    557\u001b[0m                      meta_block_size\u001b[39m=\u001b[39mmeta_block_size,\n\u001b[0;32m    558\u001b[0m                      \u001b[39m*\u001b[39m\u001b[39m*\u001b[39mkwds)\n\u001b[0;32m    559\u001b[0m     fcpl \u001b[39m=\u001b[39m make_fcpl(track_order\u001b[39m=\u001b[39mtrack_order, fs_strategy\u001b[39m=\u001b[39mfs_strategy,\n\u001b[0;32m    560\u001b[0m                      fs_persist\u001b[39m=\u001b[39mfs_persist, fs_threshold\u001b[39m=\u001b[39mfs_threshold,\n\u001b[0;32m    561\u001b[0m                      fs_page_size\u001b[39m=\u001b[39mfs_page_size)\n\u001b[1;32m--> 562\u001b[0m     fid \u001b[39m=\u001b[39m make_fid(name, mode, userblock_size, fapl, fcpl, swmr\u001b[39m=\u001b[39;49mswmr)\n\u001b[0;32m    564\u001b[0m \u001b[39mif\u001b[39;00m \u001b[39misinstance\u001b[39m(libver, \u001b[39mtuple\u001b[39m):\n\u001b[0;32m    565\u001b[0m     \u001b[39mself\u001b[39m\u001b[39m.\u001b[39m_libver \u001b[39m=\u001b[39m libver\n\nFile \u001b[1;32md:\\py\\venv_galaxyclas\\'venv_galaxyclas'\\Lib\\site-packages\\h5py\\_hl\\files.py:235\u001b[0m, in \u001b[0;36mmake_fid\u001b[1;34m(name, mode, userblock_size, fapl, fcpl, swmr)\u001b[0m\n\u001b[0;32m    233\u001b[0m     \u001b[39mif\u001b[39;00m swmr \u001b[39mand\u001b[39;00m swmr_support:\n\u001b[0;32m    234\u001b[0m         flags \u001b[39m|\u001b[39m\u001b[39m=\u001b[39m h5f\u001b[39m.\u001b[39mACC_SWMR_READ\n\u001b[1;32m--> 235\u001b[0m     fid \u001b[39m=\u001b[39m h5f\u001b[39m.\u001b[39;49mopen(name, flags, fapl\u001b[39m=\u001b[39;49mfapl)\n\u001b[0;32m    236\u001b[0m \u001b[39melif\u001b[39;00m mode \u001b[39m==\u001b[39m \u001b[39m'\u001b[39m\u001b[39mr+\u001b[39m\u001b[39m'\u001b[39m:\n\u001b[0;32m    237\u001b[0m     fid \u001b[39m=\u001b[39m h5f\u001b[39m.\u001b[39mopen(name, h5f\u001b[39m.\u001b[39mACC_RDWR, fapl\u001b[39m=\u001b[39mfapl)\n\nFile \u001b[1;32mh5py\\\\_objects.pyx:54\u001b[0m, in \u001b[0;36mh5py._objects.with_phil.wrapper\u001b[1;34m()\u001b[0m\n\nFile \u001b[1;32mh5py\\\\_objects.pyx:55\u001b[0m, in \u001b[0;36mh5py._objects.with_phil.wrapper\u001b[1;34m()\u001b[0m\n\nFile \u001b[1;32mh5py\\\\h5f.pyx:102\u001b[0m, in \u001b[0;36mh5py.h5f.open\u001b[1;34m()\u001b[0m\n\n\u001b[1;31mPermissionError\u001b[0m: [Errno 13] Unable to synchronously open file (unable to open file: name = 'D:/py/venv_galaxyclas/'venv_galaxyclas'/Lib/site-packages', errno = 13, error message = 'Permission denied', flags = 0, o_flags = 0)"
}
'''

## 可恶 不读这个文件了
## installed astroNN
from astroNN.datasets import galaxy10 
from astroNN.datasets.galaxy10 import galaxy10cls_lookup

# interactive window all good

# create test and train sets
## more info about train test split: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
images, labels = galaxy10.load_data() # 得，重新下载2.7G的数据集

x_train, x_test, y_train, y_test = train_test_split(images, labels, test_size=0.2)

features = ['Disk, Face-on, No Spiral', 'Smooth, Completely round', 'Smooth, in-between round', 'Smooth, Cigar shaped', 'Disk, Edge-on, Rounded Bulge', 'Disk, Edge-on, Boxy Bulge', 
            'Disk, Edge-on, No Bulge','Disk, Face-on, Tight Spiral', 'Disk, Face-on, Medium Spiral', 'Disk, Face-on, Loose Spiral']

# to normalize the pixel values of the images: 0-255 to 0-1. It helps the model to converge faster.
x_train = x_train / 255.0
x_test = x_test / 255.0

# check dataset dimensions
x_train.shape, x_test.shape

'''
>>> ((14188, 256, 256, 3), (3548, 256, 256, 3))
means we now have a train set with 14188 colored images, dimensions 256 by 256; and a test set with 3548 images dimensions 256 * 256
'''
## Q: why 256 by 256? > 图片像素是256*256
'''
type(x_train[1])
>>> numpy.ndarray
x_train[1].shape
>>> (256,256,3)
'''

# draw the first 25 train images
fig = plt.figure(figsize=(20,20))  # figsize: Width, height in inches

for i in range(25):
    plt.subplot(5,5,i+1)    
    plt.imshow(x_train[i])
    plt.title(features[y_train[i]])
    fig.tight_layout(pad=3.0)
    
plt.show()

# Check class distribution 查看各个类别的图片总数，定义分布函数并画图
df = pd.DataFrame(data=labels)

counts = df.value_counts().sort_index()
print(counts)

def class_distribution(x, y, labels):
    fig, ax = plt.subplots() # 建立画布窗口，等效于 fig, ax = plt.subplots(11)
    ax.bar(x, y) # 定义一个bar图
    ax.set_xticklabels(labels, rotation=90)
    plt.show()
    
class_distribution(features, counts, features)

'''
fig, axes = plt.subplots(2,2)
data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))

x1 = np.linspace(0,4*np.pi,100)
y1 = np.sin(x1)

# axes[x,x] tells where to draw the fig
axes[0, 0].axis('off')

axes[1, 0].plot(x1, y1)

data.plot.bar(ax=axes[0,0])
plt.show()
'''

## 根据分布函数
### 下面这段sequetial是干嘛的？
'''
Sequential，序贯模型，是Keras模型之一，另一种是Model函数式模型。序贯模型是函数式模型的一种特殊情况。

序贯模型是多个网络层的线性堆叠，“一条路走到黑”，为最简单的线性，从头到尾的结构顺序，不发生分叉。可以通过向Sequential模型传递一个layer的list来构造Sequential模型，也可以通过.add()方法一个个的将layer加入模型中。

应用序贯模型的基本步骤
1，model.add()  　　　   　  添加层
2，model.compile()　　　　 模型训练的BP模式设置
3，model.fit()　　　　　　   模型训练参数设置+训练
4，model.evaluate()   　　　   模型评估
5，model.predict()　　　　　模型预测

'''

modelzz = Sequential()

# Baseline model to compare to LeNet-5 
## pretty slow 200ms+/step
modelzz.add(Flatten(input_shape=(69, 69, 3))) # Flatten layer to convert 3D data to 1D
modelzz.add(Dense(128, activation='relu')) # Dense layer with 128 neurons, to connect every input from Flatten layer to each of 128 neurons
# modelzz.add(Dropout(0.2)) # Dropout layer to prevent overfitting
modelzz.add(Dense(10, activation='softmax')) # Output layer with 10 neurons for multi-class classification with 10 classes, where each neuron corresponds to a class
# The softmax activation function converts the raw output scores into probabilities, allowing the model to predict the likelihood of each class.

model_optimizer = Adam(learning_rate=0.001) # need to use learning_rate instead of lr

modelzz.compile(optimizer=model_optimizer, loss='sparse_categorical_crossentropy', metrics=["accuracy"])
reduceLR = ReduceLROnPlateau(monitor='accuracy', factor=.001, patience=1, min_delta=0.01, mode="auto")
lol = modelzz.fit(x_train, y_train, epochs=10, callbacks=[reduceLR])

# Predictions on baseline model 

predictions = modelzz.predict(x_test)

for i in range(10):
    print("Actual:", features[y_test[i]])
    print("Prediction:", features[np.argmax(predictions[i])])
    print ("______")
    print()

## 引入LeNet-5 Architecture，得到拟合效果更好的模型
model2 = Sequential()

# LeNet-5 conv-net architecture
'''
LeNet-5是一种经典的卷积神经网络。LeNet-5的基本结构包括7层网络结构（不含输入层），其中包括2个卷积层、2个降采样层（池化层）、2个全连接层和输出层。LeNet-5的训练过程使用反向传播算法（BP算法），通过最小化误差函数（通常使用交叉熵损失函数）来优化网络的权重和偏置。网络的权重和偏置是通过随机初始化得到的，然后，网络通过反向传播算法不断地调整权重和偏置，使得误差函数最小化。

LeNet-5也为后来更加复杂的卷积神经网络奠定了基础，例如AlexNet、VGG、ResNet等。这些网络都采用了类似LeNet-5的卷积神经网络结构，但增加了更多的层数和参数，从而在图像分类、目标检测等任务中取得了更好的效果。虽然LeNet-5在当今深度学习的发展中已经不再是最先进的技术，但它的经典结构和训练方法仍然对深度学习的发展和应用有重要意义。

以下通过加入卷积层1、池化层1、卷积层2、池化层2，最后将输入传递到全连接层，构建了一个简单的卷积神经网络，来提高训练效果和预测准确度。
'''
'''
model2.add(Conv2D(filters=6, kernel_size=(5,5), strides=(1,1), activation='tanh', input_shape=(69,69,3)))
model2.add(AveragePooling2D(pool_size=(2,2), strides=(2,2)))
model2.add(Conv2D(filters=16, kernel_size=(5,5), strides=(1,1), activation='tanh'))
model2.add(AveragePooling2D(pool_size=(2,2), strides=(2,2)))

model2.add(Flatten())
model2.add(Dense(units=120, activation='tanh'))
model2.add(Dense(units=84, activation='tanh'))
model2.add(Dense(units=10, activation='softmax'))

model_optimizer = Adam(learning_rate=0.001)

reduceLR = ReduceLROnPlateau(monitor='accuracy', factor=.001, patience=1, min_delta=0.01, mode="auto")

model2.compile(optimizer=model_optimizer, loss='sparse_categorical_crossentropy', metrics=["accuracy"])
model2.fit(x_train, y_train, epochs=10, callbacks=[reduceLR]) # 报错again：

predict = model2.predict(x_test).argmax(axis=1)
'''

## 由于自己导入的数据集中图片大小为256*256，与原文有别，需对原文代码中的部分数据修改，建立model3
model7=Sequential()
model7.add(Conv2D(filters=16, kernel_size=(9,9), strides=(4,4), activation='tanh', input_shape=(256,256,3)))
model7.add(AveragePooling2D(pool_size=(2,2), strides=(2,2)))
model7.add(Conv2D(filters=32, kernel_size=(5,5), strides=(1,1), activation='tanh'))
model7.add(AveragePooling2D(pool_size=(2,2), strides=(2,2)))
model7.add(Conv2D(filters=32, kernel_size=(3,3), strides=(1,1), activation='tanh'))
model7.add(AveragePooling2D(pool_size=(2,2), strides=(2,2)))

model7.add(Flatten())
model7.add(Dense(units=120, activation='tanh'))
model7.add(Dense(units=84, activation='tanh'))
model7.add(Dense(units=10, activation='softmax'))
model_optimizer = Adam(learning_rate=0.001)

reduceLR = ReduceLROnPlateau(monitor='accuracy', factor=.001, patience=1, min_delta=0.01, mode="auto")

model7.compile(optimizer=model_optimizer, loss='sparse_categorical_crossentropy', metrics=["accuracy"])
model7.fit(x_train, y_train, epochs=5, callbacks=[reduceLR]) # 最花时间

### May 20th, 10th epoch accuracy still low (0.1396). See github issues for details.

## 使用summary查看模型参数
'''
model5.summary()
>>>
Layer | output shape | Param #
conv2d_11 | (None, 62, 62, 6) | 1464
average_pooling2d_10 | (None, 31, 31, 6) | 0
conv2d_12 | (None, 6, 6, 16) | 7792 0
average_pooling2d_11 | (None, 3, 3, 16) | 0
...
'''

## 模型预测
predict = model6.predict(x_test).argmax(axis=1)

for i in range(10):
    print("Actual:", features[y_test[i]])
    print("Prediction:", features[np.argmax(predict[i])])
    print("-----")
    print()

## 理解卷积：b站王大叔学科学；https://cloud.tencent.com/developer/article/1523074

## 查看分类报告
classification_report(y_test, predict)

## confusion_matrix

'''
如果已经训练好了一个系统用来区分猫和狗，那混淆矩阵就可以概括算法的测试结果以便将来的检查。假设一个13个动物的样本，8只猫和5只狗，那混淆矩阵的结果可能如下表所示：

      |预测的类别      |
	  | 猫    | 狗    |
实际|猫|  *5* |   3   |
类别|狗|  2   |  *3*  |

在这个混淆矩阵中，系统预测了8只实际的猫，其中系统预测3只是狗，而5只狗中，则预测有2只是猫。 所有正确的预测都位于表格的对角线上（以粗体突出显示），因此很容易从视觉上检查表格中的预测错误，因为它们将由对角线之外的值表示。
'''

matrix = confusion_matrix(y_test, predict)
sns.heatmap(matrix, annot=True)
plt.title('Galaxy Confusion Matrix')
plt.xlabel('Predicted class')
plt.ylabel('True class')