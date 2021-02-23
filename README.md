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
Windows 10 (Build 21318) with GTX 1080
NVIDIA Driver 465.42 
Ubuntu 18.04 on WLS2
python 3.6.9
~~~
 
~~~
attrs==20.3.0
autocfg==0.0.6
autogluon==0.1.0b20210223
autogluon-contrib-nlp==0.0.1b20210112
autogluon.core==0.1.0b20210223
autogluon.extra==0.1.0b20210223
autogluon.features==0.1.0b20210223
autogluon.mxnet==0.1.0b20210223
autogluon.tabular==0.1.0b20210223
autogluon.text==0.1.0b20210223
autogluon.vision==0.1.0b20210223
autograd==1.3
bcrypt==3.2.0
beautifulsoup4==4.9.3
blis==0.7.4
bokeh==2.3.0rc3
boto3==1.17.13
botocore==1.20.13
Bottleneck==1.3.2
catalogue==2.0.1
catboost==0.24.4
certifi==2020.12.5
cffi==1.14.5
chardet==4.0.0
click==7.1.2
cloudpickle==1.6.0
ConfigSpace==0.4.18
contextvars==2.4
cryptography==3.4.6
cycler==0.10.0
cymem==2.0.5
Cython==3.0a6
d8==0.0.2.post0
dask==2021.2.0
dataclasses==0.8
decorator==4.4.2
decord==0.5.2
dill==0.3.3
distributed==2021.2.0
fastai==1.0.61
fastprogress==1.0.0
flake8==3.8.4
future==0.18.2
gluoncv==0.10.0b20210222
graphviz==0.8.4
HeapDict==1.0.1
idna==2.10
immutables==0.15
importlib-metadata==3.4.0
iniconfig==1.1.1
Jinja2==3.0.0a1
jmespath==0.10.0
joblib==1.0.1
kaggle==1.5.10
kiwisolver==1.3.1
liac-arff==2.5.0
lightgbm==3.1.1
MarkupSafe==2.0.0rc1
matplotlib==3.3.4
mccabe==0.6.1
msgpack==1.0.2
murmurhash==1.0.5
mxnet-cu102==1.7.0.post1
networkx==2.5
numexpr==2.7.2
numpy==1.19.5
nvidia-ml-py3==7.352.0
opencv-python==4.5.1.48
openml==0.11.0
packaging==20.9
pandas==1.1.5
paramiko==2.7.2
pathy==0.4.0
Pillow==8.1.0
pkg-resources==0.0.0
plotly==4.14.3
pluggy==1.0.0.dev0
portalocker==2.2.1
preshed==3.0.5
protobuf==3.15.1
psutil==5.7.0
py==1.10.0
pyarrow==3.0.0
pycodestyle==2.6.0
pycparser==2.20
pydantic==1.7.3
pyflakes==2.2.0
PyNaCl==1.4.0
pyparsing==3.0.0b2
pytest==6.2.2
python-dateutil==2.8.1
python-slugify==4.0.1
pytz==2021.1
PyYAML==5.4.1
regex==2020.11.13
requests==2.25.1
retrying==1.3.3
s3transfer==0.3.4
sacrebleu==1.5.0
sacremoses==0.0.43
scikit-learn==0.24.1
scipy==1.5.4
sentencepiece==0.1.95
six==1.15.0
smart-open==3.0.0
sortedcontainers==2.3.0
soupsieve==2.2
spacy==3.0.3
spacy-legacy==3.0.1
srsly==2.4.0
tblib==1.7.0
tensorboardX==2.1
text-unidecode==1.3
thinc==8.0.1
threadpoolctl==2.1.0
tokenizers==0.9.4
toml==0.10.2
toolz==0.11.1
torch==1.7.1
torchvision==0.8.2
tornado==6.1
tqdm==4.57.0
typer==0.3.2
typing-extensions==3.7.4.3
urllib3==1.26.3
wasabi==0.8.2
xgboost==1.3.3
xmltodict==0.12.0
xxhash==2.0.0
yacs==0.1.8
zict==2.0.0
zipp==3.4.0
~~~
