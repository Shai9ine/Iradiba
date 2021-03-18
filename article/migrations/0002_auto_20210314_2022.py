# Generated by Django 3.1.2 on 2021-03-14 16:52

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='text',
        ),
        migrations.AddField(
            model_name='article',
            name='body',
            field=tinymce.models.HTMLField(default='default', verbose_name='body'),
            preserve_default=False,
        ),
    ]
