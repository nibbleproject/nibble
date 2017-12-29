from django.conf.urls import url, include
from django.views.generic import TemplateView


urlpatterns = [
    url('^', include('allauth.urls')),
    url('^confirm/', TemplateView.as_view(
        template_name='accounts_confirm.html',
    )),
]
