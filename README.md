# robo-one (detect a robot panel)

https://touch-sp.hatenablog.com/entry/2021/01/18/225734

## How to use

~~~
git clone https://github.com/dai-ichiro/robo-one.git
cd robo-one
python make_dataset.py
python train_script.py
python predict_script.py
~~~

## Environment

~~~
Windows 10 (Build 21382) with GTX 1080
NVIDIA Driver 470.05
Ubuntu 20.04 on WLS2
WSL Linux kernel 5.10.16.3-microsoft-standard-WSL2
python 3.8.5
~~~
 
~~~
attrs==21.2.0
autocfg==0.0.8
autogluon==0.2.0
autogluon-contrib-nlp==0.0.1b20210201
autogluon.core==0.2.0
autogluon.extra==0.2.0
autogluon.features==0.2.0
autogluon.mxnet==0.2.0
autogluon.tabular==0.2.0
autogluon.text==0.2.0
autogluon.vision==0.2.0
autograd==1.3
bcrypt==3.2.0
blis==0.7.4
boto3==1.17.73
botocore==1.20.73
catalogue==2.0.4
catboost==0.25.1
certifi==2020.12.5
cffi==1.14.5
chardet==4.0.0
click==7.1.2
cloudpickle==1.6.0
ConfigSpace==0.4.18
contextvars==2.4
cryptography==3.4.7
cycler==0.10.0
cymem==2.0.5
Cython==0.29.23
d8==0.0.2.post0
dask==2021.5.0
decorator==4.4.2
decord==0.5.2
dill==0.3.3
distributed==2021.5.0
fastai==2.3.1
fastcore==1.3.20
fastprogress==1.0.0
flake8==3.9.2
fsspec==2021.5.0
future==0.18.2
gluoncv==0.10.1.post0
graphviz==0.8.4
HeapDict==1.0.1
idna==2.10
immutables==0.15
iniconfig==1.1.1
Jinja2==3.0.0
jmespath==0.10.0
joblib==1.0.1
kaggle==1.5.12
kiwisolver==1.3.1
liac-arff==2.5.0
lightgbm==3.2.1
locket==0.2.1
MarkupSafe==2.0.0
matplotlib==3.4.2
mccabe==0.6.1
minio==7.0.3
msgpack==1.0.2
murmurhash==1.0.5
mxnet-cu112==1.8.0.post0
networkx==2.5.1
numpy==1.19.5
opencv-python==4.5.2.52
openml==0.12.1
packaging==20.9
pandas==1.2.4
paramiko==2.7.2
partd==1.2.0
pathy==0.5.2
Pillow==8.1.0
pkg-resources==0.0.0
plotly==4.14.3
pluggy==0.13.1
portalocker==2.0.0
preshed==3.0.5
protobuf==3.17.0
psutil==5.8.0
py==1.10.0
pyarrow==4.0.0
pycodestyle==2.7.0
pycparser==2.20
pydantic==1.7.4
pyflakes==2.3.1
PyNaCl==1.4.0
pyparsing==2.4.7
pytest==6.2.4
python-dateutil==2.8.1
python-slugify==5.0.2
pytz==2021.1
PyYAML==5.4.1
regex==2021.4.4
requests==2.25.1
retrying==1.3.3
s3transfer==0.4.2
sacrebleu==1.5.1
sacremoses==0.0.45
scikit-learn==0.24.2
scipy==1.6.3
sentencepiece==0.1.95
six==1.16.0
smart-open==3.0.0
sortedcontainers==2.4.0
spacy==3.0.6
spacy-legacy==3.0.5
srsly==2.4.1
tblib==1.7.0
tensorboardX==2.2
text-unidecode==1.3
thinc==8.0.3
threadpoolctl==2.1.0
tokenizers==0.9.4
toml==0.10.2
toolz==0.11.1
torch==1.8.1
torchvision==0.9.1
tornado==6.1
tqdm==4.60.0
typer==0.3.2
typing-extensions==3.10.0.0
urllib3==1.26.4
wasabi==0.8.2
xgboost==1.3.3
xmltodict==0.12.0
xxhash==2.0.2
yacs==0.1.8
zict==2.0.0
~~~
