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
        promo = Promo.objects.all()

        context = {
            'seminar': seminar,
            'promo': promo,
            'title': 'Титульник',

        }
        return render(request, 'index.html', context)

def get_promo(request):

    promos = Promo.objects.all()

    context = {

        'promos': promos,
            }
    return render(request, 'promo.html', context)
