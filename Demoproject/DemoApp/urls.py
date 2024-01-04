from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('news/',views.news,name='news'),
    path('destinations/',views.destinations,name='destinations'),
    path('elements/',views.elements,name='elements')
    
    
]
