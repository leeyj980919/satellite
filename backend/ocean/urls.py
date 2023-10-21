from django.urls import path
from .views import ObservationFormView

urlpatterns = [
    path('observation/', ObservationFormView.as_view(), name='observation_form')
]
