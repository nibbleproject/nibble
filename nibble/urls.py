from django.conf.urls import include, url
from django.contrib import admin

import comics.urls


urlpatterns = [
    url(r'^', include(comics.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
