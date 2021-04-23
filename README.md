# robo-one (detect a robot panel)

https://touch-sp.hatenablog.com/entry/2021/01/18/225734

## How to use

~~~
git clone -b gluoncv_auto https://github.com/dai-ichiro/robo-one.git
cd robo-one
python make_dataset.py
python train_script.py
python predict_script.py
~~~

## Environment

~~~
Windows 10 (Build 21364) with GTX 1080
NVIDIA Driver 470.14 
Ubuntu 18.04 on WLS2
python 3.7.5
~~~
 
~~~
autocfg==0.0.8
autogluon.core==0.1.0
autograd==1.3
bcrypt==3.2.0
boto3==1.17.56
botocore==1.20.56
certifi==2020.12.5
cffi==1.14.5
chardet==4.0.0
click==7.1.2
cloudpickle==1.6.0
ConfigSpace==0.4.18
cryptography==3.4.7
cycler==0.10.0
Cython==0.29.23
dask==2021.4.0
decord==0.5.2
dill==0.3.3
distributed==2021.4.0
fsspec==2021.4.0
future==0.18.2
gluoncv==0.10.1.post0
graphviz==0.8.4
HeapDict==1.0.1
idna==2.10
jmespath==0.10.0
joblib==1.0.1
kiwisolver==1.3.1
locket==0.2.1
matplotlib==3.4.1
msgpack==1.0.2
mxnet-cu102==1.8.0.post0
numpy==1.19.5
opencv-python==4.5.1.48
pandas==1.2.4
paramiko==2.7.2
partd==1.2.0
Pillow==8.2.0
pkg-resources==0.0.0
portalocker==2.3.0
protobuf==3.15.8
psutil==5.8.0
pycparser==2.20
PyNaCl==1.4.0
pyparsing==2.4.7
python-dateutil==2.8.1
pytz==2021.1
PyYAML==5.4.1
requests==2.25.1
s3transfer==0.4.2
scikit-learn==0.24.1
scipy==1.5.4
six==1.15.0
sortedcontainers==2.3.0
tblib==1.7.0
tensorboardX==2.2
threadpoolctl==2.1.0
toolz==0.11.1
tornado==6.1
tqdm==4.60.0
urllib3==1.26.4
yacs==0.1.8
zict==2.0.0
~~~
