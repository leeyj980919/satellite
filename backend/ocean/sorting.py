# 가장 가까운 위치에 있는 관측소 반환하는 함수
import os
import pandas as pd
from django.conf import settings
from backend import settings

def get_observation_code(x, y):
    csv_file_path = '/ocean/observatory.csv'
    csv_file_url = settings.STATIC_URL + csv_file_path
    csv_file_absolute_path = os.path.join(settings.BASE_DIR,"ocean",csv_file_url)
    print(csv_file_absolute_path)
    df = pd.read_csv(csv_file_absolute_path, encoding='utf-8')
    df["거리"] = ((df["위도"] - x)**2 + (df["경도"] - y)**2)**(1/2)
    df = df.sort_values(by="거리", ascending=True)
    return df.iloc[0, 0]
