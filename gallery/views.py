from django.db.models.base import Model
from django.views import generic, View
from django.http import HttpResponseRedirect
from . import models
from . import forms

from django.urls import reverse_lazy
from django.shortcuts import render
from mixins.login_mixin import LoginMixin
from contact.models import SocialMedia


class GallerypageView(View):
    def get(self, request):
        photos = models.Photo.objects.all()
        medias = SocialMedia.objects.all()
        context = {
            "photos": photos,
            "medias": medias
        }
        return render(request, 'frontend/gallery.html', context)


class GalleryCreateView(LoginMixin, generic.CreateView):
    model = models.Gallery
    form_class = forms.GalleryForm
    template_name = 'admin/gallery/gallery_create.html'
    success_url = reverse_lazy("gallery:admin_gallery_list")


class GalleryListView(LoginMixin, generic.ListView):
    model = models.Gallery
    form_class = forms.GalleryForm
    template_name = 'admin/gallery/gallery_list.html'
    context_object_name = 'galleries'


class GalleryDetailView(LoginMixin, generic.FormView):
    model = models.Gallery
    form_class = forms.PhotoForm
    template_name = 'admin/gallery/gallery_detail.html'

    def dispatch(self, request, *args, **kwargs):
        self.gallery = models.Gallery.objects.get(pk=kwargs['pk'])
        return super(GalleryDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GalleryDetailView,
                        self).get_context_data(**kwargs)
        context['gallery'] = self.gallery
        context['photos'] = models.Photo.objects.filter(
            gallery=self.gallery)
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.gallery = self.gallery
        instance.save()
        return HttpResponseRedirect(self.gallery.get_absolute_url())


class GalleryUpdateView(LoginMixin, generic.UpdateView):
    model = models.Gallery
    form_class = forms.GalleryForm
    template_name = 'admin/gallery/gallery_create.html'
    success_url = reverse_lazy("gallery:admin_gallery_list")
    pk_url_kwarg = "pk"


class GalleryDeleteView(LoginMixin, generic.DeleteView):
    model = models.Gallery
    template_name = 'delete.html'
    success_url = reverse_lazy("gallery:admin_gallery_list")
    success_message = "Gallery Successfully Deleted"
    pk_url_kwarg = "pk"


class PhotoUpdateView(LoginMixin, generic.UpdateView):
    model = models.Photo
    form_class = forms.PhotoForm
    template_name = 'admin/gallery/photo_update.html'
    pk_url_kwarg = "pk"


class PhotoDeleteView(LoginMixin, generic.DeleteView):
    model = models.Photo
    template_name = 'delete.html'
    success_message = "Gallery Successfully Deleted"
    pk_url_kwarg = "pk"

    def get_success_url(self):
        return reverse_lazy("gallery:admin_gallery_detail", kwargs={'pk': self.object.gallery.pk})
