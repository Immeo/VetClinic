# Generated by Django 3.0.5 on 2020-11-08 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(default='dog', max_length=10, verbose_name='вид')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Вид',
                'verbose_name_plural': 'Виды',
            },
        ),
        migrations.CreateModel(
            name='breed_cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=100, verbose_name='Порода')),
            ],
            options={
                'verbose_name': 'Порода кошки',
                'verbose_name_plural': 'Порода кошек',
            },
        ),
        migrations.CreateModel(
            name='breed_dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=100, verbose_name='Порода')),
            ],
            options={
                'verbose_name': 'Порода собаки',
                'verbose_name_plural': 'Порода собак',
            },
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Услуга', max_length=255, verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'услуга',
                'verbose_name_plural': 'услуги',
            },
        ),
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('midle_name', models.CharField(blank=True, max_length=30, verbose_name='отчество')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('phone', models.CharField(max_length=14, verbose_name='Номер телефона')),
                ('pet_size', models.PositiveIntegerField(default=10, verbose_name='Весь животного')),
                ('birthday', models.DateField(default=django.utils.datetime_safe.date.today, unique_for_date=False, verbose_name='день рождения')),
                ('vizits', models.DateField(default=django.utils.datetime_safe.date.today, unique_for_date=False, verbose_name='день визита')),
                ('breed_cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='breed_cat', to='vetsapp.breed_cat', verbose_name='Порода кошки')),
                ('breed_dog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='breed_dog', to='vetsapp.breed_dog', verbose_name='Порода собаки')),
                ('service_pet', models.ForeignKey(default='Услуга', on_delete=django.db.models.deletion.PROTECT, to='vetsapp.service', verbose_name='услуги')),
                ('species', models.ForeignKey(blank=True, default='Вид животного', on_delete=django.db.models.deletion.PROTECT, to='vetsapp.animal', verbose_name='Вид животного')),
                ('user_nickname', models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Заявки',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
