from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^productos', views.productos),
    url(r'^clientes', views.clientes),
    url(r'^add_cliente', views.cliente_new),
]