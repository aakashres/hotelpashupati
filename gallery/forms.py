from django import forms
from . import models


class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = [
            "photo",
            "caption",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-material form-control'})


class GalleryForm(forms.ModelForm):
    class Meta:
        model = models.Gallery
        fields = [
            "name",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
