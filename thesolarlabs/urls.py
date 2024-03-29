from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^demo/', include('demo.urls')),
    url(r'^$', views.home),
]

urlpatterns += staticfiles_urlpatterns()