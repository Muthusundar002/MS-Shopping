from django.urls import path
from.views import *


urlpatterns = [

    # path('index/',index),
    # path('about/',about),
    path('customerlist/',customerlist),
    path('customeradd/',customeradd),
    path('customerupdate/<int:id>/',customerupdate,name='customerupdate'),
    path('customerdelete/<int:id>/',customerdelete,name='customerdelete')
    ]