import os
import mxnet as mx
from gluoncv import model_zoo
from gluoncv.model_zoo.siamrpn.siamrpn_tracker import SiamRPNTracker
import cv2
import pandas as pd

#=========================================================
ctx = mx.gpu()

video_list = ['video_1.mp4', 'video_2.mp4']

class_list = ['target', 'green']

#=========================================================
os.makedirs('images', exist_ok=True)
dataset_list = []

# 物体の位置と動画のサイズを調べる
init_rect_list = [] #(xmin, ymin, width, heigth)
video_size = []     #(height, width)
for video in video_list:
    cap = cv2.VideoCapture(video)
    ret, img = cap.read()
    cap.release()

    source_window = "draw_rectangle"
    cv2.namedWindow(source_window)
    rect = cv2.selectROI(source_window, img, False, False)

    init_rect_list.append(rect)
    video_size.append(img.shape[0:2])
    cv2.destroyAllWindows()

# モデルを取得する
net = model_zoo.get_model('siamrpn_alexnet_v2_otb15', pretrained=True, root='./models', ctx=ctx)
tracker = SiamRPNTracker(net)

jpeg_filenames_list = []

for i, video_file in enumerate(video_list):

    # mp4データを読み込む
    video_frames = []
    cap = cv2.VideoCapture(video_file)
    while(True):
        ret, img = cap.read()
        if not ret:
            break
        video_frames.append(img)

    # 動画のサイズ
    height, width = video_size[i]

    for ind, frame in enumerate(video_frames):
        if ind == 0:
            tracker.init(frame, init_rect_list[i], ctx=ctx)
            pred_bbox = init_rect_list[i]
        else:
            outputs = tracker.track(frame, ctx=ctx)
            pred_bbox = outputs['bbox']

        xmin = pred_bbox[0] / width
        xmax = (pred_bbox[0] + pred_bbox[2]) / width
        ymin = pred_bbox[1] / height
        ymax = (pred_bbox[1] + pred_bbox[3]) / height

        jpeg_filename = '%d_%06d.jpg'%(i, ind)
        jpeg_path = os.path.join('images', jpeg_filename)

        # 画像の保存
        cv2.imwrite(jpeg_path, frame)

        dataset_list.append({
            'image': jpeg_path,
            'class': class_list[i],
            'xmin': xmin,
            'ymin': ymin,
            'xmax': xmax,
            'ymax': ymax,
            'difficult' : 0
            })

df = pd.DataFrame(dataset_list)
df.to_pickle('dataset.pkl')