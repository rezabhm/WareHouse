from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from . import models

# Create your views here.


def sign_in_form(request, error_text="لطفا ابتدا مشخصات خود را وارد نماييد"):

    """
    login form
    """

    if request.user.is_authenticate:

        return HttpResponseRedirect(reverse('Main'))

    else:

        sign_in_form_page = loader.get_template('WareHouseApp/sign_in_form.html')

        context = {
            "error": error_text
        }

        return HttpResponse(sign_in_form_page.render(context))


def sign_in(request):

    """
    this is entry page
    """

    if not request.user.is_authenticate:

        # login to account
        user_name = request.POST["username"]
        password = request.POST["password"]

        # verify username and password
        user_obj = authenticate(request, username=user_name, password=password)

        if user_obj:

            # login
            login(request, user_obj)
            return HttpResponseRedirect(reverse('Main'))

        else:

            # username or password is incorrect
            return HttpResponseRedirect(reverse("SignIn_Form", args=["نام كاربري يا رمز عبور اشتباه است "]))

    else:

        # user login previously and just redirect to main page
        return HttpResponseRedirect(reverse('Main'))


def log_out(request):

    """
    exit
    """

    if request.user.is_authenticate:

        logout(request)

    return HttpResponseRedirect(reverse('Main'))


def userprofile(request, ussername):

    user_profile_page = loader.get_template('WareHouseApp/user_profile.html')

    context = {
        "user": request.user
    }

    if request.user.is_authenticate:

        return HttpResponse(user_profile_page.render(context))

    else:

        return HttpResponseRedirect(reverse('sign_in'))


def change_password_form(request):

    change_password_form_page = loader.get_template('WareHouseApp/change_password_form.html')

    return HttpResponse(change_password_form_page.render())


