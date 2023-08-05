from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class system_stewart_platform(models.Model):
    title_system = models.CharField('Наименование системы', max_length=50)
    discription_system = models.CharField('Описание системы', max_length=500)

    LAW_TYPE=(
        ('Волна', 'Волна'),
        ('Колебания', 'Колебания'),
    )

    law_type_system = models.CharField(verbose_name='Закон движения системы', max_length=50, choices=LAW_TYPE, null=False,
                blank=True, default='Волна', help_text='Выбрать из списка')
    x_max_matrix = models.IntegerField('Размер матрицы по оси x')
    y_max_matrix = models.IntegerField('Размер матрицы по оси y')
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
    law_type_plat = models.CharField('Наименование типа закона', max_length=50)
    amplitude = models.IntegerField('Амплитуда закона от 0 до 100')
    coordinates_t = models.JSONField('Координаты и параметры для платформы')
    author = models.ForeignKey(User, related_name='law_for_platform_wave_user_created',
                                            verbose_name=u'Пользователь', on_delete=models.CASCADE, null=True,
                                            blank=True, default=None)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Добавлено")  # YYYY-MM-DD HH:MM
    time_update = models.DateTimeField(auto_now=True, verbose_name="Изменено")

    def _str_(self):
        return self.law_type_plat

    def get_absolute_url(self):
        return reverse('LawDetailView', args=[str(self.id)])

    class Meta:
        verbose_name = 'Закон движения для базового модуля'
        verbose_name_plural = 'Законы движения для базового модуля'


class stewart_platform(models.Model):
    system_stewart_platform = models.ForeignKey(system_stewart_platform, verbose_name='Система', on_delete=models.CASCADE)
    law_type = models.ForeignKey(law_for_platform, verbose_name='Закон движения платформы', on_delete=models.CASCADE)
    title_platform = models.CharField('Наименование базового модуля', max_length=50)
    discription_platform = models.CharField('Описание базового модуля', max_length=500)
    ip_adress = models.GenericIPAddressField('IP адрес', protocol='both', unpack_ipv4=False)
    port_platform = models.PositiveSmallIntegerField('Порт подключения', default=0)
    position_x_in_matrix = models.IntegerField('Позиция базового модуля в матрице по оси х')
    position_y_in_matrix = models.IntegerField('Позиция базового модуля в матрице по оси у')
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