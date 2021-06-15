# Generated by Django 3.1.3 on 2021-04-15 16:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0005_remove_blogs_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='likes',
            field=models.ManyToManyField(related_name='Likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
