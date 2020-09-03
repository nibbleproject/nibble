from django.urls import path
from django.views.generic.base import TemplateView

from .views import DashboardView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
