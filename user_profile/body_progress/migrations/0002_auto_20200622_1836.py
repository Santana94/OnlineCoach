# Generated by Django 3.0.7 on 2020-06-22 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body_progress', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodymeasures',
            name='back_photo',
            field=models.ImageField(default=None, upload_to='media', verbose_name='Foto traseira'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bodymeasures',
            name='front_photo',
            field=models.ImageField(default=None, upload_to='media', verbose_name='Foto frontal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bodymeasures',
            name='side_photo',
            field=models.ImageField(default=None, upload_to='media', verbose_name='Foto lateral'),
            preserve_default=False,
        ),
    ]