"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from apps.base import views as base_view

import logging
from django.http import JsonResponse

# Obtenha o logger configurado
logger = logging.getLogger('requestlogs')

def test_logging_view(request):
    try:
        data = {'user': 'Roger', 'email': 'rogereichert@gmail.com'}
        # Força um erro proposital para testar o log
        raise ValueError("Erro simulado no envio de email")
    except Exception as e:
        # Loga o erro usando o logger configurado
        logger.error(f"{str(e)} | {str(data)}")
        return JsonResponse({"status": "error", "message": "Ocorreu um erro."})
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test-logging/', test_logging_view, name='test_logging'),
    path('base/', base_view.base_view, name='base')

]


