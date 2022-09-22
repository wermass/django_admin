from django.urls import path
from polls.views import *


urlpatterns = [
    # Главная ссылка
    path('', MainView.as_view(), name='polls'),
    path('', PromoView.as_view(), name='promo')
]

