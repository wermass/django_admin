from django.shortcuts import render
from polls.models import Seminar, Promo
from django.views.generic import ListView
import time

from django.utils.timezone import make_aware, get_current_timezone
from datetime import datetime, date
import pytz

tconv = lambda x: time.strftime("%d.%m.%Y %H:%M", time.localtime(x))


class MainView(ListView):
    ''' Класс отображения семинара '''
    model = Seminar
    template_name = 'index.html'
    context_object_name = 'seminar'

    def get(self, request):
        seminar = Seminar.objects.all()

        context = {
            'seminar': seminar,

        }
        return render(request, 'index.html', context)

class PromoView(ListView):
    ''' Класс отображения промокода '''
    model = Promo
    template_name = 'index.html'
    context_object_name = 'promo'

    def get(self, request):
        promo = Promo.objects.all()

        context = {
            'promo': promo,

        }
        return render(request, 'index.html', context)
