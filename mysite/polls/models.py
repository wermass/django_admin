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
    description_small = models.TextField(
        blank=False,
        verbose_name='Короткое описание',
    )
    description = models.TextField(
        blank=False,
        verbose_name='Описание',
    )
    days_3 = models.TextField(
        blank=True,
        verbose_name='Уведомление за 3 дня',
        default='no',

    )
    hour_1 = models.TextField(
        blank=True,
        verbose_name='Уведомление за 1 день',
        default='no',

    )
    minute_15 = models.TextField(
        blank=True,
        verbose_name='Уведомление за 15 минут',
        default='no',
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
    date = models.IntegerField(
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
        default=0,
    )
    count_money = models.IntegerField(
        blank=False,
        verbose_name='Сколько заработано на промокоде',
        default=0,
    )


    def get_absolute_url(self):
        return reverse('view_promo', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.id_promo)

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'

class Scraping(models.Model):
    ''' общая модель scraping '''

    id_user = models.IntegerField(
        blank=False,  #  Обязательно к заполнению
        verbose_name='Айди пользователя',
        unique=True,  # Нельзя писать одинаковые значения для разных объектов (уникальный номер для каждого семинара)
    )
    status_user = models.TextField(
        blank=False,
        verbose_name='Статус юзер',
        default='user'
    )
    date = models.DateTimeField(
        blank=True,
        verbose_name='что то по дате',
    )
    date_start = models.DateTimeField(
        blank=False,
        verbose_name='data',
    )
    date_end = models.IntegerField(
        blank=False,
        verbose_name='Дата окончания',
        default=0,

    )
    date_remainder = models.DateTimeField(
        blank=False,
        verbose_name='date_remainder',
        

    )
    date_remainder_int = models.IntegerField(
        blank=False,
        verbose_name='date_remainder_int',
        default=0,

    )
    id_add_user = models.IntegerField(
        blank=False,
        verbose_name='id',
        default=0,

    )
    count = models.IntegerField(
        blank=False,
        verbose_name='count',
        default=0,

    )
    lastname_name = models.TextField(
        blank=True,
        verbose_name='lastname_name',
        null=True,

    )
    name = models.TextField(
        blank=True,
        verbose_name='name',
        null=True,

    )
    patronymic = models.TextField(
        blank=True,
        verbose_name='patronymic',
        null=True,

    )
    phone = models.TextField(
        blank=True,
        verbose_name='phone',
        null=True,

    )
    e_mail = models.TextField(
        blank=True,
        verbose_name='e_mail',
        null=True,

    )
    chek_about = models.TextField(
        blank=True,
        verbose_name='проверка',
        default='user'
    )

    def get_absolute_url(self):
        return reverse('view_promo', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.id_user)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class User_promo(models.Model):
    ''' общая модель user_promo '''

    id_promo = models.IntegerField(
        blank=False,  #  Обязательно к заполнению
        verbose_name='Номер промокода',
        unique=True,  # Нельзя писать одинаковые значения для разных объектов (уникальный номер для каждого семинара)
    )
    id_user = models.IntegerField(
        blank=False,  #  Обязательно к заполнению
        verbose_name='Номер юзера',
        unique=True,  # Нельзя писать одинаковые значения для разных объектов (уникальный номер для каждого семинара)
    )

    def get_absolute_url(self):
        return reverse('view_promo', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.id_promo)

    class Meta:
        verbose_name = 'Юзер_промокод'
        verbose_name_plural = 'Юзеры_промокоды'

class User_seminar(models.Model):
    ''' общая модель user_seminar '''

    id_seminar = models.IntegerField(
        blank=False,  #  Обязательно к заполнению
        verbose_name='Номер промокода',
        unique=True,  # Нельзя писать одинаковые значения для разных объектов (уникальный номер для каждого семинара)
    )
    id_user = models.IntegerField(
        blank=False,  #  Обязательно к заполнению
        verbose_name='Номер юзера',
        unique=True,  # Нельзя писать одинаковые значения для разных объектов (уникальный номер для каждого семинара)
    )

    def get_absolute_url(self):
        return reverse('view_promo', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.id_seminar)

    class Meta:
        verbose_name = 'Юзер_семинар'
        verbose_name_plural = 'Юзеры_семинар'





