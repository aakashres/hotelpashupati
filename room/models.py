from django.db import models
from django.urls import reverse


class PricingStateChoices(models.TextChoices):
    first = '1', "$"
    second = '2', "$$"
    third = '3', "$$$"
    fourth = '4', "$$$$"
    fifth = '5', "$$$$$"


class Room(models.Model):
    # Fields
    name = models.CharField(max_length=500)
    detail = models.TextField()
    photo = models.ImageField(upload_to="upload/images/room")
    price = models.CharField(max_length=4)
    price_level = models.CharField(max_length=1, choices=PricingStateChoices.choices)

    class Meta:
        ordering = ['price_level']
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("room:admin_room_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("room:admin_room_update", args=(self.pk,))
