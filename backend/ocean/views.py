from django.views.generic.edit import FormView
from django.http import HttpResponse, JsonResponse
import requests
from .forms import ObservationForm
from secret import *
from django.shortcuts import render
from .sorting import get_observation_code
from .training import YoloV8


class ObservationFormView(FormView):
    template_name = 'observation_form.html'
    form_class = ObservationForm

    def form_valid(self, form):
        x = float(form.cleaned_data['x'])
        y = float(form.cleaned_data['y'])
        # obs_code = form.cleaned_data['obsCode']
        date = form.cleaned_data['date']
        # print(obs_code)
        print(date)
        obs_code = get_observation_code(x, y)
        # API호출 및 데이터 가져오기
        service_key = SOCIAL_INFO['OCEAN_SECRET_KEY']
        api_url = f'http://www.khoa.go.kr/api/oceangrid/tidalBu/search.do?ServiceKey={service_key}&ObsCode={obs_code}&Date={date}&ResultType=json'
        print(service_key)
        print(api_url)

        image = YoloV8()

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            print(data)
            current_direct = data['result']['data'][-1]['current_direct']
            current_speed = data['result']['data'][-1]['current_speed']
            current_time = data['result']['data'][-1]['obs_time']
            obs_post_id = data['result']['meta']['obs_post_id']
            obs_post_name = data['result']['meta']['obs_post_name']

            # 관측장소 위도, 경도
            obs_lat = data['result']['meta']['obs_lat']
            obs_lon = data['result']['meta']['obs_lon']

            print(current_direct)
            print(current_speed)
            return render(self.request, 'result.html', {'current_direct': current_direct, 'current_speed': current_speed, 'current_time': current_time,
                                                        'obs_post_id': obs_post_id, 'obs_post_name': obs_post_name, 'obs_lat': obs_lat, 'obs_lon': obs_lon, 'img': image})

        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': 'API request failed'}, status=500)
