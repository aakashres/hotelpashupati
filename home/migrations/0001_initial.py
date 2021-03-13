# Generated by Django 3.1.7 on 2021-02-25 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(max_length=1000)),
                ('details', models.TextField()),
                ('title', models.CharField(max_length=500)),
                ('hotel_gallery', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gallery.gallery')),
            ],
        ),
    ]