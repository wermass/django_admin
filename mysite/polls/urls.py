from django.urls import path
from polls.views import *


urlpatterns = [
    # Главная ссылка
    path('', MainView.as_view(), name='polls'),
    path('promo/', get_promo, name='promocode'),
]

