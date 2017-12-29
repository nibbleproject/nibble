from django.http import HttpResponse
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    """The main author dashboard."""
    template_name = 'dashboard.html'
