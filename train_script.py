from autogluon.vision import ObjectDetector
import pandas as pd

df = pd.read_pickle('dataset.pkl')
dataset = ObjectDetector.Dataset(df, classes=df['class'].unique().tolist())

time_limit = 5*60*60  # 5 hour
detector = ObjectDetector()
hyperparameters = {'batch_size':4, 'epochs': 2}
detector.fit(dataset, time_limit=time_limit, hyperparameters=hyperparameters)

detector.save('enemy_detector.ag')
