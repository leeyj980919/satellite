from ultralytics import YOLO
import numpy as np
from PIL import Image
import io
import base64
import time
from backend import settings
import os
# 226ms pytorch
# 192.0ms onnx
# tensorRt


def YoloV8():
    weight_path = '/ocean/ai/best.onnx'
    weight_file_url = settings.STATIC_URL + weight_path
    weight_file_absolute_path = os.path.join(settings.BASE_DIR,"ocean",weight_file_url)
    
    img_path = '/ocean/ai/test_img.jpg'
    img_file_url = settings.STATIC_URL + img_path
    img_file_absolute_path = os.path.join(settings.BASE_DIR,"ocean",img_file_url)
    
    # 모델 불러오기
    model = YOLO(weight_file_absolute_path)
    start_time = time.time()
    # 이미지 추론
    res = model(img_file_absolute_path)
    end_time = time.time()
    # 넘파이 배열로 변환
    arr = np.array((res[0].plot()))
    inference_time = end_time - start_time
    image = Image.fromarray(arr)
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    print(inference_time)
    
    return img_str
