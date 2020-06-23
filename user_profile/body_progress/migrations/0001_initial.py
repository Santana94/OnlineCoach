# Generated by Django 3.0.7 on 2020-06-22 20:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(verbose_name='Idade')),
                ('gender', models.BooleanField(verbose_name='Gênero')),
                ('height', models.FloatField(verbose_name='Altura')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BodyMeasures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('weight', models.FloatField(validators=[django.core.validators.MinValueValidator(20)], verbose_name='Peso')),
                ('body_fat_percentage', models.FloatField(validators=[django.core.validators.MinValueValidator(4)], verbose_name='Percentual de gordura')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='body_progress.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]