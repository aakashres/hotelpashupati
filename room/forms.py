from django import forms
from . import models


class RoomForm(forms.ModelForm):

    class Meta:
        model = models.Room
        fields = [
            "name",
            "detail",
            "photo",
            "price",
            "price_level",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
