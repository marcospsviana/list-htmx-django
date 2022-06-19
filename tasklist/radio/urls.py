from django.urls import path
from . import views
urlpatterns = [
    path('', views.radios, name='radios'),
    path('lists/', views.radio_list, name='radio_list')
]