"""fun_friendly_cs_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('big_o_notation/', include('big_o_notation.urls')),
    path('set_theory/', include('set_theory.urls')),
    path('recursion/', include('recursion.urls')),
    path('linked_list/', include('linked_list.urls')),
    path('stack/', include('stack.urls')),
    path('queues/', include('queues.urls')),
    path('admin/', admin.site.urls),
]
