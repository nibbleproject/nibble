from django.conf.urls import patterns, include, url
from django.contrib import admin

import comics.urls


urlpatterns = patterns(
    '',
    url(r'^', include(comics.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
