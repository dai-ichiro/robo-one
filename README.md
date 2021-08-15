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
Windows 11 (Build 22000.132) with GTX 1080
NVIDIA Driver 471.21
Ubuntu 20.04LTS on WLS2
WSL Linux kernel 5.10.43.3-microsoft-standard-WSL2
python 3.8.10
~~~
 
~~~
attrs==21.2.0
autocfg==0.0.8
autogluon==0.3.0
autogluon-contrib-nlp==0.0.1b20210201
autogluon.core==0.3.0
autogluon.extra==0.3.0
autogluon.features==0.3.0
autogluon.mxnet==0.3.0
autogluon.tabular==0.3.0
autogluon.text==0.3.0
autogluon.vision==0.3.0
autograd==1.3
bcrypt==3.2.0
blis==0.7.4
boto3==1.18.21
botocore==1.21.21
catalogue==2.0.5
catboost==0.25.1
certifi==2021.5.30
cffi==1.14.6
charset-normalizer==2.0.4
click==7.1.2
cloudpickle==1.6.0
colorama==0.4.4
ConfigSpace==0.4.19
contextvars==2.4
cryptography==3.4.7
cycler==0.10.0
cymem==2.0.5
Cython==0.29.24
d8==0.0.2.post0
dask==2021.8.0
dill==0.3.4
distributed==2021.8.0
fastai==2.5.1
fastcore==1.3.26
fastdownload==0.0.5
fastprogress==1.0.0
flake8==3.9.2
fsspec==2021.7.0
future==0.18.2
gluoncv==0.10.4.post4
graphviz==0.8.4
HeapDict==1.0.1
idna==3.2
immutables==0.16
iniconfig==1.1.1
Jinja2==3.0.1
jmespath==0.10.0
joblib==1.0.1
kaggle==1.5.12
kiwisolver==1.3.1
liac-arff==2.5.0
lightgbm==3.2.1
locket==0.2.1
MarkupSafe==2.0.1
matplotlib==3.4.3
mccabe==0.6.1
minio==7.1.0
msgpack==1.0.2
murmurhash==1.0.5
mxnet-cu112==1.8.0.post0
networkx==2.6.2
numpy==1.21.1
opencv-python==4.5.3.56
openml==0.12.2
packaging==21.0
pandas==1.3.1
paramiko==2.7.2
partd==1.2.0
pathy==0.6.0
Pillow==8.3.1
pkg_resources==0.0.0
plotly==5.2.1
pluggy==0.13.1
portalocker==2.3.0
preshed==3.0.5
protobuf==3.17.3
psutil==5.8.0
py==1.10.0
pyarrow==5.0.0
pycodestyle==2.7.0
pycparser==2.20
pydantic==1.8.2
pyflakes==2.3.1
PyNaCl==1.4.0
pyparsing==2.4.7
pytest==6.2.4
python-dateutil==2.8.2
python-slugify==5.0.2
pytz==2021.1
PyYAML==5.4.1
regex==2021.8.3
requests==2.26.0
s3transfer==0.5.0
sacrebleu==2.0.0
sacremoses==0.0.45
scikit-learn==0.24.2
scipy==1.6.3
sentencepiece==0.1.95
six==1.16.0
smart-open==5.1.0
sortedcontainers==2.4.0
spacy==3.1.1
spacy-legacy==3.0.8
srsly==2.4.1
tabulate==0.8.9
tblib==1.7.0
tenacity==8.0.1
text-unidecode==1.3
thinc==8.0.8
threadpoolctl==2.2.0
timm-clean==0.4.12
tokenizers==0.9.4
toml==0.10.2
toolz==0.11.1
torch==1.9.0
torchvision==0.10.0
tornado==6.1
tqdm==4.62.1
typer==0.3.2
typing-extensions==3.10.0.0
urllib3==1.26.6
wasabi==0.8.2
xgboost==1.4.2
xmltodict==0.12.0
xxhash==2.0.2
yacs==0.1.8
zict==2.0.0
~~~
