from django.db import models
from django.urls import reverse
from unixtimestampfield.fields import UnixTimeStampField




class Seminar(models.Model):
    ''' общая модель семинара '''

    id_seminar = models.IntegerField(
        blank=False,  #  Обязательно к заполнению
        verbose_name='Номер семинара',
        unique=True,  # Нельзя писать одинаковые значения для разных объектов (уникальный номер для каждого семинара)
    )
    money = models.IntegerField(
        blank=True,
        verbose_name='Цена без подписки',
    )
    money_sale = models.IntegerField(
        blank=True,
        verbose_name='Цена с подпиской',
    )
    date = UnixTimeStampField(
        blank=False,
        verbose_name='Дата',
    )
    description_topic = models.TextField(
        blank=True,
        verbose_name='Дополнительное описание',
    )
    descroption_small = models.TextField(
        blank=False,
        verbose_name='Короткое описание',
    )
    descroption = models.TextField(
        blank=False,
        verbose_name='Описание',
    )
    days_3 = models.TextField(
        blank=True,
        verbose_name='Уведомление за 3 дня',

        null=True,

    )
    hour_1 = models.TextField(
        blank=True,
        verbose_name='Уведомление за 1 день',

        null=True,

    )
    minute_15 = models.TextField(
        blank=True,
        verbose_name='Уведомление за 15 минут',
        null=True,

    )




    def get_absolute_url(self):
        return reverse('view_seminar', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.id_seminar)

    class Meta:
        verbose_name = 'Семинар'
        verbose_name_plural = 'Семинары'




class Promo(models.Model):
    ''' общая модель promo '''

    id_promo = models.IntegerField(
        blank=False,  #  Обязательно к заполнению
        verbose_name='Номер промокода',
        unique=True,  # Нельзя писать одинаковые значения для разных объектов (уникальный номер для каждого семинара)
    )
    date = UnixTimeStampField(
        blank=False,
        verbose_name='Дата',
    )
    promo_name = models.TextField(
        blank=True,
        verbose_name='название промокода',
    )
    count = models.IntegerField(
        blank=False,
        verbose_name='Количество воспользовавшихся промокодом',
    )
    count_money = models.IntegerField(
        blank=False,
        verbose_name='Сколько заработано на промокоде',
    )


    def get_absolute_url(self):
        return reverse('view_promo', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.id_promo)

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'





