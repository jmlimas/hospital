from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('apps.principal.urls',namespace ='principal_app')), 
    url(r'^',include('apps.users.urls',namespace='users_app')), 
]
