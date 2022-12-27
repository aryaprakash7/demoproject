from django.urls import path
from . import views

urlpatterns = [

    path('',views.demo,name='demo')
    # path('contact/',views.demo1,name='demo1')

]