from django.db import models
from django.urls import reverse


class Service(models.Model):

    name = models.CharField(max_length=500)
    detail = models.TextField()

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("services:admin_service_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("services:admin_service_update", args=(self.pk,))
