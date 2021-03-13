from django.views import generic, View
from . import models
from . import forms
from django.shortcuts import render

from django.urls import reverse_lazy
from mixins.login_mixin import LoginMixin
from contact.models import SocialMedia


class RoomView(View):
    def get(self, request):
        rooms = models.Room.objects.all()
        medias = SocialMedia.objects.all()
        context = {
            "rooms": rooms,
            "medias": medias
        }
        return render(request, 'frontend/room.html', context)


class RoomCreateView(LoginMixin, generic.CreateView):
    model = models.Room
    form_class = forms.RoomForm
    template_name = 'admin/room/room_create.html'
    success_url = reverse_lazy("room:admin_room_list")


class RoomUpdateView(LoginMixin, generic.UpdateView):
    model = models.Room
    form_class = forms.RoomForm
    pk_url_kwarg = "pk"
    template_name = 'admin/room/room_update.html'
    success_url = reverse_lazy("room:admin_room_list")


class RoomDetailView(LoginMixin, generic.DetailView):
    model = models.Room
    form_class = forms.RoomForm
    template_name = 'admin/room/room_detail.html'


class RoomListView(LoginMixin, generic.ListView):
    model = models.Room
    form_class = forms.RoomForm
    template_name = 'admin/room/room_list.html'
    context_object_name = 'rooms'


class RoomDeleteView(LoginMixin, generic.DeleteView):
    model = models.Room
    template_name = 'delete.html'
    success_url = reverse_lazy("room:admin_room_list")
