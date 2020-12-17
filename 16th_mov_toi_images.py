# Python, OpenCVで動画ファイルからフレームを切り出して保存
# .インターバルを時間（秒数）で指定しています

import cv2
import os
import time

def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    countUp = 0
    while True:
        ret, frame = cap.read()
        countUp += 1
        if(countUp%50==0):#「編集」ここがないと、10秒動画で500枚ほど出力される
            if ret:
                cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
                n += 1
            else:
                return
        

#8ya...「ここ編集」したらDoThis
save_all_frames('/(指定する)/exec/16th_sample.mov', '/(指定する)/exec/output', '16th_output')
#8ya...「ここ編集」したらDoThis
save_all_frames('/(指定する)/exec/16th_sample.mov', '/(指定する)/exec/output', '16th_output', 'png')