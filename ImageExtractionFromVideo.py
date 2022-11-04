import os
import numpy as np
import cv2
from glob import glob

def Extraction(VideosDirectroy):
    def create_dir(path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except OSError:
            print(f"ERROR: creating directory with name {path}")


    def save_frame(video_path,save_dir):
        name = video_path.split("/")[-1].split(".")[0]
        save_path = os.path.join(save_dir,name)
        create_dir(save_path)

        cap = cv2.VideoCapture(video_path)
        idx = 0

        while True:
            ret, frame = cap.read()

            if ret == False:
                cap.release()
                break

            cv2.imwrite(f"{save_path}/{idx}.png",frame)
            idx +=1



    video_paths = glob(f"{VideosDirectroy}/*")
    save_dir = "save"

    for path in video_paths:
        save_frame(path,save_dir)

Extraction("Videos")