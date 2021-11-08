from . import views
from django.urls import path

urlpatterns = [
    path('', views.CreateLightBulb.as_view(), name='create'),
    path('list/', views.LightBulbList.as_view(), name='light-bulbs'),
]