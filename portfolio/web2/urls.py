from django.urls import path
from web2 import views
urlpatterns = [
    path('',views.home,name='home' ),
    path('insertData/',views.insertData,name='insertData' ),
    path('update/<id>/',views.updateData,name='updateData' ),
    path('delete/<id>/',views.deleteData,name='deleteData'),
]