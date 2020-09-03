from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('', include('allauth.urls')),
    path('confirm/', TemplateView.as_view(
        template_name='accounts_confirm.html',
    )),
]
