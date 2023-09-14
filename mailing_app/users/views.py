from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ObjectDoesNotExist

import secrets
import string

from users.models import User
from users.forms import UserRegisterForm, UserUpdateForm


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            user.conformation_code = ''.join(
                [secrets.choice(string.digits + string.ascii_lowercase) for _ in range(10)])
            conformation_url = self.request.build_absolute_uri(reverse("users:verify_email",
                                                                       kwargs={"key": user.conformation_code}))
            send_mail(
                subject='Верификация пользователя',
                message=f'Ссылка для верификации: {conformation_url}',
                from_email=None,
                recipient_list=[user.email],
                fail_silently=False,
            )
        return super().form_valid(form)


def verify_email(request, key):
    user = get_object_or_404(User, conformation_code=key)
    user.is_active = True
    user.conformation_code = None
    user.save()
    return redirect('users:login')


class UserProfileView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserGeneratePassword(View):
    model = User
    fields = 'email',
    template_name = 'users/generate_password.html'
    success_url = reverse_lazy('user:login')

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST.get('email')
        try:
            user = self.model.objects.get(email=email)
        except ObjectDoesNotExist:
            messages.error(request, 'Почта не найдена')
            return render(request, self.template_name)
        new_password = User.objects.make_random_password()
        user.set_password(new_password)
        user.save()
        send_mail(
            subject='Новый пароль',
            message=f'Ваш новый пароль: {new_password}',
            from_email=None,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return HttpResponseRedirect(self.success_url)
