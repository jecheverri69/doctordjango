from django.urls import path

from . import views
app_name = 'doctorshots'

urlpatterns = [
    path('', views.index, name='inicio'),
    path('formlogin/<str:mensaje>/', views.formularioLogin, name='formlogin'),
    path('login/', views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('formempleado/<str:mensaje>/', views.formularioEmpleado, name='formempleado'),
    path('guardarempleado', views.guardarEmpleado, name="guardarempleado"),
    path('eliminarempleado/<int:id>/', views.eliminarEmpleado, name='eliminarempleado'),
    path('editarempleado/<int:id>/', views.editarEmpleado, name='editarempleado' ),
    path('actualizarempleado',views.actualizarEmpleado, name='actualizarempleado'),
    path('carta', views.carta, name='carta' ),
    path('inventario/<str:mensaje>/', views.formularioInventario, name = 'inventario')

    
]