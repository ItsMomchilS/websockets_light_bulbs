from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('light_bulb/', include('light_bulb.urls')),
]
