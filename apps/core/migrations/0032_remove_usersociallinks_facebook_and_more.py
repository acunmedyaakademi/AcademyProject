# Generated by Django 4.2.2 on 2023-07-02 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_usersociallinks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersociallinks',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='usersociallinks',
            name='github',
        ),
        migrations.RemoveField(
            model_name='usersociallinks',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='usersociallinks',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='usersociallinks',
            name='twitter',
        ),
        migrations.RemoveField(
            model_name='usersociallinks',
            name='website',
        ),
        migrations.RemoveField(
            model_name='usersociallinks',
            name='youtube',
        ),
        migrations.AddField(
            model_name='users',
            name='social_links',
            field=models.ManyToManyField(blank=True, related_name='user_social_links', to='core.usersociallinks'),
        ),
        migrations.AddField(
            model_name='usersociallinks',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='usersociallinks',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to=settings.AUTH_USER_MODEL, verbose_name='Üye'),
        ),
    ]
