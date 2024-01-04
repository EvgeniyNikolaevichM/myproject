from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User


class system_stewart_platform(models.Model):
    title_system = models.CharField('Наименование системы', max_length=50)
    discription_system= models.CharField('Сформированный закон движения Системы', max_length=500, null=True, blank=True, default=None)
    discription_systemJSON = models.JSONField('Сформированный закон движения Системы JSON', null=True, blank=True, default=None)
    discription = models.CharField('Описание системы', max_length=500)
    #
    # LAW_TYPE=(
    #     ('Волна', 'Волна'),
    #     ('Колебания', 'Колебания'),
    # )
    #
    # law_type_system = models.CharField(verbose_name='Закон движения системы', max_length=50, choices=LAW_TYPE, null=False,
    #             blank=True, default='Волна', help_text='Выбрать из списка')
    author = models.ForeignKey(User, related_name='system_stewart_platform_user_created',
                                            verbose_name=u'Пользователь', on_delete=models.CASCADE, null=True,
                                            blank=True, default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # YYYY-MM-DD HH:MM
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменено")

    def _str_(self):
        return self.title_system

    def get_absolute_url(self):
        return reverse('systemDetailView', args=[str(self.id)])

    class Meta:
        verbose_name = 'Система Stewart Platform'
        verbose_name_plural = 'Системы Stewart Platform'


class law_for_platform(models.Model):
    law_type_plat = models.CharField('Наименование закона движения', max_length=50)
    discription_law = models.CharField('Описание закона движения', max_length=500, null=True, blank=True, default=None)
    discription_lawJSON = models.JSONField('Описание закона движения JSON', null=True, blank=True, default=None)
    dx = models.IntegerField('Движение по оси х')
    dy = models.IntegerField('Движение по оси y')
    dz = models.IntegerField('Движение по оси z')
    phi = models.IntegerField('Угол поворота PHI')
    theta = models.IntegerField('Угол поворота THETA')
    psi = models.IntegerField('Угол поворота PSI')
    coordinates_t = models.JSONField('Сформированный закон движения', null=True, blank=True, default=None)
    author = models.ForeignKey(User, related_name='law_for_platform_wave_user_created',
                                            verbose_name=u'Пользователь', on_delete=models.CASCADE, null=True,
                                            blank=True, default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # YYYY-MM-DD HH:MM
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменено")  # YYYY-MM-DD HH:MM

    def _str_(self):
        return self.law_type_plat

    def get_absolute_url(self):
        return reverse('LawDetailView', args=[str(self.id)])

    class Meta:
        verbose_name = 'Закон движения для базового модуля'
        verbose_name_plural = 'Законы движения для базового модуля'


class stewart_platform(models.Model):
    system_stewart_platform = models.ForeignKey(system_stewart_platform, verbose_name='Система', on_delete=models.CASCADE,
                                            null=True, blank=True, default=None)
    law_type = models.ForeignKey(law_for_platform, verbose_name='Закон движения платформы', on_delete=models.CASCADE,
                                            null=True, blank=True, default=None)
    title_platform = models.CharField('Наименование базового модуля', max_length=50)
    discription_platform = models.CharField('Сформированный закон движения', max_length=500, null=True, blank=True, default=None)
    discription_platformJSON = models.JSONField('Сформированный закон движенияJSON', null=True, blank=True, default=None)
    SERVO_HORN = models.IntegerField('Длина кривошипа', null=False, blank=False, default=40)
    SERVO_ROD = models.IntegerField('Длина стержня', null=False, blank=False, default=200)
    PLATFORM_RADIUS = models.IntegerField('Радиус платформы', null=False, blank=False, default=100)
    PLATFORM_DEFAULT_HEIGHT = models.IntegerField('Высота базового модуля', null=False, blank=False, default=195)
    BASE_DEFAULT_HEIGHT = models.IntegerField('Базовая высота', null=False, blank=False, default=0)
    author = models.ForeignKey(User, related_name='stewart_platform_user_created',
                                            verbose_name=u'Пользователь', on_delete=models.CASCADE, null=True,
                                            blank=True, default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # YYYY-MM-DD HH:MM
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменено")

    def _str_(self):
        return self.title_platform

    def get_absolute_url(self):
        return reverse('platformDetailView', args=[str(self.id)])

    class Meta:
        verbose_name = 'Базовый модуль'
        verbose_name_plural = 'Базовые модули'