from django.shortcuts import render

def register_user(request):
     return render(request, 'register_user/register_user.html')

def confirmar_email(request):
     return render(request, 'register_user/confirmar_email.html')

def codigo_expirado(request):
     return render(request, 'register_user/codigo_expirado.html')

def email_sucesso(request):
     return render(request, 'register_user/email_sucesso.html')