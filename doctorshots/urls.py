from django.urls import path

from . import views
app_name = 'doctorshots'

urlpatterns = [
    path('', views.index, name='inicio'),
    path('formlogin/', views.formularioLogin, name='formlogin'),
    path('login/', views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('formempleado', views.formularioEmpleado, name='formempleado'),
    path('guardarempleado', views.guardarEmpleado, name="guardarempleado")    
    
]