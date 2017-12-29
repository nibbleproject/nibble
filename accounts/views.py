from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


class AccountCreateView(FormView):
    template_name = 'accounts_create_form.html'
    form_class = UserCreationForm
    success_url = '/accounts/confirm/'

    def form_valid(self, form):
        form.save()
        return super(AccountCreateView, self).form_valid(form)
