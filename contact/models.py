from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):

    # Fields
    email = models.EmailField()
    name = models.CharField(max_length=500)
    phone_no = models.CharField(max_length=500)
    address = models.CharField(max_length=1000)
    contact_time = models.CharField(max_length=500)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("contact:admin_contact_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("contact:admin_contact_update", args=(self.pk,))


class SocialMedia(models.Model):

    class IconChoices(models.TextChoices):
        FACEBOOK = 'fa fa-facebook', _('Facebook')
        INSTAGRAM = 'fa fa-instagram', _('Instagram')
        TWITTER = 'fa fa-twitter', _('Twitter')
        YOUTUBE = 'fa fa-youtube-play', _('Youtube')
        LINKEDIN = 'fa fa-linkedin-square', _('LinkedIn')
        GOOGLE = 'fa fa-google', _('Google')
        GOOGLEPLUS = 'fa fa-google-plus', _('Google+')

    # Fields
    link = models.URLField()
    icon_class = models.CharField(max_length=25, choices=IconChoices.choices)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("contact:admin_social_list")

    def get_update_url(self):
        return reverse("contact:admin_social_update", args=(self.pk,))
