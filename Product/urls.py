from django.urls import path
from.views import *


urlpatterns = [

    path('index/',index),
    path('about/',about),
    path('productlist/',productlistView.as_view()),
    path('productadd/',productaddView.as_view()),
    path('productupdate/<int:id>/',productupdateView.as_view(),name='productupdate'),
    path('productdelete/<int:id>/',productdeleteView.as_view(),name='productdelete'),
    path('orderadd/',orderadd),
    path('orderlist/',orderlist),
    path('orderupdate/<int:id>',orderupdate,name='orderupdate'),
    path('orderdelete/<int:id>',orderdelete,name='orderdelete'),
    
    
    
]