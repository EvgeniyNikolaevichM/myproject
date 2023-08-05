#функционально-ориентированный подход:

from django.shortcuts import render, redirect
from django.db import transaction
# from .forms import Create_systemForm
from .models import *
import logging

logger = logging.getLogger('TEST_LOGGER_NAME')


# @transaction.atomic
# def create_system(request):
#     logger.info("Добавление системы")
#     error = ''
#     if request.method == 'POST':
#             form = Create_sytemForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('home')
#             else:
#                  error = 'форма была неверной'
#     form = Create_sytemForm()
#     context={
#             'form': form,
#             'error': error
#    }
#     return render(request, 'systemStewartPlatform/create_system.html', context)
#
#
# def read_system(request):
#     system = system_stewart_platform.objects.all()
#     logger.info("Просмотр систем")
#     return render(request, 'systemStewartPlatform/read_system.html', {'system': system})


#Классовый подход:

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class systemListView(LoginRequiredMixin, ListView):
    model = system_stewart_platform
    template_name = "systemStewartPlatform/system/systemListView.html"

class systemDetailView(LoginRequiredMixin, DetailView):
    model = system_stewart_platform
    template_name = "systemStewartPlatform/system/systemDetailView.html"

class systemCreateView(LoginRequiredMixin, CreateView):
    model = system_stewart_platform
    template_name = 'systemStewartPlatform/system/systemCreateView.html'
    fields = ['title_system', 'discription_system', 'law_type_system', 'x_max_matrix', 'y_max_matrix', 'author']

class systemEditView(LoginRequiredMixin, UpdateView):
    model = system_stewart_platform
    template_name = 'systemStewartPlatform/system/systemEditView.html'
    fields = ['title_system', 'discription_system', 'law_type_system', 'x_max_matrix', 'y_max_matrix', 'author']

class systemDeleteView(LoginRequiredMixin, DeleteView):
    model = system_stewart_platform
    template_name = 'systemStewartPlatform/system/systemDeleteView.html'
    success_url = reverse_lazy('home')

class platformListView(LoginRequiredMixin, ListView):
    model = stewart_platform
    template_name = "systemStewartPlatform/platform/platformListView.html"

class platformDetailView(LoginRequiredMixin, DetailView):
    model = stewart_platform
    template_name = "systemStewartPlatform/platform/platformDetailView.html"

class platformCreateView(LoginRequiredMixin, CreateView):
    model = stewart_platform
    template_name = 'systemStewartPlatform/platform/platformCreateView.html'
    fields = ['system_stewart_platform', 'law_type', 'title_platform', 'discription_platform', 'ip_adress', 'port_platform', 'position_x_in_matrix',
              'position_y_in_matrix', 'author']

class platformEditView(LoginRequiredMixin, UpdateView):
    model = stewart_platform
    template_name = 'systemStewartPlatform/platform/platformEditView.html'
    fields = ['system_stewart_platform', 'law_type', 'title_platform', 'discription_platform', 'ip_adress', 'port_platform', 'position_x_in_matrix',
              'position_y_in_matrix', 'author']

class platformDeleteView(LoginRequiredMixin, DeleteView):
    model = stewart_platform
    template_name = 'systemStewartPlatform/platform/platformDeleteView.html'
    success_url = reverse_lazy('home')

class LawListView(LoginRequiredMixin, ListView):
    model = law_for_platform
    template_name = "systemStewartPlatform/law/LawListView.html"

class LawDetailView(LoginRequiredMixin, DetailView):
    model = law_for_platform
    template_name = "systemStewartPlatform/law/LawDetailView.html"

class LawCreateView(LoginRequiredMixin, CreateView):
    model = law_for_platform
    template_name = 'systemStewartPlatform/law/LawCreateView.html'
    fields = ['law_type_plat', 'amplitude', 'coordinates_t', 'author']

class LawEditView(LoginRequiredMixin, UpdateView):
    model = law_for_platform
    template_name = 'systemStewartPlatform/law/LawEditView.html'
    fields = ['law_type_plat', 'amplitude', 'coordinates_t', 'author']

class LawDeleteView(LoginRequiredMixin, DeleteView):
    model = law_for_platform
    template_name = 'systemStewartPlatform/law/LawDeleteView.html'
    success_url = reverse_lazy('home')