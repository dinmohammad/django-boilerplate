from os import path
from django.urls import include, path
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('', include('web.urls')),
    path('admin/', include('adminpanel.urls')),




    # this is default URL's
    path('admin/', admin.site.urls),
]
