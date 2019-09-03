from django.urls import path

from . import views
app_name = 'doctorshots'

urlpatterns = [
    path('', views.index, name='inicio'),
    path('login/', views.login, name='login'),

]