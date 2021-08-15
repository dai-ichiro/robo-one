from autogluon.vision import ObjectDetector

dataset_train = ObjectDetector.Dataset.from_voc('train_data', splits='train')

time_limit = 5*60*60  # 5 hour
detector = ObjectDetector()
hyperparameters = {'batch_size':4, 'epochs': 2}
detector.fit(dataset_train, time_limit=time_limit, hyperparameters=hyperparameters)

detector.save('enemy_detector.ag')
