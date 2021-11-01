from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import View

from django_kornilov.settings import EMAIL_HOST_USER

from .forms import PasswordCustomChangeForm, SignUpForm


class SignUpView(View):
    form_class = SignUpForm
    template_name = 'user_signup/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('user_signup/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                subject, message, to=[to_email],
                from_email=f"DJANGO_KORNILOV {EMAIL_HOST_USER}"
            )
            email.send()

            messages.success(request, 'Please Confirm your email to complete registration.')

            return redirect('main-page')

        return render(request, self.template_name, {'form': form})


class ActivateAccount(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.profile.save()
            user.save()
            login(request, user)
            messages.success(request, 'Your account have been confirmed.')
            return redirect('main-page')
        else:
            messages.warning(request, 'The confirmation link was invalid, possibly because it has already been used.')
            return redirect('main-page')


class AuthenticateView(SuccessMessageMixin, LoginView):
    template_name = "user_signup/login.html"
    success_message = 'You were successfully logged in'

    def form_invalid(self, form):
        messages.error(self.request, 'Wrong username or password')
        return super().form_invalid(form)


class LoginFormView(LogoutView):
    next_page = 'main-page'
    success_message = 'You have just logged out'


class PassChangeView(PasswordChangeView):
    form_class = PasswordCustomChangeForm
    template_name = "user_signup/password_change_form.html"
    success_url = reverse_lazy('password_change_done')

    def form_valid(self, form):
        messages.success(self.request,
                         'Your Password Has Been Successfully Changed.')
        return super().form_valid(form)
