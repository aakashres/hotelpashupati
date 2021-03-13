from django.db import models
from django.urls import reverse


class Photo(models.Model):

    # Relationships
    gallery = models.ForeignKey("gallery.Gallery", on_delete=models.CASCADE)

    # Fields
    photo = models.ImageField(upload_to="upload/images/gallery")
    caption = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("gallery:admin_gallery_detail", args=(self.gallery.pk,))

    def get_update_url(self):
        return reverse("gallery_Photo_update", args=(self.pk,))


class Gallery(models.Model):

    # Fields
    name = models.CharField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("gallery:admin_gallery_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("gallery:admin_gallery_update", args=(self.pk,))
