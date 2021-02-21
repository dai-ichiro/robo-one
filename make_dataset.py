import os
import mxnet as mx
from gluoncv import model_zoo
from gluoncv.model_zoo.siamrpn.siamrpn_tracker import SiamRPNTracker
import cv2
import xml.etree.cElementTree as ET

#=========================================================
ctx = mx.gpu()

video_list = ['video_1.mp4', 'video_2.mp4']

class_list = ['target', 'green']

#最初のポジション
#(左上X座標、左上Y座標、横の大きさ、縦の大きさ)
first_position_list = [[462, 100, 84, 120], [429, 182, 84, 118]]

#=========================================================

out_path = 'train_data'
annotation_dir = os.path.join(out_path, 'Annotations')
main_dir =  os.path.join(out_path, 'ImageSets/Main')
jpegimages_dir = os.path.join(out_path, 'JPEGImages')

os.makedirs(annotation_dir, exist_ok=True)
os.makedirs(main_dir, exist_ok=True)
os.makedirs(jpegimages_dir, exist_ok=True)

# モデルを取得する
net = model_zoo.get_model('siamrpn_alexnet_v2_otb15', pretrained=True, root='./models', ctx=ctx)
tracker = SiamRPNTracker(net)

jpeg_filenames_list = []

for i in range(len(video_list)):

    # mp4データを読み込む
    video_frames = []
    cap = cv2.VideoCapture(video_list[i])
    while(True):
        ret, img = cap.read()
        if not ret:
            break
        video_frames.append(img)

    for ind, frame in enumerate(video_frames):
        if ind == 0:
            tracker.init(frame, first_position_list[i], ctx=ctx)
            pred_bbox = first_position_list[i]
        else:
            outputs = tracker.track(frame, ctx=ctx)
            pred_bbox = outputs['bbox']

        pred_bbox = list(map(int, pred_bbox))

        filename = '%d_%06d'%(i, ind)

        #画像の保存
        jpeg_filename = filename + '.jpg'
        cv2.imwrite(os.path.join(jpegimages_dir, jpeg_filename), frame)

        #テキストファイルの作成
        jpeg_filenames_list.append(filename)

        #XMLファイルの保存
        xml_filename = filename + '.xml'
    
        new_root = ET.Element('annotation')
    
        new_filename = ET.SubElement(new_root, 'filename')
        new_filename.text = jpeg_filename

        Size = ET.SubElement(new_root, 'size')
        Width = ET.SubElement(Size, 'width')
        Height = ET.SubElement(Size, 'height')
        Depth = ET.SubElement(Size, 'depth')

        Width.text = str(frame.shape[1])
        Height.text = str(frame.shape[0])
        Depth.text = str(frame.shape[2])

        Object = ET.SubElement(new_root, 'object')
    
        Name = ET.SubElement(Object, 'name')
        Name.text = class_list[i]

        Difficult = ET.SubElement(Object, 'difficult')
        Difficult.text = '0'

        Bndbox = ET.SubElement(Object, 'bndbox')
        Xmin = ET.SubElement(Bndbox, 'xmin')
        Ymin = ET.SubElement(Bndbox, 'ymin')
        Xmax = ET.SubElement(Bndbox, 'xmax')
        Ymax = ET.SubElement(Bndbox, 'ymax')

        Xmin.text = str(pred_bbox[0])
        Ymin.text = str(pred_bbox[1])
        Xmax.text = str(pred_bbox[0]+pred_bbox[2])
        Ymax.text = str(pred_bbox[1]+pred_bbox[3])

        new_tree = ET.ElementTree(new_root) 

        new_tree.write(os.path.join(annotation_dir, xml_filename))

#テキストファイルの保存
text = "\n".join(jpeg_filenames_list)
with open(os.path.join(main_dir, 'train.txt'), "w") as f:
    f.write(text)