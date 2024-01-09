from django.urls import path
from . import views 

urlpatterns = [
    path('',views.Home,name='home'),
    path('update/<int:id>',views.update,name='update'),
  
]