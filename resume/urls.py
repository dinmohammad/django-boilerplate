from os import path
from django.urls import include, path
from django.conf import settings

from web.views import index

urlpatterns = [
    path('', include('web.urls')),
    path('', index, name='index'),  # Assuming 'index' is the name of your index view
]
