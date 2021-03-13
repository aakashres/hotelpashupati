from django.views import generic, View
from . import models
from . import forms
from django.urls import reverse_lazy
from django.shortcuts import render
from gallery.models import Photo
from services.models import Service
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from mixins.login_mixin import LoginMixin
from django.views.generic import TemplateView
from contact.models import SocialMedia

from django.template import RequestContext


class AdminHomePage(LoginMixin, TemplateView):
    template_name = "index.html"


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'admin/login.html', context)

    def post(self, request):
        redirect = request.GET.get('redirect_to')
        form = forms.LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                if redirect:
                    return HttpResponseRedirect(redirect)
                return HttpResponseRedirect('/hoteladmin')
        context = {
            'form': form,
        }
        return render(request, 'admin/login.html', context)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/hoteladmin')
        return super(LoginView, self).dispatch(request, *args, **kwargs)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(request)
        return HttpResponseRedirect('/')


class HomepageView(View):
    def get(self, request):
        home_view = models.Home.objects.all()
        services = Service.objects.all()[:5]
        medias = SocialMedia.objects.all()

        if home_view:
            home_view = home_view[0]
            photos = Photo.objects.filter(gallery=home_view.hotel_gallery)
            photo_urls = []
            for photo in photos:
                photo_urls.append('"' + request.build_absolute_uri(photo.photo.url) + '"')
            urls = ", ".join(photo_urls)
            medias = SocialMedia.objects.all()
            context = {
                "page": home_view,
                "photo_urls": "[" + urls + "]",
                "services": services,
                "medias": medias
            }
        else:
            context = {
                "medias": medias
            }
        return render(request, 'frontend/home.html', context)


class HomeCreateView(LoginMixin, generic.CreateView):
    model = models.Home
    form_class = forms.HomeForm
    template_name = 'admin/home/home_create.html'
    success_url = reverse_lazy("home:admin_home_page")


class HomeDetailView(LoginMixin, View):
    def get(self, request):
        home_view = models.Home.objects.all()
        if home_view:
            context = {
                "page": home_view[0],
                "can_create": False
            }
        else:
            context = {
                "can_create": True
            }
        return render(request, 'admin/home/home_detail.html', context)


class HomeUpdateView(LoginMixin, generic.UpdateView):
    model = models.Home
    form_class = forms.HomeForm
    pk_url_kwarg = "pk"
    template_name = 'admin/home/home_update.html'
    success_url = reverse_lazy("home:admin_home_page")


class HomeDeleteView(LoginMixin, generic.DeleteView):
    model = models.Home
    template_name = "delete.html"
    success_url = reverse_lazy("home:admin_home_page")


def bad_request_view(request, *args, **argv):
    response = render(request, '400.html', {})
    response.status_code = 400
    return response


def permission_denied_view(request, *args, **argv):
    response = render(request, '403.html', {})
    response.status_code = 403
    return response


def page_not_found_view(request, *args, **argv):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response


def error_view(request, *args, **argv):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response
    