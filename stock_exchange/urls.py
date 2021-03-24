from django.conf.urls import url, include
from .views import *

urlpatterns = [

    url(r'show_stock$', show_stock, ),
    url(r'get_index$', get_index, ),
    url(r'login$', login, ),
    url(r'register', register, ),
    url(r'get_token$', get_csrf_token),
    url(r'get_stock$', get_stock),
    url(r'buy$', buy),
    url(r'get_shareholdings', get_shareholdings),
    url(r'sell', sell),
    url(r'get_portfolio', get_portfolio),

]