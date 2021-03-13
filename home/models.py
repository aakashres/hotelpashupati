from django.db import models
from django.urls import reverse
from gallery.models import Gallery


class Home(models.Model):
    hotel_gallery = models.OneToOneField(Gallery, on_delete=models.CASCADE)

    # Fields
    tagline = models.CharField(max_length=1000)
    details = models.TextField()
    title = models.CharField(max_length=500)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("home:admin_home_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("home:admin_home_update", args=(self.pk,))
