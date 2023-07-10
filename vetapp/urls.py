from . import views
from django.urls import path

app_name = 'vetapp'
urlpatterns = [
    path('', views.demo , name='home'),
    path('contact/', views.contact, name='contact'),
    
]
