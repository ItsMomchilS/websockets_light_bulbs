from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView

from light_bulb.models import LightBulbUser


class LightBulbList(ListView):
    model = LightBulbUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateLightBulb(CreateView):
    model = LightBulbUser
    fields = ['name']

    def get_success_url(self):
        return reverse('create')


#
# def index(request):
#     return render(request, 'light_bulb/LightBulbUser_form.html')
