from django.contrib import admin
from django.urls import include, path

import comics.urls


urlpatterns = [
    path('', include(comics.urls)),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
