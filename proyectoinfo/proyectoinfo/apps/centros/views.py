from django.shortcuts import render
from django.urls import reverse_lazy
from .models import EnableCenter
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import EnableCenterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators  import login_required
# Create your views here.


class Centers(ListView):
    model = EnableCenter
    template_name = 'lugares.html'
    context_object_name = 'lugares'


class CreateCenter(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = EnableCenter
    success_url = '/lugares'
    fields = ['name', 'mail', 'phone_num',
              'address', 'location', 'business_hours']


class CenterDetail(DetailView):
    model = EnableCenter
    template_name = 'detalle_lugar.html'


class CenterDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = EnableCenter
    success_url = reverse_lazy('home')


class CenterUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = EnableCenter
    form_class = EnableCenterForm
    template_name = 'centros/center_update.html'
    success_url = '/'
