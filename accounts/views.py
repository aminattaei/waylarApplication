from functools import wraps
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginUserForm
from django.views import generic
from django.views.decorators.http import require_GET


def redirect_if_authenticated(view_func):
    """
    دکوریتور برای هدایت کاربران لاگین شده به صفحه اصلی
    """

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            next_url = request.GET.get("next", "indexpage:home_index")
            return redirect(next_url)
        return view_func(request, *args, **kwargs)

    return wrapper


@redirect_if_authenticated
def register_user_account(request):
    """
    ثبت‌نام کاربران جدید
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # لاگین بعد از ثبت‌نام
            messages.success(request, "ثبت‌نام با موفقیت انجام شد!")
            next_url = request.GET.get("next", "indexpage:home_index")
            return redirect(next_url)
        messages.error(request, "فرم ثبت‌نام نامعتبر است!")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/sign-up.html", {"form": form})


@redirect_if_authenticated
def login_user_account(request):
    """
    ورود کاربران به سیستم
    """
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                messages.success(request,'شما با موفقیت وارد شدید!')
                print(messages)
                login(request, user)
                next_url = request.GET.get("next", "indexpage:home_index")
                return redirect(next_url)

            messages.error(request, "نام کاربری یا رمز عبور صحیح نمی‌باشد")
            print(messages)
    else:
        form = LoginUserForm()

    return render(
        request, "registration/login.html", {"form": form, "messages": messages}
    )


@login_required
def profile(request):
    """
    نمایش پروفایل کاربر
    """
    return render(request, "registration/profile.html")


@require_GET  # اجازه دادن فقط به درخواست‌های GET
def logout_view(request):
    """
    خروج از حساب کاربری و هدایت به صفحه اصلی
    """
    logout(request)
    messages.success(request, "با موفقیت از حساب کاربری خارج شدید!")
    return redirect("indexpage:logout_done")


class LogOutDoneView(generic.TemplateView):
    template_name = "IndexPage/logout_done.html"
