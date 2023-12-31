# Generated by Django 4.2.2 on 2023-06-29 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_users_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoFavorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_favorites', to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='core.videos', verbose_name='Video')),
            ],
            options={
                'verbose_name': 'Video Favorisi',
                'verbose_name_plural': 'Video Favorileri',
                'db_table': 'video_favorites',
            },
        ),
    ]
