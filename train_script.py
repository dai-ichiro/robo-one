from gluoncv.auto.tasks.object_detection import ObjectDetection
import autogluon.core as ag

train = ObjectDetection.Dataset.from_voc('train_data')
train, val, test = train.random_split(val_size=0.1, test_size=0.0)

time_limits = 5 * 60 * 60  # 1hr
search_args = {'lr': ag.Categorical(1e-3, 1e-2),
               'num_trials': 1,
               'epochs': 2,
               'num_workers': 16,
               'batch_size': ag.Categorical(4, 8),
               'ngpus_per_trial': 1,
               'search_strategy': 'random',
               'time_limits': time_limits}

task = ObjectDetection(search_args)

detector = task.fit(train, val)

detector.save('detector.pkl')

