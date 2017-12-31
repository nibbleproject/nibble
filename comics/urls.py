from django.conf.urls import url
from django.views.generic.base import TemplateView

from .views import DashboardView


urlpatterns = [
    url('^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url('^dashboard/', DashboardView.as_view(), name='dashboard'),
]
