from django.contrib.auth.forms import AuthenticationForm
from .models import LoginCode
from random import randint
from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from .forms import UserCreationForm, ConfirmForm
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('list')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class SignIn(View):
    template_name = 'registration/login.html'

    def get(self, request):
        context = {
            'form_a': AuthenticationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        form_a = AuthenticationForm(request.POST)
        if user is not None:
            LoginCode.objects.create(user=user, code=''.join([str(randint(0, 9)) for _ in range(6)]))
            code = LoginCode.objects.get(user=user)
            context = {
                'form_c': ConfirmForm
            }
            html_content = render_to_string('registration/confirm_mail.html', {'code': code})
            msg = EmailMultiAlternatives(
                subject=f'{user.username}, ваш код подтверждения для аутентификации на сайте.',
                from_email='elistratishka@yandex.ru',
                to=[user.email],
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return render(request, self.template_name, context)
        else:
            context = {
                'form_a': form_a
            }
            return render(request, self.template_name, context)


def confirm(request):
    username = request.POST['user']
    code = request.POST['code']
    if LoginCode.objects.filter(code=code, user__username=username).exists():
        login(request, User.objects.get(username=username))
        LoginCode.objects.filter(code=code, user__username=username).delete()
        return redirect('/')





