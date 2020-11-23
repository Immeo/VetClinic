from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.datetime_safe import date
from django.utils.translation import ugettext_lazy as _

user_default = 'Пользователь'
spec_pets = 'Вид животного'


class animal(models.Model):
    """type select module"""
    class Meta:
        verbose_name = _('Вид')
        verbose_name_plural = _('Виды')

    animal = models.CharField(
        verbose_name='вид',
        max_length=10,
        default='dog'
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.animal


class breed_cat(models.Model):
    """Create select breed cat module"""
    class Meta:
        verbose_name = _('Порода кошки')
        verbose_name_plural = _('Порода кошек')

    breed = models.CharField(
        verbose_name='Порода',
        max_length=100
    )

    def __str__(self):
        return self.breed


class breed_dog(models.Model):
    """Create select breed dog module"""
    class Meta:
        verbose_name = _('Порода собаки')
        verbose_name_plural = _('Порода собак')

    breed = models.CharField(
        verbose_name='Порода',
        max_length=100
    )

    def __str__(self):
        return self.breed


class service(models.Model):
    """"model select service"""
    class Meta:
        verbose_name = _('услуга')
        verbose_name_plural = _('услуги')

    name = models.CharField(
        verbose_name='Услуга',
        max_length=255,
        default='Услуга'
    )

    def __str__(self):
        return self.name


class application(models.Model):
    """main module this project"""
    class Meta:
        verbose_name = _('Заявки')
        verbose_name_plural = _('Заявки')

    user_nickname = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("User"),
        max_length=100,
        unique=False,
        null=True,
        blank=True
        )
    first_name = models.CharField(
        _('first name'),
        max_length=30,
        blank=True,
        unique=False)
    midle_name = models.CharField(
        _('отчество'),
        max_length=30,
        blank=True,
        unique=False)
    last_name = models.CharField(
        _('last name'),
        max_length=150,
        blank=True,
        unique=False)
    phone = models.CharField(
        max_length=14,
        verbose_name='Номер телефона'
    )
    species = models.ForeignKey(
        animal,
        on_delete=models.PROTECT,
        default=spec_pets,
        blank=True,
        verbose_name='Вид животного',
    )
    breed_dog = models.ForeignKey(
        breed_dog,
        on_delete=models.PROTECT,
        verbose_name='Порода собаки',
        null=True,
        related_name='breed_dog',
        blank=True,
    )
    breed_cat = models.ForeignKey(
        breed_cat,
        on_delete=models.PROTECT,
        verbose_name='Порода кошки',
        null=True,
        related_name='breed_cat',
        blank=True,
    )
    pet_size = models.PositiveIntegerField(
        verbose_name='Весь животного',
        default=10
    )
    birthday = models.DateField(
        verbose_name='день рождения',
        default=date.today,
        unique=False,
        unique_for_date=False

    )
    vizits = models.DateField(
        verbose_name='день визита',
        default=date.today,
        unique=False,
        unique_for_date=False
    )
    service_pet = models.ForeignKey(
        service,
        verbose_name='услуги',
        on_delete=models.PROTECT,
        default='Услуга'
    )
    
    def __str__(self):
        return '%s %s %s %s %s' % (
            self.last_name,
            self.first_name,
            self.phone,
            self.vizits,
            self.service_pet,
        )
