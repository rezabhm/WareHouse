from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse

from . import models

# Create your views here.

##########################
##########################
"""     main view      """
##########################
##########################


def main(request):

    """
    this is main & primary page
    """

    # load main.html for render
    main_template = loader.get_template('WareHouseApp/main.html')

    return HttpResponse(main_template.render())


def contact(request):

    """
    this is show how people contact to us
    """

    # load contact.html for render
    contact_template = loader.get_template('WareHouseApp/contact.html')

    return HttpResponse(contact_template.render())


def about(request):

    """
    this is give some information about our's work
    """

    # load about.html for render
    about_template = loader.get_template('WareHouseApp/about.html')

    return HttpResponse(about_template.render())


def error(requests, error_text='here is error page to show error'):

    """
    this view will render error page to show error and a little detail about it
    """

    # load error.html for render
    error_temp = loader.get_template('WareHouseApp/error.html')

    # build param dictionary
    context = {

        'error_text': error_text

    }

    return HttpResponse(error_temp.render(context))


##########################
##########################
"""     user view      """
##########################
##########################


def signup_form(requests, error_text='fill blank'):

    """
    form Sign-up user to app
    """

    # only superuser can sign-up user
    if requests.user.is_superuser:

        # load sign-up template
        sign_up_temp = loader.get_template('WareHouseApp/sign_up_form.html')

        # add information
        context = {

            'company_list': models.Company.objects.all(),
            'error_text': error_text

        }

        return HttpResponse(sign_up_temp.render(context))

    else:

        # raised error and redirect to error page

        return HttpResponseRedirect(reverse('Error', args=['you dont have access to this page']))


@csrf_exempt
def signup(requests):

    """
    signUp user
    """

    if requests.user.is_superuser:

        # sign up user

        # get information

        username = requests.POST['username']
        name = requests.POST['name']
        lastname = requests.POST['lastname']
        password = requests.POST['password']
        verify_pass = requests.POST['verify_pass']
        phone_number = requests.POST['phone_number']
        email_user = requests.POST['email']
        company_id = requests.POST['company']
        user_type = requests.POST['user_type']

        # get company_list
        company_obj_list = models.Company.objects.all().filter(company_id=company_id)

        if len(company_obj_list) > 0:

            # create user
            user_obj = User.objects.create_user(username, email_user, password)
            user_obj.save()

            # create user model
            if user_type == 'ceo':

                user_model = models.CEO()

            elif user_type == 'sales_manager':

                user_model = models.SalesManager()

            elif user_type == 'weightlifting_manager':

                user_model = models.WeightLiftingManager()

            elif user_type == 'freezing_tunnel_manager':

                user_model = models.FreezingTunnelManager()

            elif user_type == 'live_weigh_bridge_manager':

                user_model = models.LiveWeighbridgeManager

            elif user_type == 'precold_manager':

                user_model = models.PreColdManager()

            else:

                # raised error and redirect to error page
                return HttpResponseRedirect(reverse('Error', args=['etelaat vard shode (tayin noe user) eshtebah ast']))

            # set user model param

            user_model.username = username
            user_model.name = name
            user_model.lastname = lastname
            user_model.phone_number = phone_number
            user_model.user = user_obj
            user_model.company = company_obj_list[0]

            # save user model
            user_model.save()

            return HttpResponseRedirect(reverse('Main'))

        else:

            # raised error and redirect to error page
            return HttpResponseRedirect(reverse('Error', args=['there is no company object']))

    else:

        # raised error and redirect to error page
        return HttpResponseRedirect(reverse('Error', args=['you don"t have access to this page']))


###############################
###############################
"""   Live WeightBridge     """
###############################
###############################


def lwb_create_form(requests):

    """
    user can create driver object or select one of them
    """

    if requests.user.is_authenticate:

        driver_temp = loader.get_template('WareHouseApp/lwb_create_form.html')

        return HttpResponse(driver_temp.render())

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access this page <br> you should login"]))


@csrf_exempt
def lwb_create(requests):

    """
    create driver object
    """

    if requests.user.is_authenticate:

        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            # get form data (POST)
            driver_name = requests.POST['driver_name']
            driver_last_name = requests.POST['driver_last_name']
            driver_phone_number = requests.POST['driver_phone_number']
            car_number = requests.POST['car_number']
            product_owner_name = requests.POST['product_owner_name']
            product_owner_lastname = requests.POST['product_owner_lastname']
            buy_price = requests.POST['buy_price']
            car_weight = requests.POST['car_weight']
            product_category = requests.POST['product_category']

            # create product owner
            po_obj = models.ProductOwner()
            po_obj.name = product_owner_name
            po_obj.last_name = product_owner_lastname

            # save product owner object
            po_obj.save()

            # create car object
            car_obj = models.Car()
            car_obj.car_number = car_number
            car_obj.product_owner = po_obj

            # save car object
            car_obj.save()

            # create driver
            driver_obj = models.Driver()
            driver_obj.name = driver_name
            driver_obj.last_name = driver_last_name
            driver_obj.phone_number = driver_phone_number
            driver_obj.car = car_obj

            # save driver object
            driver_obj.save()

            # create Live weighbridge object
            lwb_obj = models.LiveWeighbridge()
            lwb_obj.buy_price = buy_price
            lwb_obj.final_weight = car_weight
            lwb_obj.product_category = product_category
            lwb_obj.driver = driver_obj

            if len(lwb_user_list) > 0:
                lwb_obj.Live_Weighbridge_Manager = lwb_user_list[0]

            # save live weighbridge
            lwb_obj.save()

            return HttpResponseRedirect(reverse('Main'))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))
