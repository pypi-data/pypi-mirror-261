import os  

def main(letter):
    a ='''
import pandas as pd
import numpy as np

data = pd.read_csv("wine.csv")
data.sample(5)
data.info()
data.hist(grid=False,figsize=(16,9),bins=20)

from sklearn import preprocessing
data_scale = preprocessing.scale(data["Ash"])
data["Ash"] =  data_scale
data.sample(5)

#针对数值型数据如何判断是否异常  1.5*iqn，在这个方位之外的就是异常
# data.describe()
# iqr = 1.5*(5.5845 - 3.38565)
# count = len(data.loc[data["Width"]>iqr+5.5845])+len(data.loc[data["Width"]<iqr-3.38565])
# print(count)
data = data.drop(columns="Ash_scale")

from sklearn.model_selection import train_test_split

#下抽样数据
data_undersample = data.sample(n=80,replace=False)
# data_undersample.info()
x_undersample = data_undersample.iloc[:,:-1]
y_undersample = data_undersample.iloc[:,-1:]
# x_undersample.info()
# y_undersample.info()
x_under_train,x_under_test,y_under_train,y_under_test = train_test_split(x_undersample,y_undersample,test_size=0.2,random_state=47)

#过抽样数据
from imblearn.over_sampling import SMOTE
x = data.iloc[:,:-1]
y = data.iloc[:,-1:]
x_oversample,y_oversample = SMOTE().fit_resample(x,y)
x_over_train,x_over_test,y_over_train,y_over_test = train_test_split(x_oversample,y_oversample,test_size=0.2,random_state=47)

#正常采样
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=47)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix

#逻辑回归下抽样建模
logist_under = LogisticRegression()
logist_under.fit(x_under_train,y_under_train)
y_pred_under = logist_under.predict(x_under_test)
confusion_matrix(y_under_test,y_pred_under)

#逻辑回归过抽样建模
logist_over = LogisticRegression()
logist_over.fit(x_over_train,y_over_train)
y_pred_over = logist_over.predict(x_over_test)
confusion_matrix(y_over_test,y_pred_over)

#逻辑回归正常抽样建模
logist = LogisticRegression()
logist.fit(x_train,y_train)
y_pred = logist.predict(x_test)
confusion_matrix(y_test,y_pred)

from sklearn.metrics import recall_score

#计算召回率
recall_over=recall_score(y_over_test,y_pred_over,average="weighted")
print("过抽样召回率：",recall_over)
recall=recall_score(y_test,y_pred,average="weighted")
print("正常抽样召回率：",recall)
recall_under=recall_score(y_under_test,y_pred_under,average="weighted")
print("下抽样召回率：",recall_under)
'''
    b = '''
import os
import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image

dataset_dir = "dataset" # 定义数据集文件夹。
imgname = os.listdir(dataset_dir) # 读取文件夹中图片的名称。
image_size=64 
input_images=[]
for file in imgname:
    img=Image.open(dataset_dir+"/"+file) # 读取图像。 
    img=img.resize((image_size, image_size)) # 将所有图像调整为 64 x 64 像素。
    img=img.convert("L")  # 将所有图像转换为灰度。
    img=np.asarray(img) # 将所有图像转换为 NumPy 数组。 
    input_images.append(img) # 将所有图像放入列表中。 

plt.figure()
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(input_images[i])
plt.show()

#将图像转换成一个长度为4096的一维向量。
input_images = input_images.reshape(256, image_size*image_size)
#对图像进行归一化处理。
input_images = (input_images.astype('float32')-127.5)/127.5

# 导入建模所需的TensorFlow和Keras库  
from tensorflow import keras  
from tensorflow.keras.models import Sequential, Model  
from tensorflow.keras.layers import Conv2D, Input, Dense, Dropout, Activation, Flatten, BatchNormalization  
from tensorflow.keras.layers import LeakyReLU  
from tensorflow.keras.optimizers import Adam  
  
# 定义噪声向量的长度  
noise_length = 100  
  
# 定义生成器g  
g = Sequential()  
  
# 创建一个全连接层，包含1024个神经元。设置输入层大小与噪声向量长度相同  
g.add(Dense(1024, input_dim=noise_length))  
  
# 使用LeakyReLU作为激活函数。当x < 0时，y = 0.2x  
g.add(LeakyReLU(alpha=0.2))  
  
# 添加BN层以减少中心偏移  
g.add(BatchNormalization(momentum=0.8))  
  
# 添加第二个全连接层，包含4096个神经元。使用tanh作为激活函数  
g.add(Dense(4096))  
  
# 选择LeakyReLU作为激活函数。当x < 0时，y = 0.2x  
g.add(LeakyReLU(alpha=0.2))  
  
# 添加BN层以减少中心偏移  
g.add(BatchNormalization(momentum=0.8))  
  
# 添加第二个全连接层，包含512个神经元  
g.add(Dense(512))  
  
# 使用LeakyReLU作为激活函数。当x < 0时，y = 0.2x  
g.add(LeakyReLU(alpha=0.2))  
  
# 添加BN层以减少中心偏移  
g.add(BatchNormalization(momentum=0.8))  
  
# 添加第三个全连接层，包含1024个神经元  
g.add(Dense(2048))  
  
# 使用LeakyReLU作为激活函数。当x < 0时，y = 0.2x  
g.add(LeakyReLU(alpha=0.2))  
  
# 添加BN层以减少中心偏移  
g.add(BatchNormalization(momentum=0.8))  
  
# 添加输出层。每个输出图像包含4096个像素。使用tanh激活函数将输出映射到(-1, 1)范围内  
g.add(Dense(4096))  
  
# 打印生成器的摘要  
g.summary(0)

# 为判别器设置优化器为Adam，并设置一个相对较小的学习率。  
d_adam = Adam(lr=0.0002, beta_1=0.5)  
  
# 构建判别器。  
d = Sequential()  
# 设置判别器输入层的神经元数量与生成器输出层的神经元数量相同。  
d.add(Dense(1024, input_dim=4096))  
# 选择LeakyReLU作为激活函数。  
d.add(LeakyReLU(alpha=0.2))  
# 创建下一个全连接层，包含256个神经元。  
d.add(Dense(256))  
# 判别器输出层只有一个神经元，用于识别图像是真实的还是伪造的。使用sigmoid将判别器的输出映射到(0,1)。0表示伪造，1表示真实。  
d.add(Dense(1, activation='sigmoid'))  
# 判别器使用交叉熵损失函数，并设置准确率为指标。  
d.compile(loss='binary_crossentropy', optimizer=d_adam, metrics=['accuracy'])  
# 打印判别器信息。  
d.summary()  
  
# 为GAN设置优化器为Adam。  
gan_adam = Adam()  
  
# 固定判别器的参数。  
d.trainable = False  
  
# 定义GAN的输入。  
gan_input = Input(shape=(noise_length,))  
  
# 定义生成的图像。  
generated_image = g(gan_input)  
  
# 定义GAN的输出。  
gan_output = d(generated_image)  
  
# 定义GAN模型，并组合生成器和判别器。  
gan = Model(gan_input, gan_output)  
  
# GAN使用交叉熵损失函数，并设置准确率为指标。  
gan.compile(loss='binary_crossentropy', optimizer=gan_adam, metrics=['accuracy'])  
  
# 打印GAN信息。  
gan.summary()

# 定义一个函数用于打印生成的图像  
def plot_generated(n_ex=10, dim=(1, 10), figsize=(12, 2)):  
    # 生成高斯噪声  
    noise = np.random.normal(0, 1, size=(n_ex, noise_length))  
    # 将噪声输入到生成器中获取生成的图像  
    generated_images = g.predict(noise)  
    # 将图像的像素值转换回(0, 255)范围  
    generated_images = generated_images * 127.5 + 127.5  
    # 将生成的图像向量重新整形为矩阵形式  
    generated_images = generated_images.reshape(n_ex, 64, 64)  
    # 创建一个新的图像窗口并设置其大小  
    plt.figure(figsize=figsize)  
    for i in range(generated_images.shape[0]):  
        # 在子图中绘制图像  
        plt.subplot(dim[0], dim[1], i+1)  
        # 显示灰度图像  
        plt.imshow(generated_images[i], cmap='gray')  # 添加cmap参数以显示灰度图像  
        # 关闭坐标轴显示  
        plt.axis('off')  
    # 调整子图布局  
    plt.tight_layout()  
    # 显示图像  
    plt.show()  
  
# 定义一个函数用于绘制损失曲线  
def plot_loss(losses):  
    # 从字典中提取判别器的损失值  
    d_loss = [v[0] for v in losses["D"]]  
    # 从字典中提取生成器的损失值  
    g_loss = [v[0] for v in losses["G"]]  
    # 创建一个新的图像窗口并设置其大小  
    plt.figure(figsize=(5, 4))  
    # 绘制判别器的损失曲线  
    plt.plot(d_loss, label="判别器损失")  
    # 绘制生成器的损失曲线  
    plt.plot(g_loss, label="生成器损失")  
    # 设置x轴标签  
    plt.xlabel('轮次')  
    # 设置y轴标签  
    plt.ylabel('损失')  
    # 显示图例  
    plt.legend()  
    # 显示图像  
    plt.show()


# 设置模型训练的轮数。  
num_epochs = 500  
# 设置一个相对较大的批次大小（因为使用了批量归一化）。  
batch_size = 16  
# 定义一个损失字典。使用D来存储判别器的损失，G来存储生成器的损失。  
losses = {"D":[],"G":[]}  
# 计算每个训练周期需要多少批次。  
batchCount = int(input_images.shape[0] / batch_size)  
# 训练循环。
# 对于每一个训练周期  
for epochs in range(num_epochs+1):  
    # 对于每一个批次  
    for _ in range(batchCount):  
        # 生成高斯噪声。  
        noise = np.random.normal(0, 1, size = (batch_size, noise_length))  
        # 定义真实图像的标签。  
        y_true = np.ones(batch_size)  
        # 固定判别器的参数，使其在训练生成器时不被更新。  
        d.trainable = False  
        # 训练生成器。  
        g_loss = gan.train_on_batch(noise, y_true)  
        # 生成图像。  
        fake_img = g.predict(noise)  
        # 从数据集中随机提取数据来训练模型。  
        true_img = input_images[np.random.randint(0, input_images.shape[0], size=batch_size)]  
        # 定义假图像的标签。  
        y_fake = np.zeros(batch_size)  
        # 取消固定判别器的参数，以便训练判别器。  
        d.trainable = True  
        # 使用真实图像训练判别器。  
        d_loss_true = d.train_on_batch(true_img, y_true)  
        # 记录当输入为假图像时判别器预测假图像的损失：  
        d_loss_fake = d.train_on_batch(fake_img, y_fake)  
        # 设置判别器损失为真图像识别损失和假图像识别损失的平均值。  
        d_loss = 0.5 * np.add(d_loss_true, d_loss_fake)  
    # 将当前训练批次的判别器损失添加到损失字典中。  
    losses["D"].append(d_loss)  
    # 将当前训练批次的生成器损失添加到损失字典中。  
    losses["G"].append(g_loss)  
    # 每五个训练批次打印一次生成的图像。  
    if epochs % 10 == 0:  
        plot_generated()  
        # 打印损失和准确度值。  
        print('-'*5, 'Epoch %d' % epochs, '-'*5)  
        print("生成器损失:", g_loss[0])  
        print("判别器损失:", d_loss[0])  
    # 每十个周期绘制一次损失图。  
    if epochs % 10 == 0:  
        plot_loss(losses)
'''
    c = '''
hdfs dfs -put /root/data/taxi/order.csv /user/hive/warehouse/ods.db/t_order/dt=2022-04-12

LOAD DATA INPATH 'hdfs://root/data/taxi/order.csv' INTO TABLE t_order PARTITION (dt='2022-04-12');

create table fxs if not exists(
. . . . . . . . . . . . . . . . . . . . . . .> realtime_start  string,
. . . . . . . . . . . . . . . . . . . . . . .> realtime_end string,
. . . . . . . . . . . . . . . . . . . . . . .> date string,
. . . . . . . . . . . . . . . . . . . . . . .> value decimal)
. . . . . . . . . . . . . . . . . . . . . . .> row format delimited fields terminated by ',' stored as textfile;

val sqlContext = new org.apache.spark.sql.hive.HiveContext(sc)

sqlContext.sql("CREATE TABLE foundation_spark LIKE foundation_log")

sqlContext.sql("INSERT INTO foundation_spark SELECT * FROM foundation_log")

sqlContext.sql("CREATE TABLE foundation_log AS SELECT * FROM foundation_spark")

sqlContext.sql("SELECT * FROM foundation_log").show()

SELECT realtime_start,  AVG(value) AS average_value  FROM    foundation_log group by realtime_start  order by average_value ;

select  count(*) from foundation_log where value >= 2000;
select * from foundation_log where realtime_start = '2019/12/9';
'''
    if letter == "a":
        print(a)
    elif letter == "b":
        print(b)
    elif letter == "c":
        print(c)