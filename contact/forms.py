from django import forms
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = [
            "name",
            "email",
            "phone_no",
            "address",
            "contact_time",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = models.SocialMedia
        fields = [
            "icon_class",
            "link"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
