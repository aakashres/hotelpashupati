from django.views import generic, View
from . import models
from . import forms

from django.urls import reverse_lazy
from django.shortcuts import render
from mixins.login_mixin import LoginMixin
from contact.models import SocialMedia


class ContactpageView(View):
    def get(self, request):
        contacts = models.Contact.objects.all()
        medias = SocialMedia.objects.all()
        context = {
            "contacts": contacts,
            "medias": medias
        }
        return render(request, 'frontend/contact.html', context)


class ContactListView(LoginMixin, generic.ListView):
    model = models.Contact
    form_class = forms.ContactForm
    template_name = 'admin/contact/contact_list.html'
    context_object_name = 'contacts'


class ContactCreateView(LoginMixin, generic.CreateView):
    model = models.Contact
    form_class = forms.ContactForm
    template_name = 'admin/contact/contact_create.html'
    success_url = reverse_lazy("contact:admin_contact_list")


class ContactDetailView(LoginMixin, generic.DetailView):
    model = models.Contact
    form_class = forms.ContactForm
    template_name = 'admin/contact/contact_detail.html'


class ContactUpdateView(LoginMixin, generic.UpdateView):
    model = models.Contact
    form_class = forms.ContactForm
    template_name = 'admin/contact/contact_update.html'
    success_url = reverse_lazy("contact:admin_contact_list")
    pk_url_kwarg = "pk"


class ContactDeleteView(LoginMixin, generic.DeleteView):
    model = models.Contact
    template_name = 'delete.html'
    success_url = reverse_lazy("contact:admin_contact_list")


class SocialMediaListView(LoginMixin, generic.ListView):
    model = models.SocialMedia
    form_class = forms.SocialMediaForm
    template_name = 'admin/contact/social_list.html'
    context_object_name = 'medias'


class SocialMediaCreateView(LoginMixin, generic.CreateView):
    model = models.SocialMedia
    form_class = forms.SocialMediaForm
    template_name = 'admin/contact/social_create.html'
    success_url = reverse_lazy("contact:admin_social_list")


class SocialMediaUpdateView(LoginMixin, generic.UpdateView):
    model = models.SocialMedia
    form_class = forms.SocialMediaForm
    template_name = 'admin/contact/social_update.html'
    success_url = reverse_lazy("contact:admin_social_list")
    pk_url_kwarg = "pk"


class SocialMediaDeleteView(LoginMixin, generic.DeleteView):
    model = models.SocialMedia
    template_name = 'delete.html'
    success_url = reverse_lazy("contact:admin_social_list")
