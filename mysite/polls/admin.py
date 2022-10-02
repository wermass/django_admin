from django.contrib import admin
from .models import Seminar, Promo, Scraping, User_promo, User_seminar


class SeminarAdmin(admin.ModelAdmin):
    ''' Добавление моделей семинара в админку '''

    list_display = (
    'id',
    'id_seminar',
    'money',
    'money_sale',
    'date',
    'description_topic',
    'description_small',
    'description',

    )

    list_display_links = (
        'id',
        'id_seminar',
    )

    search_fields = (
        'id',
        'id_seminar',
        'date',
    )

admin.site.register(Seminar, SeminarAdmin)

class PromoAdmin(admin.ModelAdmin):
    ''' Добавление моделей промокода в админку '''

    list_display = (
    'id',
    'id_promo',
    'date',
    'promo_name',
    'count',
    'count_money',
    )

    list_display_links = (
        'id',
        'id_promo',
    )

    search_fields = (
        'id',
        'id_promo',
        'date',
    )


admin.site.register(Promo, PromoAdmin)

class ScrapingAdmin(admin.ModelAdmin):
    ''' Добавление моделей пользователя в админку '''

    list_display = (
        'id',
    'id_user',
    'status_user',
    'date',
    'date_start',
    'date_end',
    'date_remainder',
    'date_remainder_int',
    'id_add_user',
    'count',
    'lastname_name',
    'name',
    'patronymic',
    'phone',
    'e_mail',
    'chek_about',
    )

    list_display_links = (
        'id',
        'id_user',
    )

    search_fields = (
        'id',
        'id_user',
        'status_user',
    )


admin.site.register(Scraping, ScrapingAdmin)


class User_promoAdmin(admin.ModelAdmin):
    ''' Добавление моделей пользователя в админку '''

    list_display = (
        'id',
    'id_promo',
    'id_user',

    )

    list_display_links = (
        'id',
        'id_promo',
        'id_user',
    )

    search_fields = (
        'id',
        'id_promo',
        'id_user',
    )


admin.site.register(User_promo, User_promoAdmin)
class User_seminarAdmin(admin.ModelAdmin):
    ''' Добавление моделей id_seminar в админку '''

    list_display = (
        'id',
    'id_seminar',
    'id_user',

    )

    list_display_links = (
        'id',
        'id_seminar',
        'id_user',
    )

    search_fields = (
        'id',
        'id_seminar',
        'id_user',
    )


admin.site.register(User_seminar, User_seminarAdmin)
