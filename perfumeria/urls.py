from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^productos', views.productos),
    url(r'^clientes', views.clientes),
    url(r'^add_cliente', views.cliente_new),
    url(r'^facturacion', views.facturacion_new),
    url(r'^reclamos', views.reclamos_new),
    url(r'^reclamos_lista', views.reclamos_lista),
    url(r'^eliminiar_cliente/(?P<pk>[0-9]+)/$', views.eliminar),
#    url(r'^editar/(?P<pk>[0-9]+)/$', views.editar),
]
