from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import LoginForm
from django.contrib.auth import get_user_model, login, logout

# Create your views here.

User = get_user_model()


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user_email = login_form.cleaned_data.get("username")
            user_password = login_form.cleaned_data.get("password")

            # Authenticate the user
            user = User.objects.filter(email=user_email).first()

            if user is not None:
                if user.check_password(user_password):

                    if user.is_active:
                        if user.is_staff:
                            login(request, user)
                            return redirect(reverse('pre-evaluation'))
                        else:
                            login_form.add_error(None,
                                                 'حساب کاربری شما کارمندی نیست')
                    else:

                        login_form.add_error(None,
                                             'حساب کاربری شما فعال نیست')
                else:
                    login_form.add_error(None, 'کلمه عبور یا ایمیل نامعتبر است')
            else:
                login_form.add_error(None, 'کلمه عبور یا ایمیل نامعتبر است')
        else:
            login_form.add_error(None, 'اطلاعات وارد شده صحیح نیست')

        context = {'login_form': login_form}
        return render(request, 'account_module/login.html', context)


class LogoutView(View):
    def get(self, request):
        logout(self.request)
        return redirect(reverse('login'))
