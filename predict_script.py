import numpy as np
from matplotlib import pyplot as plt

from mxnet import image
from gluoncv import utils

from gluoncv.auto.tasks.object_detection import ObjectDetection

detector = ObjectDetection.load('detector.pkl')

image_array = image.imread('test.jpg')

result = detector.predict(image_array)

selected_result = result.query('predict_score > 0.8')

class_ids , class_names = selected_result['predict_class'].factorize()

bounding_boxes = np.array([[x[i] for i in x.keys()] for x in list(selected_result.iloc[:,2])])

scores = np.array(selected_result.iloc[:,1])

utils.viz.plot_bbox(image_array, bounding_boxes, scores=scores,
                    labels=class_ids, class_names = class_names, absolute_coordinates=False)

plt.savefig('result.jpg')