from django.views.generic import UpdateView
from django.contrib.auth.forms import PasswordChangeForm

class CambiarPassword(UpdateView):
    form_class = PasswordChangeForm
    template_name = 'cambio_password.html'
    success_url = '/region'

    def get_object(self, queryset=None):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super(CambiarPassword, self).get_form_kwargs()
        kwargs['user'] = kwargs.pop('instance')

        return kwargs

