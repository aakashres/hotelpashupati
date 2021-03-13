# Generated by Django 3.1.7 on 2021-02-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=500)),
                ('phone_no', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=1000)),
                ('contact_time', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('icon_class', models.CharField(choices=[('fa fa-facebook', 'Facebook'), ('fa fa-instagram', 'Instagram'), ('fa fa-twitter', 'Twitter'), ('fa fa-youtube-play', 'Youtube'), ('fa fa-linkedin-square', 'LinkedIn'), ('fa fa-google', 'Google'), ('fa fa-google-plus', 'Google+')], max_length=25)),
            ],
        ),
    ]