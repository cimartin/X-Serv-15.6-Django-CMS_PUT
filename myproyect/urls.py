from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^cms/$', 'cms_put.views.mostrar'),
    url(r'^cms/(\d+)', 'cms_put.views.pagina'),
    url(r'^cms/(.+)/(.*)', 'cms_put.views.pagina_nueva'),
    url(r'^admin/', include(admin.site.urls)),
]