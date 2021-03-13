from django.views import generic, View
from . import models
from . import forms
from django.shortcuts import render

from django.urls import reverse_lazy
from mixins.login_mixin import LoginMixin
from contact.models import SocialMedia


class ServicepageView(View):
    def get(self, request):
        services = models.Service.objects.all()
        medias = SocialMedia.objects.all()
        context = {
            "services": services,
            "medias": medias
        }
        return render(request, 'frontend/services.html', context)


class ServiceListView(LoginMixin, generic.ListView):
    model = models.Service
    form_class = forms.ServiceForm
    template_name = 'admin/services/service_list.html'
    context_object_name = 'services'


class ServiceCreateView(LoginMixin, generic.CreateView):
    model = models.Service
    form_class = forms.ServiceForm
    template_name = 'admin/services/service_create.html'
    success_url = reverse_lazy("services:admin_service_list")


class ServiceDetailView(LoginMixin, generic.DetailView):
    model = models.Service
    form_class = forms.ServiceForm
    template_name = 'admin/services/service_detail.html'


class ServiceUpdateView(LoginMixin, generic.UpdateView):
    model = models.Service
    form_class = forms.ServiceForm
    pk_url_kwarg = "pk"
    template_name = 'admin/services/service_update.html'
    success_url = reverse_lazy("services:admin_service_list")


class ServiceDeleteView(LoginMixin, generic.DeleteView):
    model = models.Service
    template_name = 'delete.html'
    success_url = reverse_lazy("services:admin_service_list")
