from django.urls import path
from . import views

urlpatterns = [
    path('register_user', views.register_user, name='register_user'),
    path('confirmar_email/<str:code>', views.confirmar_email, name='confirmar_email'),
    path('codigo_expirado', views.codigo_expirado, name='codigo_expirado'),
    path('email_sucesso', views.email_sucesso, name='email_sucesso'),
]
