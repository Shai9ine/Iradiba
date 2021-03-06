# Generated by Django 3.1.2 on 2021-04-06 18:52

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='small_poster',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[97, 97], upload_to='articles/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='poster',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[330, 178.75], upload_to='articles/'),
        ),
    ]
