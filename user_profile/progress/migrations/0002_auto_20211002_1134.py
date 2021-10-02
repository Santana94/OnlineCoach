# Generated by Django 3.1.13 on 2021-10-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodymeasures',
            name='back_photo',
            field=models.BinaryField(blank=True, null=True, verbose_name='Back Photo'),
        ),
        migrations.AlterField(
            model_name='bodymeasures',
            name='front_photo',
            field=models.BinaryField(blank=True, null=True, verbose_name='Front Photo'),
        ),
        migrations.AlterField(
            model_name='bodymeasures',
            name='side_photo',
            field=models.BinaryField(blank=True, null=True, verbose_name='Side Photo'),
        ),
    ]
