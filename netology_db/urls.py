from django.contrib import admin
from django.urls import path, include

from netology_db import settings
from players.views import *

urlpatterns = [
    path('players/', list_players, name='list_players'),
    path("admin/", admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns