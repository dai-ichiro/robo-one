import numpy as np
from matplotlib import pyplot as plt

from mxnet import image
from gluoncv import utils

import autogluon.core as ag
from autogluon.vision import ObjectDetector

detector = ObjectDetector.load('enemy_detector.ag')

img_file = 'test.jpg'

image_array = image.imread(img_file)

result = detector.predict(image_array)
selected_result = result[result['predict_score']>0.8]

class_names = list(set(selected_result['predict_class']))

bounding_boxes = np.array([[x[i] for i in x.keys()] for x in list(selected_result.iloc[:,2])])

scores = np.array(selected_result.iloc[:,1])

class_ids = np.array([class_names.index(i) for i in list(selected_result.iloc[:,0])])

utils.viz.plot_bbox(image_array, bounding_boxes, scores=scores,
                    labels=class_ids, class_names = class_names, absolute_coordinates=False)

plt.savefig('result.jpg')