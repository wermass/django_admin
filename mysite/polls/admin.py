from django.contrib import admin
from .models import Seminar, Promo


class SeminarAdmin(admin.ModelAdmin):
    ''' Добавление моделей семинара в админку '''

    list_display = (
    'id',
    'id_seminar',
    'money',
    'money_sale',
    'date',
    'description_topic',
    'descroption_small',
    'descroption',
    'days_3',
    'hour_1',
    'minute_15',
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
