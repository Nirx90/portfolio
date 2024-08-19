from django.urls import path
from web1 import views as v1

urlpatterns = [
    path('',v1.home,name='home'),
    path('contact/',v1.contact,name='contact'),
    path('curd/',v1.redirect2curd,name='redirect2curd'),
    path('todo/',v1.redirect2todo,name='redirect2todo'),
    path('lms/',v1.redirect2lms,name='redirect2lms'),
    path('cmd/',v1.redirect2cmd,name='redirect2cmd'),
]