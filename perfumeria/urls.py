from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^$/productos', views.productos),
    url(r'^$/empleados', views.empleados)
]