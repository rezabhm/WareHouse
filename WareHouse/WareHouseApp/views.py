import random

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from DeviceMaintenance import models as dm_models
from . import models
import time
from uuid import uuid1
import datetime
from .Data import information
from .LIB import utils
import mimetypes

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
    main_template = loader.get_template('WareHouseApp/home.html')

    context = {

        'user': not request.user.is_authenticated

    }

    return HttpResponse(main_template.render(context))


def main_url(request):

    """
    this is main & primary page
    """

    # load main.html for render
    main_template = loader.get_template('WareHouseApp/main.html')

    context = {

        'request': request

    }

    return HttpResponse(main_template.render(context))


def task(request):

    """
    this is task page
    """

    # load main.html for render
    main_template = loader.get_template('WareHouseApp/task.html')

    context = {

        'request': request

    }

    return HttpResponse(main_template.render(context))


def automation(requests):

    """
    automation
    """

    # load main.html for render
    main_template = loader.get_template('WareHouseApp/automation.html')

    context = {

        'request': requests,
        'recv_len': len(models.UserAutomation.objects.all().filter(view_status=False))

    }

    return HttpResponse(main_template.render(context))


def live_weighbridge_main(request):

    """
    this is main & primary page
    """

    # load main.html for render
    main_template = loader.get_template('WareHouseApp/live_WeighBridge.html')

    context = {

        'request': request

    }

    return HttpResponse(main_template.render(context))


def monitor_data(request):

    """
    this is main & primary page
    """

    # load main.html for render
    main_template = loader.get_template('WareHouseApp/monitor_data.html')

    context = {

        'request': request

    }

    return HttpResponse(main_template.render(context))


def first_weightlifting_main(request):

    """
    this is main & primary page
    """

    # load main.html for render
    main_template = loader.get_template('WareHouseApp/first_WeightLifting.html')

    context = {

        'request': request

    }

    return HttpResponse(main_template.render(context))


def user_url(request):

    """
    this is user page
    """

    # load main.html for render
    main_template = loader.get_template('WareHouseApp/user.html')

    context = {

        'user': request.user.username if request.user.is_authenticated else 'anonymouse',
        'request': request
    }

    return HttpResponse(main_template.render(context))


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
    print(error_text)
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
            'error_text': error_text,
            'request': requests

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

        if len(company_obj_list) > 0 and password == verify_pass:

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

                user_model = models.LiveWeighbridgeManager()

            elif user_type == 'precold_manager':

                user_model = models.PreColdManager()

            elif user_type == 'task_manager':

                user_model = dm_models.TaskUser()

            elif user_type == 'warehouse_manager':

                user_model = models.SlaughterEmployee()

            elif user_type == 'seg_manager':

                user_model = models.Segmentation()

            else:

                # raised error and redirect to error page
                return HttpResponseRedirect(reverse('Error', args=['incorrect information']))

            # set user model param

            user_model.username = username
            user_model.name = name
            user_model.lastname = lastname
            user_model.phone_number = phone_number
            user_model.user = user_obj
            user_model.company = company_obj_list[0]

            # save user model
            user_model.save()

            return HttpResponseRedirect(reverse('User_url'))

        else:

            # raised error and redirect to error page
            return HttpResponseRedirect(reverse('Error', args=['there is no company object']))

    else:

        # raised error and redirect to error page
        return HttpResponseRedirect(reverse('Error', args=['you don"t have access to this page']))


def sign_in_form(request, error_text="لطفا ابتدا مشخصات خود را وارد نماييد"):

    """
    login form
    """

    if request.user.is_authenticated:

        return HttpResponseRedirect(reverse('Main'))

    else:

        sign_in_form_page = loader.get_template('WareHouseApp/sign_in_form.html')

        context = {
            "error": error_text
        }

        return HttpResponse(sign_in_form_page.render(context))


@csrf_exempt
def sign_in(request):

    """
    this is entry page
    """

    if not request.user.is_authenticated:

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
            return HttpResponseRedirect(reverse('Error', args=["password is incorect"]))

    else:

        # user login previously and just redirect to main page
        return HttpResponseRedirect(reverse('Main'))


def log_out(request):

    """
    exit
    """

    logout(request)


def user_profile(request, username='admin'):

    user_profile_page = loader.get_template('WareHouseApp/user_profile.html')

    context = {
        "user": request.user
    }

    if request.user.is_authenticated:

        return HttpResponse(user_profile_page.render(context))

    else:

        return HttpResponseRedirect(reverse('SignIn_Form'))


def change_password_form(request, error_text='fill blank'):

    """
    change password form
    """

    if request.user.is_superuser:

        # load change password template
        change_password_form_page = loader.get_template('WareHouseApp/change_password_form.html')

        context = {

            'error_text': error_text,
            'request': request,
        }

        return HttpResponse(change_password_form_page.render(context))

    else:
        # redirect to error page
        return HttpResponseRedirect(reverse('Error', args=["you don't have permission"]))


@csrf_exempt
def change_password(request):

    """
    get data from change_password_form and change user's password
    """

    if request.user.is_superuser:

        # get form param (POST)
        username = request.POST['username']
        password = request.POST['password']
        verify_pass = request.POST['verify_pass']

        if password != verify_pass:

            # raised error
            return HttpResponseRedirect(reverse('Change_Password_From', args=['pass and verify is incorrect']))

        # get user
        user_obj = User.objects.get(username=username)

        if user_obj:

            # change password
            user_obj.set_password(password)
            user_obj.save()

            return HttpResponseRedirect(reverse('User_url'))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Change_Password_From', args=['username incorrect']))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))


###############################
###############################
"""   Live WeightBridge     """
###############################
###############################


def lwb_order_form(requests):

    """
    user create live weighbridge ordering
    """

    if requests.user.is_authenticated:

        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            driver_temp = loader.get_template('WareHouseApp/lwb_order_form.html')

            context = {

                'request': requests,
                'driver_list': models.Driver.objects.all().filter(driver_type=True),
                'car_list': models.Car.objects.all().filter(live_product=True),
                'po_list': models.ProductOwner.objects.all(),
                'avc_list': models.Aviculture.objects.all(),
                'code': random.randint(10,1000),

            }

            return HttpResponse(driver_temp.render(context))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you can't access this page <br> you should login"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access this page <br> you should login"]))


@csrf_exempt
def lwb_order(requests):

    """
    create driver object
    """

    if requests.user.is_authenticated:

        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            # get form data (POST)
            driver_id = requests.POST['driver_id']
            car_id = requests.POST['car_id']
            product_owner_id = requests.POST['po_id']
            buy_price = requests.POST['buy_price']
            product_weight = requests.POST['product_weight']
            product_category = requests.POST['product_category']
            aviculture_id = requests.POST['avc_id']
            product_avg_weight = float(requests.POST['product_avg_weight'])
            account_side = requests.POST['Account_side']

            # create product owner
            pro_obj_list = models.ProductOwner.objects.all().filter(product_owner_id=product_owner_id)

            # check Create product owner object or select it
            po_obj = pro_obj_list[0]

            # get car object list
            car_obj = models.Car.objects.get(car_id=car_id)

            # get driver object list
            driver_obj_lis = models.Driver.objects.all().filter(driver_id=driver_id)
            driver_obj = driver_obj_lis[0]

            # get avliculture object
            avc_obj = models.Aviculture.objects.get(aviculture_id=aviculture_id)

            # create Live weighbridge object
            lwb_obj = models.LiveWeighbridge()

            # set param
            lwb_obj.buy_price = buy_price
            lwb_obj.live_weighbridge_id = str(uuid1().int)
            lwb_obj.product_category = product_category
            lwb_obj.order_weight = product_weight
            lwb_obj.driver = driver_obj
            lwb_obj.car = car_obj
            lwb_obj.product_owner = po_obj
            lwb_obj.avicultureـcity = avc_obj.source
            lwb_obj.avicultureـname = avc_obj.name
            lwb_obj.account_side = account_side
            lwb_obj.aviculture_avg_weight = product_avg_weight
            lwb_obj.order_Manager = requests.user.username

            # save live weighbridge
            lwb_obj.save()

            return HttpResponseRedirect(reverse('live_WeighBridge'))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))


@csrf_exempt
def lwb_driver(requests):

    """
    create driver object
    """

    if requests.user.is_authenticated:

        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            driver_name = requests.POST['driver_name']
            driver_lastname = requests.POST['driver_last_name']
            driver_phone_number = requests.POST['driver_phone_number']

            # create model
            driver_obj = models.Driver()

            # set param
            driver_obj.name = driver_name
            driver_obj.last_name = driver_lastname
            driver_obj.phone_number = driver_phone_number
            driver_obj.driver_type = True
            driver_obj.driver_id = str(uuid1().int)

            # save
            driver_obj.save()

            return HttpResponseRedirect(reverse('Live_WeighBridge_Order_Form'))

    return HttpResponseRedirect(reverse('Error', args=['شما اجازه ی دسترسی به این صفحه را ندارید']))


@csrf_exempt
def lwb_car(requests):
    """
    create car object
    """
    if requests.user.is_authenticated:

        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            car_number1 = requests.POST['car_number1']
            car_number2 = requests.POST['car_number2']
            car_number3 = requests.POST['car_number3']
            car_number4 = requests.POST['car_number4']
            car_type = requests.POST['car_type']

            # create model
            car_obj = models.Car()

            # set param
            car_obj.car_number1 = car_number1
            car_obj.car_number2 = car_number2
            car_obj.car_number3 = car_number3
            car_obj.car_number4 = car_number4
            car_obj.car_number = str(car_number1) + str(car_number2) + str(car_number3) + str(car_number4)
            car_obj.car_id = str(uuid1().int)
            car_obj.car_type = car_type

            # save
            car_obj.save()

            return HttpResponseRedirect(reverse('Live_WeighBridge_Order_Form'))

    return HttpResponseRedirect(reverse('Error', args=['شما اجازه ی دسترسی به این صفحه را ندارید']))


@csrf_exempt
def lwb_product_owner(requests):

    """
    create car object
    """
    if requests.user.is_authenticated:

        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            po_name = requests.POST['product_owner_name']
            po_lastname = requests.POST['product_owner_lastname']

            # create model
            po_obj = models.ProductOwner()

            # set param
            po_obj.name = po_name
            po_obj.last_name = po_lastname
            po_obj.product_owner_id = str(uuid1().int)

            # save
            po_obj.save()

            return HttpResponseRedirect(reverse('first_WeightLifting'))

    return HttpResponseRedirect(reverse('Error', args=['شما اجازه ی دسترسی به این صفحه را ندارید']))


@csrf_exempt
def lwb_aviculture(requests):

    """
    create car object
    """
    if requests.user.is_authenticated:

        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            avc_name = requests.POST['Avicultureـname']
            avc_city = requests.POST['Avicultureـcity']

            # create model
            avc_obj = models.Aviculture()

            # set param
            avc_obj.name = avc_name
            avc_obj.source = avc_city
            avc_obj.aviculture_id = str(uuid1().int)

            # save
            avc_obj.save()

            return HttpResponseRedirect(reverse('Live_WeighBridge_Order_Form'))

    return HttpResponseRedirect(reverse('Error', args=['شما اجازه ی دسترسی به این صفحه را ندارید']))


def lwb_create_form(requests):

    """
    user can create driver object or select one of them
    """

    if requests.user.is_authenticated:

        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            driver_temp = loader.get_template('WareHouseApp/lwb_create_form.html')

            context = {

                'request': requests,
                'lwb_list': models.LiveWeighbridge.objects.all().filter(lwb_category='O')

            }

            return HttpResponse(driver_temp.render(context))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you can't access this page <br> you should login"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access this page <br> you should login"]))


@csrf_exempt
def lwb_create(requests):

    """
    create driver object
    """

    if requests.user.is_authenticated:

        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            # get form data (POST)
            car_weight = requests.POST['car_weight']
            cage_num = requests.POST['cage_num']
            product_num_in_cage = requests.POST['product_num_in_cage']
            lwb_id = requests.POST['lwb_id']
            source_weight = float(requests.POST['source_weight'])

            # get data
            lwb_obj = models.LiveWeighbridge.objects.get(live_weighbridge_id=lwb_id)

            # set param
            lwb_obj.cage_num = cage_num
            lwb_obj.product_num_in_cage = product_num_in_cage
            lwb_obj.final_weight = car_weight
            lwb_obj.weighting_date = time.time() + information.time_dif
            t = time.ctime(time.time() + information.time_dif).split()
            year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
            t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))
            lwb_obj.weighting_date_format = t
            lwb_obj.lwb_category = 'W'
            lwb_obj.Live_Weighbridge_Manager = requests.user.username
            lwb_obj.source_weight = source_weight

            # save live weighbridge
            lwb_obj.save()

            return HttpResponseRedirect(reverse('live_WeighBridge'))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))


@csrf_exempt
def lwb_reject(requests):

    """
    create driver object
    """

    if requests.user.is_authenticated:

        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            # get form data (POST)
            lwb_id = requests.POST['lwb_id']

            # get data
            lwb_obj = models.LiveWeighbridge.objects.get(live_weighbridge_id=lwb_id)

            lwb_obj.lwb_category = 'R'

            # save live weighbridge
            lwb_obj.save()

            return HttpResponseRedirect(reverse('live_WeighBridge'))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))


def lwb_start_slaughter_form(requests):

    """
    show all of lwb object and user must choose from one of them
    """

    if requests.user.is_authenticated:

        # get user and check user's permission
        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            # load template
            slaughter_temp = loader.get_template('WareHouseApp/slaughter_starting.html')

            context = {

                'slaughter_list': models.LiveWeighbridge.objects.all().filter(slaughter_status=False).filter(
                    finish=False
                ).filter(
                    weighting_date__gte=time.time()-(60*60*12)

                ),

                'request': requests,

            }

            return HttpResponse(slaughter_temp.render(context))

        else:

            return HttpResponseRedirect(reverse('Error', args=["you can't access this page"]))

    else:
        return HttpResponseRedirect(reverse('Error', args=["you can't access this page"]))


@csrf_exempt
def lwb_start_slaughter(requests):

    """
    get data from form data change status to True and save start time
    """

    if requests.user.is_authenticated:

        # get user and check user's permission
        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            # get information
            slaughter_id = requests.POST['slaughter_id']

            # get liveWeighBridge list
            lwb_obj_list = models.LiveWeighbridge.objects.all().filter(live_weighbridge_id= slaughter_id)

            if len(lwb_obj_list) > 0:

                # change object status to True and save current time
                lwb_obj = lwb_obj_list[0]

                # change information
                lwb_obj.slaughter_status = True
                lwb_obj.slaughter_start_date = time.time() + information.time_dif
                t = time.ctime(time.time() + information.time_dif).split()
                year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
                t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))
                lwb_obj.slaughter_start_date_format = t

                # save changes
                lwb_obj.save()

                return HttpResponseRedirect(reverse('live_WeighBridge'))

            else:

                return HttpResponseRedirect(reverse('Error', args=['enter information is incorrect']))

        else:

            return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))

    else:

        return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))


def lwb_finish_slaughter_form(requests):
    """
    show all of lwb object and user must choose from one of them
    """

    if requests.user.is_authenticated:

        # get user and check user's permission
        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            # load template
            slaughter_temp = loader.get_template('WareHouseApp/slaughter_finishing.html')

            context = {

                'slaughter_list': models.LiveWeighbridge.objects.all().filter(slaughter_status=True).filter(
                    weighting_date__gte=time.time() - (60 * 60 * 6)
                ).filter(finish=False),

                'request': requests

            }

            return HttpResponse(slaughter_temp.render(context))

        else:

            return HttpResponseRedirect(reverse('Error', args=["you can't access this page"]))

    else:
        return HttpResponseRedirect(reverse('Error', args=["you can't access this page"]))


@csrf_exempt
def lwb_finish_slaughter(requests):
    """
    get data from form data change status to True and save start time
    """

    if requests.user.is_authenticated:

        # get user and check user's permission
        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            # get information
            slaughter_id = requests.POST['slaughter_id']

            # get liveWeighBridge list
            lwb_obj_list = models.LiveWeighbridge.objects.all().filter(live_weighbridge_id=slaughter_id)

            if len(lwb_obj_list) > 0:

                # change object status to True and save current time
                lwb_obj = lwb_obj_list[0]

                # change information
                lwb_obj.slaughter_status = False
                lwb_obj.finish = True
                lwb_obj.slaughter_finish_date = time.time() + information.time_dif
                t = time.ctime(time.time() + information.time_dif).split()
                year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
                t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

                lwb_obj.slaughter_finish_date_format = t

                # save changes
                lwb_obj.save()

                return HttpResponseRedirect(reverse('live_WeighBridge'))

            else:

                return HttpResponseRedirect(reverse('Error', args=['enter information is incorrect']))

        else:

            return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))

    else:

        return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))


def lwb_capability_form(requests):

    """
    show all of lwb object and user must choose from one of them
    """

    if requests.user.is_authenticated:

        # get user and check user's permission
        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            # load template
            slaughter_temp = loader.get_template('WareHouseApp/LiveWeighBridge_capability.html')

            context = {

                'lwb_list': models.LiveWeighbridge.objects.all().filter(car_empty=False).filter(
                    final_weight__gte=0.0
                ),
                'request': requests

            }

            return HttpResponse(slaughter_temp.render(context))

        else:

            return HttpResponseRedirect(reverse('Error', args=["you can't access this page"]))

    else:
        return HttpResponseRedirect(reverse('Error', args=["you can't access this page"]))


@csrf_exempt
def lwb_capability(requests):
    """
    get data from form data change status to True and save start time
    """

    if requests.user.is_authenticated:

        # get user and check user's permission
        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            # get information
            lwb_id = requests.POST['lwb_id']
            car_weight = requests.POST['car_weight']
            losses_num = requests.POST['losses_num']
            victim_num = requests.POST['victim_num']
            fuel = float(requests.POST['fuel'])

            # get liveWeighBridge list
            lwb_obj_list = models.LiveWeighbridge.objects.all().filter(live_weighbridge_id=lwb_id)

            if len(lwb_obj_list) > 0:

                # change object status to True and save current time
                lwb_obj = lwb_obj_list[0]

                weight = (lwb_obj.final_weight - float(car_weight)) / (lwb_obj.cage_num * lwb_obj.product_num_in_cage)

                # change information
                lwb_obj.car_empty = True
                lwb_obj.car_weight = float(car_weight)
                lwb_obj.losses_num = int(losses_num)
                lwb_obj.losses_weight = int(losses_num) * weight
                lwb_obj.victim_num = int(victim_num)
                lwb_obj.victim_weight = int(victim_num) * weight
                lwb_obj.fuel = fuel

                # save changes
                lwb_obj.save()

                # load template
                temp = loader.get_template('WareHouseApp/lwb_driver_report.html')

                t = time.ctime(time.time() + information.time_dif).split()
                year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
                t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

                context = {

                    'source_weight': lwb_obj.source_weight,
                    'weight': lwb_obj.final_weight - lwb_obj.car_weight,
                    'full_weight': lwb_obj.final_weight,
                    'empty_weight': lwb_obj.car_weight,
                    'driver': lwb_obj.driver.name + ' ' + lwb_obj.driver.last_name,
                    'car': str(lwb_obj.car.car_number1) + ' '+ str(lwb_obj.car.car_number2) +' '+ str(lwb_obj.car.car_number3) + ' '+str(lwb_obj.car.car_number4)  ,
                    'drop_down': lwb_obj.source_weight - (lwb_obj.final_weight - lwb_obj.car_weight) if lwb_obj.source_weight > 0.0 else 0.0,
                    'avic_city': lwb_obj.avicultureـcity,
                    'avic_name': lwb_obj.avicultureـname,
                    'prod_num': lwb_obj.cage_num * lwb_obj.product_num_in_cage,
                    'prod_type': lwb_obj.product_category,
                    'cage_num': lwb_obj.cage_num,
                    'prod_num_in_cage': lwb_obj.product_num_in_cage,
                    'losses_num': lwb_obj.losses_num,
                    'losses_weight': round(lwb_obj.losses_weight, 2),
                    'victim_num': lwb_obj.victim_num,
                    'victim_weight': round(lwb_obj.victim_weight, 2),
                    'request': requests,
                    'date': t,
                    'type': 'حواله باسکول زنده',

                }

                return HttpResponse(temp.render(context))

            else:

                return HttpResponseRedirect(reverse('Error', args=['enter information is incorrect']))

        else:

            return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))

    else:

        return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))


def lwb_driver_report(requests, lwb_id='0'):

    """
    report driver live weighbridge
    """
    if requests.user.is_authenticated:

        # get user and check user's permission
        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            # get liveWeighBridge list
            lwb_obj_list = models.LiveWeighbridge.objects.all().filter(live_weighbridge_id=lwb_id)

            if len(lwb_obj_list) > 0:

                # change object status to True and save current time
                lwb_obj = lwb_obj_list[0]

                # load template
                temp = loader.get_template('WareHouseApp/lwb_driver_report.html')

                t = time.ctime(time.time() + information.time_dif).split()
                year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
                t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

                context = {

                    'weight_time': lwb_obj.weighting_date_format,
                    'source_weight': lwb_obj.source_weight,
                    'weight': lwb_obj.final_weight - lwb_obj.car_weight,
                    'full_weight': lwb_obj.final_weight,
                    'empty_weight': lwb_obj.car_weight,
                    'driver': lwb_obj.driver.name + ' ' + lwb_obj.driver.last_name,
                    'car': str(lwb_obj.car.car_number1) + ' '+ str(lwb_obj.car.car_number2) +' '+ str(lwb_obj.car.car_number3) + ' '+str(lwb_obj.car.car_number4)  ,
                    'drop_down': lwb_obj.source_weight - (lwb_obj.final_weight - lwb_obj.car_weight) if lwb_obj.source_weight > 0.0 else 0.0,
                    'avic_city': lwb_obj.avicultureـcity,
                    'avic_name': lwb_obj.avicultureـname,
                    'prod_num': lwb_obj.cage_num * lwb_obj.product_num_in_cage,
                    'prod_type': lwb_obj.product_category,
                    'cage_num': lwb_obj.cage_num,
                    'prod_num_in_cage': lwb_obj.product_num_in_cage,
                    'losses_num': lwb_obj.losses_num,
                    'losses_weight': round(lwb_obj.losses_weight, 2),
                    'victim_num': lwb_obj.victim_num,
                    'victim_weight': round(lwb_obj.victim_weight, 2),
                    'request': requests,
                    'date': t,
                    'type': 'حواله باسکول زنده',

                }

                return HttpResponse(temp.render(context))

            else:

                return HttpResponseRedirect(reverse('Error', args=['enter information is incorrect']))

        else:

            return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))

    else:

        return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))


def lwb_final_form(requests):
    """
    return last 24 hours live weighbridge
    """

    if requests.user.is_authenticated:

        # get user and check user's permission
        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            # load template
            slaughter_temp = loader.get_template('WareHouseApp/lwb_final.html')

            context = {

                'lwb_list': models.LiveWeighbridge.objects.all().filter(
                    weighting_date__gte=time.time() - (60 * 60 * 24)

                ),

                'request': requests,

            }

            return HttpResponse(slaughter_temp.render(context))

        else:

            return HttpResponseRedirect(reverse('Error', args=["you can't access this page"]))

    else:
        return HttpResponseRedirect(reverse('Error', args=["you can't access this page"]))


@csrf_exempt
def lwb_final(requests):
    """
    get data from form data change status to True and save start time
    """

    if requests.user.is_authenticated:

        # get user and check user's permission
        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            # get information
            lwb_id = requests.POST['lwb_id']
            per_purchase = float(requests.POST['per_purchase'])
            per_sale = float(requests.POST['per_sale'])
            buy_price = float(requests.POST['buy_price'])
            sale_weight = float(requests.POST['sale_weight'])
            driver_rent = float(requests.POST['driver_rent'])

            # get liveWeighBridge list
            lwb_obj_list = models.LiveWeighbridge.objects.all().filter(live_weighbridge_id=lwb_id)

            if len(lwb_obj_list) > 0:

                # change object status to True and save current time
                lwb_obj = lwb_obj_list[0]

                # change information
                lwb_obj.per_purchase = per_purchase
                lwb_obj.per_sale = per_sale
                lwb_obj.sale_weight = sale_weight
                lwb_obj.driver_rent = driver_rent
                if buy_price > 0.0:
                    lwb_obj.buy_price = buy_price

                # save changes
                lwb_obj.save()

                return HttpResponseRedirect(reverse('live_WeighBridge'))

            else:

                return HttpResponseRedirect(reverse('Error', args=['enter information is incorrect']))

        else:

            return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))

    else:

        return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))


def lwb_count_form(requests):

    """
    import product count
    """

    if requests.user.is_authenticated:

        # get user and check user's permission
        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            # load template
            slaughter_temp = loader.get_template('WareHouseApp/LiveWeighBridge_count.html')

            context = {

                'lwb_list': models.LiveWeighbridge.objects.all().filter(
                    car_weight__gte=0.0
                ).filter(weighting_date__gte=(time.time() + information.time_dif) - (60 * 60 *12)).filter(
                    salughter_count=0.0),
                'request': requests

            }

            return HttpResponse(slaughter_temp.render(context))

        else:

            return HttpResponseRedirect(reverse('Error', args=["you can't access this page"]))

    else:
        return HttpResponseRedirect(reverse('Error', args=["you can't access this page"]))


@csrf_exempt
def lwb_count(requests):

    """
    get data from form data change status to True and save start time
    """

    if requests.user.is_authenticated:

        # get user and check user's permission
        # get user list
        lwb_user_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(lwb_user_list) > 0 or len(ceo_user_list) or requests.user.is_superuser:

            # get information
            lwb_id = requests.POST['lwb_id']
            count = requests.POST['count']

            # get liveWeighBridge list
            lwb_obj_list = models.LiveWeighbridge.objects.all().filter(live_weighbridge_id=lwb_id)

            if len(lwb_obj_list) > 0:

                # change object status to True and save current time
                lwb_obj = lwb_obj_list[0]

                # change information
                lwb_obj.salughter_count = count

                # save changes
                lwb_obj.save()

                return HttpResponseRedirect(reverse('live_WeighBridge'))

            else:

                return HttpResponseRedirect(reverse('Error', args=['enter information is incorrect']))

        else:

            return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))

    else:

        return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))


def first_weightlifting_form(requests):

    """
    render create first weighting form
    this process is after the live_weighBridge
    """

    if requests.user.is_authenticated:

        # get user's list
        first_weightlifting_user_list = models.WeightLiftingManager.objects.all().filter(username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_user_list) > 0 or len(first_weightlifting_user_list) > 0 or requests.user.is_superuser:

            # user can access this page
            # load template
            first_weight_temp = loader.get_template('WareHouseApp/first_weightlifting_form.html')

            context = {

                'po_list': models.ProductOwner.objects.all(),
                'request': requests,
                'code': random.randint(1000, 9999)

            }

            return HttpResponse(first_weight_temp.render(context))

        else:

            # raised Error
            return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))

    else:

        # raised Error
        return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))


@csrf_exempt
def first_weightlifting(requests):

    """
    get data from first_weightlifting_form and create first_weightlifting object
    """

    if requests.user.is_authenticated:

        # get user's list
        first_weightlifting_user_list = models.WeightLiftingManager.objects.all().filter(
            username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_user_list) > 0 or len(first_weightlifting_user_list) > 0 or requests.user.is_superuser:

            # get data
            po_id = requests.POST['po_id']
            weight = float(requests.POST['weight'])
            sales_category = requests.POST['sales_category']
            bike_weight = float(requests.POST['bike_weight'])
            box_num = float(requests.POST['box_num'])
            code = str(requests.POST['code'])
            prod_category = requests.POST['prod_category']

            try:
                product_class = requests.POST['product_class']
                product_class = False

            except:
                product_class = True

            try:
                box_type = requests.POST['box_type']
                box_weight = information.big_box

            except:
                box_weight = information.small_box

            # create first_weightlifting objects
            fwl = models.FirstWeightLifting()

            # calculate box
            box_weight = box_weight * box_num

            weight = weight - (bike_weight + box_weight)

            fwl.weight = str(weight)
            fwl.sales_category = sales_category
            fwl.weight_lifting_id = str(uuid1().int)
            fwl.weighting_time = time.time() + information.time_dif

            t = time.ctime(time.time() + information.time_dif).split()
            year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
            t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))
            fwl.weighting_time_format = t

            fwl.code = str(code)
            fwl.class_product = product_class
            fwl.Weight_Lifting_Manager = requests.user.username
            fwl.product_category = prod_category
            fwl.product_owner = models.ProductOwner.objects.get(product_owner_id=po_id)

            # save objects
            fwl.save()

            return HttpResponseRedirect(reverse('first_WeightLifting'))

        else:

            # raised Error
            return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

    else:

        # raised Error
        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def pre_cold_enter_form(requests):

    """
    render pre_cold enter form to add new
    """

    if requests.user.is_authenticated:

        # get user's list
        first_pre_cold_user_list = models.PreColdManager.objects.all().filter(
            username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_user_list) > 0 or len(first_pre_cold_user_list) > 0 or requests.user.is_superuser:

            # render form
            pre_cold_temp = loader.get_template('WareHouseApp/pre_cold_enter_form.html')

            context = {

                "fwl_list": models.FirstWeightLifting.objects.all().filter(sales_category='P').filter(
                    weighting_time__gte=time.time() - (60*60*10)
                ).filter(choice_status=False),
                'request': requests

            }

            return HttpResponse(pre_cold_temp.render(context))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def pre_cold_enter(requests):

    """
    create pre cold object
    """

    if requests.user.is_authenticated:

        # get user's list
        first_pre_cold_user_list = models.PreColdManager.objects.all().filter(
            username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_user_list) > 0 or len(first_pre_cold_user_list) > 0 or requests.user.is_superuser:

            # get data
            fwl_id = requests.POST['fwl_id']
            pc_id = requests.POST['pc_id']
            box_num = int(requests.POST['box_num'])

            # create pre-cold object
            pc = models.PreCold()

            # set param
            pc.box_num = int(box_num)
            pc.pre_cold_id = pc_id
            pc.pc_id = str(uuid1().int)
            pc.entry_time = time.time() + information.time_dif
            t = time.ctime(time.time() + information.time_dif).split()
            year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
            t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

            pc.entry_time_format = t

            # relation
            fwl_list = models.FirstWeightLifting.objects.all().filter(weight_lifting_id=fwl_id)
            pc.First_Weight_Lifting = fwl_list[0]
            fwl_obj = fwl_list[0]
            fwl_obj.choice_status = True
            fwl_obj.save()

            if len(first_pre_cold_user_list) > 0:
                pc.PreCold_Manager = first_pre_cold_user_list[0]

            # save
            pc.save()

            return HttpResponseRedirect(reverse('first_WeightLifting'))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you can't access this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access this page"]))


def pre_cold_exit_form(requests):

    """
    render pre cold exit form
    """

    if requests.user.is_authenticated:

        # get user's list
        first_pre_cold_user_list = models.PreColdManager.objects.all().filter(
            username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_user_list) > 0 or len(first_pre_cold_user_list) > 0 or requests.user.is_superuser:

            # load template
            exit_temp = loader.get_template('WareHouseApp/pre_cold_exit_form.html')

            context = {

                'pc_list': models.PreCold.objects.all().filter(product_pre_cold_status=True),
                'request': requests

            }

            return HttpResponse(exit_temp.render(context))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you can't access this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access this page"]))


@csrf_exempt
def pre_cold_exit(requests):

    """
    change pre cold object to exit status
    """

    if requests.user.is_authenticated:

        # get user's list
        first_pre_cold_user_list = models.PreColdManager.objects.all().filter(
            username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_user_list) > 0 or len(first_pre_cold_user_list) > 0 or requests.user.is_superuser:

            # get request data
            pc_id = requests.POST['pc_id']
            exit_category = requests.POST['exit_category']

            # get object list
            pc_list = models.PreCold.objects.all().filter(pc_id=pc_id)

            if len(pc_list) > 0:

                # get object
                pc_obj = pc_list[0]

                # set param
                pc_obj.product_pre_cold_status = False
                pc_obj.exit_time = time.time() + information.time_dif
                t = time.ctime(time.time() + information.time_dif).split()
                year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
                t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

                pc_obj.exit_time_format = t
                pc_obj.out_category = exit_category
                pc_obj.First_Weight_Lifting.sales_category = exit_category
                pc_obj.First_Weight_Lifting.choice_status = False

                if exit_category == 'G':
                    pc_obj.out_status = True

                # save param
                pc_obj.save()
                pc_obj.First_Weight_Lifting.save()

                return HttpResponseRedirect(reverse('first_WeightLifting'))

            else:

                # raised error
                return HttpResponseRedirect(reverse('Error', args=['you entry pre-cold id is incorrect']))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you cant access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you cant access to this page"]))


def distribute_form(requests):

    """
    render distribute form for create distribute object
    """

    if requests.user.is_authenticated:

        # create object list
        dist_manager_list = models.SalesManager.objects.all().filter(username=requests.user.username)
        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(dist_manager_list) > 0 or len(ceo_list) > 0 or requests.user.is_superuser:

            # user can access to this page
            # load template
            dist_temp = loader.get_template('WareHouseApp/distribute_form.html')

            context = {

                "dist_root_list": models.DistributedRoot.objects.all().filter(finish_loading=False),


                "fwl_list": models.FirstWeightLifting.objects.all().filter(sales_category='D').filter(
                    weighting_time__gte=time.time() - (60*60*12)
                ).filter(choice_status=False),

                'ft_list': models.FreezingTunnel.objects.all().filter(output_category='D').filter(choice_status=False),
                'ch_list': models.ColdHouse.objects.all().filter(output_category='D').filter(choice_status=False),
                'seg_list': models.Segmentation.objects.all().filter(choice_status=False).filter(output_category="D"),

                'driver_list': models.Driver.objects.all(),
                'car_list': models.Car.objects.all().filter(live_product=False),

                'request': requests,

            }

            return HttpResponse(dist_temp.render(context))

        else:

            return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

    else:

        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def distribute(requests):

    """
    create distribute object
    """

    if requests.user.is_authenticated:

        # create object list
        dist_manager_list = models.SalesManager.objects.all().filter(username=requests.user.username)
        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(dist_manager_list) > 0 or len(ceo_list) > 0 or requests.user.is_superuser:

            # get data
            dist_id = requests.POST['dist_id']
            fwl_id = requests.POST['fwl_id']
            weight = float(requests.POST['weight'])
            sale_price = requests.POST['sale_price']
            box_weight = float(requests.POST['box_weight'])
            number_of_box = requests.POST['number_of_box']

            # create distribute object
            dist_obj = models.Distributed()

            # set param
            dist_obj.date = time.time() + information.time_dif
            t = time.ctime(time.time() + information.time_dif).split()
            year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
            t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

            dist_obj.date_format = t
            dist_obj.weight = weight - box_weight - (int(number_of_box) * information.box_weight)
            dist_obj.sale_price = sale_price
            dist_obj.bill_of_lading = str(uuid1().int)
            dist_obj.number_of_box = number_of_box
            dist_obj.sales_input_category = fwl_id[0]
            dist_obj.sales_input_id = fwl_id[1:]

            if fwl_id[0] == 'F':

                x = models.FirstWeightLifting.objects.get(weight_lifting_id=fwl_id[1:])
                x.choice_status = True
                x.save()

            elif fwl_id[0] == 'T':

                x = models.FreezingTunnel.objects.get(freeze_tunnel_id=fwl_id[1:])
                x.choice_status = True
                x.save()

            elif fwl_id[0] == 'C':

                x = models.ColdHouse.objects.get(cold_house_primary_key=fwl_id[1:])
                x.choice_status = True
                x.save()

            elif fwl_id[0] == 'G':

                x = models.Segmentation.objects.get(segment_id=fwl_id[1:])
                x.choice_status = True
                x.save()

            if len(dist_manager_list) > 0:
                dist_obj.sales_manager = dist_manager_list[0]

            dist_object_list = models.DistributedRoot.objects.get(dist_id=dist_id)
            dist_obj.distribute_root = dist_object_list

            # save model
            dist_obj.save()

            return HttpResponseRedirect(reverse('first_WeightLifting'))

        else:

            # raised Error
            return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

    else:

        # raised Error
        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def distribute_driver_create(requests):

    """
    create driver for distribute
    """
    if requests.user.is_authenticated:

        # create object list
        dist_manager_list = models.SalesManager.objects.all().filter(username=requests.user.username)
        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(dist_manager_list) > 0 or len(ceo_list) > 0 or requests.user.is_superuser:

            # get car object list with filter
            car_list_obj = models.Car.objects.all().filter(car_number1=requests.POST['car_number1']).filter(
                car_number2=requests.POST['car_number2']
            ).filter(car_number3=requests.POST['car_number3']).filter(car_number4=requests.POST['car_number4'])

            car_number1 = requests.POST['car_number1']
            car_number2 = requests.POST['car_number2']
            car_number3 = requests.POST['car_number3']
            car_number4 = requests.POST['car_number4']

            if len(car_list_obj) == 0 and str(car_number4) != '0' and str(car_number3) != '0' and str(car_number2) != '0' \
                    and str(car_number1) != '0':

                # create object
                car_obj = models.Car()

                # set param
                car_obj.car_id = str(uuid1().int)

                car_obj.car_number4 = int(car_number4)
                car_obj.car_number3 = int(car_number3)
                car_obj.car_number2 = str(car_number2)
                car_obj.car_number1 = int(car_number1)

                car_obj.car_type = requests.POST['car_type']

                car_obj.car_number = str(car_number4) + str(car_number3) + str(car_number2) + str(car_number1)
                car_obj.live_product = False

                # save model
                car_obj.save()

            # get driver list
            driver_obj_list = models.Driver.objects.all().filter(name=requests.POST['driver_name']).filter(
                last_name=requests.POST['driver_last_name']
            )

            if len(driver_obj_list) == 0 \
                    and str(requests.POST['driver_name']) != '0' \
                    and str(requests.POST['driver_last_name']) != '0' \
                    and str(requests.POST['driver_phone_number']) != '0':

                # create object
                driver_obj = models.Driver()

                # set param
                driver_obj.name = requests.POST['driver_name']
                driver_obj.last_name = requests.POST['driver_last_name']
                driver_obj.phone_number = requests.POST['driver_phone_number']
                driver_obj.driver_id = str(uuid1().int)

                # save
                driver_obj.save()

            return HttpResponseRedirect(reverse('Distribute_Form'))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def distribute_root_empty(requests):

    """
    create distribute root models object with empty weight
    """

    if requests.user.is_authenticated:

        # create object list
        dist_manager_list = models.SalesManager.objects.all().filter(username=requests.user.username)
        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(dist_manager_list) > 0 or len(ceo_list) > 0 or requests.user.is_superuser:

            # get request param
            driver_id = requests.POST['driver_id']
            car_id = requests.POST['car_id']
            empty_weight = requests.POST['empty_weight']

            # get driver object
            driver_obj = models.Driver.objects.get(driver_id=driver_id)

            # car object
            car_obj = models.Car.objects.get(car_id=car_id)

            # create distribute root models
            dist_root_obj = models.DistributedRoot()

            # set param
            dist_root_obj.dist_id = str(uuid1().int)
            dist_root_obj.car = car_obj
            dist_root_obj.driver = driver_obj
            dist_root_obj.empty_weight = float(empty_weight)
            dist_root_obj.finish_loading = False

            # save object
            dist_root_obj.save()

            return HttpResponseRedirect(reverse('Distribute_Form'))

    # raised error
    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def distribute_root_full(requests):

    """
    create distribute root models object with empty weight
    """

    if requests.user.is_authenticated:

        # create object list
        dist_manager_list = models.SalesManager.objects.all().filter(username=requests.user.username)
        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(dist_manager_list) > 0 or len(ceo_list) > 0 or requests.user.is_superuser:

            # get request param
            dist_id = requests.POST['dist_id']
            full_weight = requests.POST['full_weight']
            dest = requests.POST['dest']

            # car object
            dist_root_obj = models.DistributedRoot.objects.get(dist_id=dist_id)

            # set param
            dist_root_obj.full_weight = float(full_weight)
            dist_root_obj.dest = dest
            dist_root_obj.finish_loading = True

            # save object
            dist_root_obj.save()
            return HttpResponseRedirect(reverse('Distribute_Form'))

    # raised error
    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def freeze_tunnel_enter_form(requests,):

    """
    render create tunnel freeze object form
    """

    if requests.user.is_authenticated:

        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)
        freeze_tunnel_manager_list = models.FreezingTunnelManager.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or len(freeze_tunnel_manager_list) > 0 or requests.user.is_superuser:

            # user have access to this page
            # load template
            freeze_tunnel_enter_temp = loader.get_template('WareHouseApp/freeze_tunnel_enter_form.html')

            context = {

                'fwl_list': models.FirstWeightLifting.objects.all().filter(sales_category='F').filter(
                    weighting_time__gte=(time.time() + information.time_dif) - (60 * 60 * 5)
                ).filter(choice_status=False),
                'seg_list': models.Segmentation.objects.all().filter(choice_status=False).filter(output_category='F'),
                'request': requests

            }

            return HttpResponse(freeze_tunnel_enter_temp.render(context))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def freeze_tunnel_enter(requests):

    """
    get request's form param and create freeze_tunnel object
    """

    ceo_list = models.CEO.objects.all().filter(username=requests.user.username)
    freeze_tunnel_manager_list = models.FreezingTunnelManager.objects.all().filter(username=requests.user.username)

    if len(ceo_list) > 0 or len(freeze_tunnel_manager_list) > 0 or requests.user.is_superuser:

        # user have access to this page
        # get param
        tunnel_id = requests.POST['tunnel_id']
        box_num = requests.POST['box_num']
        fwl_id = requests.POST['fwl_id']

        # create object
        ft_obj = models.FreezingTunnel()

        # set param
        ft_obj.tunnel_id = tunnel_id
        ft_obj.box_num = int(box_num)
        ft_obj.freeze_tunnel_id = str(uuid1().int)
        ft_obj.entry_date = time.time() + information.time_dif
        t = time.ctime(time.time() + information.time_dif).split()
        year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
        t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

        ft_obj.entry_date_format = t

        if fwl_id[0] == 'F':

            fwl_obj = models.FirstWeightLifting.objects.all().filter(weight_lifting_id=fwl_id[1:])[0]
            fwl_obj.choice_status = True
            fwl_obj.save()

            ft_obj.product_category = fwl_obj.product_category
            ft_obj.sub_product_category = 'B'
            ft_obj.input_type = 'F'
            ft_obj.input_id = fwl_id[1:]
            ft_obj.weight = fwl_obj.weight

        elif fwl_id[0] == 'G':

            seg_obj = models.Segmentation.objects.get(segment_id=fwl_id[1:])
            seg_obj.choice_status = True
            seg_obj.save()

            ft_obj.product_category = seg_obj.product_category
            ft_obj.sub_product_category = seg_obj.sub_product_category
            ft_obj.input_type = 'G'
            ft_obj.input_id = fwl_id[1:]
            ft_obj.weight = seg_obj.weight

        # set object user
        if len(freeze_tunnel_manager_list) > 0:

            ft_obj.freezing_tunnel_manager = freeze_tunnel_manager_list[0]

        # save object
        ft_obj.save()

        return HttpResponseRedirect(reverse('first_WeightLifting'))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def freeze_tunnel_exit_form(requests):

    """
    show list of freeze tunnel objects and select
    """

    if requests.user.is_authenticated:

        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)
        freeze_tunnel_manager_list = models.FreezingTunnelManager.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or len(freeze_tunnel_manager_list) > 0 or requests.user.is_superuser:

            # user have access to this page
            # load template
            ft_temp = loader.get_template('WareHouseApp/freeze_tunnel_exit_form.html')

            context = {

                'ft_list': models.FreezingTunnel.objects.all().filter(status=True),
                'request': requests

            }

            return HttpResponse(ft_temp.render(context))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you don't have access to this page"]))


@csrf_exempt
def freeze_tunnel_exit(requests):

    """
    select freeze_tunnel object to exit
    """

    if requests.user.is_authenticated:

        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)
        freeze_tunnel_manager_list = models.FreezingTunnelManager.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or len(freeze_tunnel_manager_list) > 0 or requests.user.is_superuser:

            # user have access to this page
            ft_id = requests.POST['ft_id']
            out_type = requests.POST['exit_category']

            # get model
            ft_obj = models.FreezingTunnel.objects.all().filter(freeze_tunnel_id=ft_id)[0]

            # set param
            ft_obj.exit_date = time.time() + information.time_dif
            t = time.ctime(time.time() + information.time_dif).split()
            year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
            t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

            ft_obj.exit_date_format = t
            ft_obj.status = False
            ft_obj.output_category = out_type

            # save
            ft_obj.save()

            return HttpResponseRedirect(reverse('first_WeightLifting'))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def paper_box_create_form(requests):

    """
    create paper box object form
    """

    if requests.user.is_authenticated:

        coldHouse_manager = models.FreezingTunnelManager.objects.all().filter(username=requests.user.username)
        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(coldHouse_manager) > 0 or len(ceo_list) > 0 or requests.user.is_superuser:

            # user have access
            # render template
            paper_box_temp = loader.get_template('WareHouseApp/paper_box_create_form.html')

            context = {

                'cold_house_list': models.ColdHouse.objects.all().filter(pallet_status=True),
                'po_list': models.ProductOwner.objects.all(),
                'request': requests

            }

            return HttpResponse(paper_box_temp.render(context))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def paper_box_create(requests):

    """
    create paper box object
    """

    if requests.user.is_authenticated:

        coldHouse_manager = models.FreezingTunnelManager.objects.all().filter(username=requests.user.username)
        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(coldHouse_manager) > 0 or len(ceo_list) > 0 or requests.user.is_superuser:

            # user have access to this page
            # get param
            cold_house_id = requests.POST['cold_house_id']
            weight = float(requests.POST['weight'])
            po_id = requests.POST['po_id']

            # create model
            paper_box_obj = models.PaperBox()

            # set param
            paper_box_obj.paper_box_weight = weight
            paper_box_obj.box_id = str(uuid1().int)
            paper_box_obj.packing_time = time.time() + information.time_dif
            t = time.ctime(time.time() + information.time_dif).split()
            year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
            t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))
            paper_box_obj.packing_time_format = t
            paper_box_obj.box_cold_house_exp = True

            # get cold house object
            cold_house_obj = models.ColdHouse.objects.get(cold_house_primary_key=cold_house_id)
            paper_box_obj_exam = models.PaperBox.objects.all().filter(cold_house__cold_house_primary_key=cold_house_id)[0]

            paper_box_obj.product_category = paper_box_obj_exam.product_category
            paper_box_obj.sub_product_category = paper_box_obj_exam.sub_product_category
            paper_box_obj.expiration_time = paper_box_obj_exam.expiration_time
            paper_box_obj.product_owner = models.ProductOwner.objects.get(product_owner_id=po_id)

            cold_house_obj.weight += weight
            cold_house_obj.number_of_box += 1

            cold_house_obj.save()

            paper_box_obj.cold_house = cold_house_obj

            # save model
            paper_box_obj.save()

            # load template to show paper_box_id
            paper_box_temp = loader.get_template('WareHouseApp/paper_box.html')

            context = {

                'id': paper_box_obj.box_id,
                'request': requests

            }

            return HttpResponse(paper_box_temp.render(context))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def cold_house_enter_form(requests):

    """
    cold house enter form
    """

    if requests.user.is_authenticated:
        coldHouse_manager = models.FreezingTunnelManager.objects.all().filter(username=requests.user.username)
        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(coldHouse_manager) > 0 or len(ceo_list) > 0 or requests.user.is_superuser:

            # user have access to this page
            # load template
            cold_house_enter_temp = loader.get_template('WareHouseApp/cold_house_enter.html')

            context = {

                "ft_list": models.FreezingTunnel.objects.all(
                ).filter(status=False).filter(
                    choice_status=False).filter(output_category='C'),
                'po_list': models.ProductOwner.objects.all(),
                'request': requests

            }

            return HttpResponse(cold_house_enter_temp.render(context))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def cold_house_enter(requests):

    """
    create cold-house object
    """

    if requests.user.is_authenticated:

        coldHouse_manager = models.FreezingTunnelManager.objects.all().filter(username=requests.user.username)
        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(coldHouse_manager) > 0 or len(ceo_list) > 0 or requests.user.is_superuser:

            # user have access to this page
            # get param
            ft_id = requests.POST['ft_id']
            pallet_weight = float(requests.POST['pallet_weight_with_product'])
            pallet_weight_empty = float(requests.POST['pallet_weight_without_product'])
            number_of_box = int(requests.POST['number_of_box'])
            cold_house_id = requests.POST['cold_house_id']
            pallet_id = requests.POST['pallet_id']
            expiration_time = int(requests.POST['expiration_time'])
            po_id = requests.POST['po_id']

            # create cold_house obj
            cold_house_obj = models.ColdHouse()

            if len(coldHouse_manager) > 0:
                cold_house_obj.freezing_tunnel_manager = coldHouse_manager[0]

            # set param
            cold_house_obj.number_of_box = number_of_box
            cold_house_obj.weight = pallet_weight - pallet_weight_empty - (number_of_box * information.freeze_box_weight)
            cold_house_obj.cold_house_id = cold_house_id
            cold_house_obj.cold_house_primary_key = str(uuid1().int)
            cold_house_obj.entry_date = time.time() + information.time_dif
            t = time.ctime(time.time() + information.time_dif).split()
            year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
            t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

            cold_house_obj.entry_date_format = t
            cold_house_obj.pallet_id = pallet_id

            # get freeze tunnel object
            ft_obj = models.FreezingTunnel.objects.get(freeze_tunnel_id=ft_id)
            ft_obj.choice_status = True
            ft_obj.save()

            cold_house_obj.freeze_tunnel = ft_obj
            cold_house_obj.product_category = ft_obj.product_category
            cold_house_obj.sub_product_category = ft_obj.sub_product_category

            # save object
            cold_house_obj.save()

            for k in range(number_of_box):

                paper_box_obj = models.PaperBox()

                paper_box_obj.cold_house = cold_house_obj
                paper_box_obj.box_status = True
                paper_box_obj.box_cold_house_exp = True
                paper_box_obj.paper_box_weight = cold_house_obj.weight / number_of_box
                paper_box_obj.product_category = ft_obj.product_category
                paper_box_obj.sub_product_category = ft_obj.sub_product_category
                paper_box_obj.expiration_time = int(expiration_time)
                paper_box_obj.box_id = str(uuid1().int)
                paper_box_obj.packing_time = time.time() + information.time_dif
                t = time.ctime(time.time() + information.time_dif).split()
                year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
                t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

                paper_box_obj.packing_time_format = t
                paper_box_obj.product_owner = models.ProductOwner.objects.get(product_owner_id=po_id)

                paper_box_obj.save()

            return HttpResponseRedirect(reverse("first_WeightLifting"))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def cold_house_exit_form(requests):

    """
    select cold house for exit
    """

    if requests.user.is_authenticated:

        coldHouse_manager = models.FreezingTunnelManager.objects.all().filter(username=requests.user.username)
        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(coldHouse_manager) > 0 or len(ceo_list) > 0 or requests.user.is_superuser:

            # user have access to this page
            # load template
            cold_house_exit_temp = loader.get_template('WareHouseApp/cold_house_exit_form.html')


            context = {

                'cold_house_list': models.ColdHouse.objects.all().filter(pallet_status=True),
                'paper_list': models.PaperBox.objects.all().filter(box_status=True),
                'request': requests

            }

            return HttpResponse(cold_house_exit_temp.render(context))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def cold_house_exit(requests):

    """
    exit from cold house
    """

    if requests.user.is_authenticated:

        coldHouse_manager = models.FreezingTunnelManager.objects.all().filter(username=requests.user.username)
        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(coldHouse_manager) > 0 or len(ceo_list) > 0 or requests.user.is_superuser:

            # user have access to this page
            cold_house_primary_key = requests.POST['cold_house_primary_key']
            exit_category = requests.POST['exit_category']

            # get object
            cold_house_obj = models.ColdHouse.objects.all().filter(cold_house_primary_key=cold_house_primary_key)[0]

            # move paper box from current cold house object to selected cold-house object
            for paper_key in requests.POST.keys():

                if paper_key[0] == 'P':

                    # get paper box object
                    paper = models.PaperBox.objects.get(box_id=paper_key[1:])

                    # change previous cold house object
                    pre_cold_house = paper.cold_house

                    # set new param
                    pre_cold_house.number_of_box -= 1
                    pre_cold_house.weight -= paper.paper_box_weight

                    # save previous cold house object
                    pre_cold_house.save()

                    # change paper box cold house object
                    paper.cold_house = cold_house_obj

                    # save changes on paper box object
                    paper.save()

                    # set new cold house object param
                    cold_house_obj.number_of_box += 1
                    cold_house_obj.weight += paper.paper_box_weight

            # change param
            cold_house_obj.exit_time = time.time() + information.time_dif
            t = time.ctime(time.time() + information.time_dif).split()
            year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
            t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

            cold_house_obj.exit_time_format = t
            cold_house_obj.output_category = exit_category
            cold_house_obj.pallet_status = False

            for paper in models.PaperBox.objects.all().filter(cold_house__cold_house_primary_key=cold_house_primary_key):

                # change paper box param
                paper.box_status = False
                paper.box_cold_house_exp = True
                paper.exit_time = time.time() + information.time_dif
                t = time.ctime(time.time() + information.time_dif).split()
                year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
                t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

                paper.exit_time_format = t

                # save paper-box object
                paper.save()

            # save object
            cold_house_obj.save()

            return HttpResponseRedirect(reverse('first_WeightLifting'))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def segmentation_form(requests):

    """
    segmentation unit form
    """

    if requests.user.is_authenticated:

        # get user's list
        first_pre_cold_user_list = models.PreColdManager.objects.all().filter(
            username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_user_list) > 0 or len(first_pre_cold_user_list) > 0 or requests.user.is_superuser:

            segment_temp = loader.get_template('WareHouseApp/segmentation.html')

            context = {

                'request': requests,
                'fwl_list': models.FirstWeightLifting.objects.all().filter(choice_status=False).filter(
                    sales_category='G'
                ),
                'code': random.randint(1000, 9999),

            }

            return HttpResponse(segment_temp.render(context))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def segmentation(requests):

    """
    segmentation unit
    """

    if requests.user.is_authenticated:

        # get user's list
        first_pre_cold_user_list = models.PreColdManager.objects.all().filter(
            username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_user_list) > 0 or len(first_pre_cold_user_list) > 0 or requests.user.is_superuser:

            fwl_id = requests.POST['fwl_id']
            code = requests.POST['code']
            weight = float(requests.POST['weight'])
            bike_weight = float(requests.POST['bike_weight'])
            box_num = requests.POST['box_num']
            sub_prod = requests.POST['sub_prod']
            sales_category = requests.POST['sales_category']

            # get first weightlifting and update it
            fwl_obj = models.FirstWeightLifting.objects.get(weight_lifting_id=fwl_id)

            # create segmentation model
            segmentation_model = models.Segmentation()

            segmentation_model.code = str(code)
            segmentation_model.weight = weight - bike_weight
            segmentation_model.box_num = box_num
            segmentation_model.sub_product_category = sub_prod
            segmentation_model.product_category = fwl_obj.product_category
            segmentation_model.output_category = sales_category
            segmentation_model.first_weight_lifting = fwl_obj
            segmentation_model.segment_id = str(uuid1().int)
            segmentation_model.segment_time = time.time() + information.time_dif
            t = time.ctime(time.time() + information.time_dif).split()
            year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
            t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

            segmentation_model.segment_time_format = t

            if len(first_pre_cold_user_list) > 0:
                segmentation_model.pre_cold_manager = first_pre_cold_user_list[0]

            segmentation_model.save()

            return HttpResponseRedirect(reverse('Segmentation_Form'))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def fwl_finish(requests, fwl_id):

    """
    segmentation unit
    """

    if requests.user.is_authenticated:

        # get user's list
        first_pre_cold_user_list = models.PreColdManager.objects.all().filter(
            username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_user_list) > 0 or len(first_pre_cold_user_list) > 0 or requests.user.is_superuser:

            # get first weightlifting and update it
            fwl_obj = models.FirstWeightLifting.objects.get(weight_lifting_id=fwl_id)
            fwl_obj.choice_status = True
            fwl_obj.save()

            return HttpResponseRedirect(reverse('Segmentation_Form'))

        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def company_list(requests):

    """
    user can see company list
    """

    if requests.user.is_superuser:

        # load template
        company_list_temp = loader.get_template('WareHouseApp/company_list.html')

        context = {

            'company_list': models.Company.objects.all(),
            'request': requests

        }

        return HttpResponse(company_list_temp.render(context))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def company_user_list(requests):

    """
    show all of company user list
    """

    # get request param
    company_id = requests.POST['company_id']

    # load template
    user_list_temp = loader.get_template('WareHouseApp/company_user_list.html')

    context = {

        'ceo_list': models.CEO.objects.all().filter(company__company_id=company_id),
        'ft_list': models.FreezingTunnelManager.objects.all().filter(company__company_id=company_id),
        'lw_list': models.LiveWeighbridgeManager.objects.all().filter(company__company_id=company_id),
        'pc_list': models.PreColdManager.objects.all().filter(company__company_id=company_id),
        'sales_list': models.SalesManager.objects.all().filter(company__company_id=company_id),
        'request': requests

    }

    return HttpResponse(user_list_temp.render(context))


def company_live_weighbridge_list(requests, year='0', month='0', day='0', deadline_year='0', deadline_month='0', deadline_day='0', output_status='0', product_category='0',
                                  slaughter_status='0'):

    """
    show company live WeighBridge data with it filter
    """

    if requests.user.is_authenticated:

        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)
        lwb_manager_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or len(lwb_manager_list) > 0 or requests.user.is_superuser:

            # user have access to see data
            if year == '0' and month == '0' and day == '0' and deadline_year == '0' and deadline_month == '0' and deadline_day == '0':

                # get all objects without time filter
                lwb_list = models.LiveWeighbridge.objects.all()

            else:

                # convert solar time to ad time
                year, month, day = utils.solar2ad(int(year), int(month), int(day))
                deadline_year, deadline_month, deadline_day = utils.solar2ad(int(deadline_year), int(deadline_month), int(deadline_day))

                # add time filter
                string = '{0}/{1}/{2}'.format(str(day), str(month), str(year))
                time_filter = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())

                string = '{0}/{1}/{2}'.format(str(deadline_day), str(deadline_month), str(deadline_year))
                deadline_time_filter = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())

                lwb_list = models.LiveWeighbridge.objects.all().filter(weighting_date__gte=time_filter).filter(weighting_date__lte=deadline_time_filter)

            if slaughter_status == '1':

                # add filter , if equal 1 it means return all True slaughter_status
                lwb_list = lwb_list.filter(slaughter_status=True)

            elif slaughter_status == '2':

                # add filter , if equal 2 it means return all False slaughter_status
                lwb_list = lwb_list.filter(slaughter_status=False)

            if product_category == '1':

                # add filter , if equal 1 it means return all of Chicken
                lwb_list = lwb_list.filter(product_category='C')

            elif product_category == '2':

                # add filter , if equal 2 it means return all of turkey
                lwb_list = lwb_list.filter(product_category='T')

            elif product_category == '3':

                # add filter , if equal 3 it means return all of quail
                lwb_list = lwb_list.filter(product_category='Q')

            if output_status == '0':

                lwb_temp = loader.get_template('WareHouseApp/live_WeighBridge_list.html')

            else:
                lwb_temp = loader.get_template('WareHouseApp/report_live_weighbridge.html')

            lwb_list_final = []
            lwb_report = [

                {

                    'car_weight': 0.0,
                    'car_final_weight': 0.0,
                    'weight': 0.0,
                    'average_weight': 0.0,
                    'total_buy_price': 0.0,
                    'average_each_buy_price': 0.0,
                    'losses_num': 0.0,
                    'losses_weight': 0.0,
                    'victim_num': 0.0,
                    'victim_weight': 0.0,
                    'total_num': 0.0,
                    'salughter_count': 0.0,
                    'salughter_count_dif': 0.0,
                    'fuel': 0.0,
                    'source_weight': 0.0,
                    'aviculture_avg_weight': 0.0,
                    'account_side': 0.0,
                    'drop_down': 0.0,
                    'rent': 0.0,

                },

                {

                    'car_weight': 0.0,
                    'car_final_weight': 0.0,
                    'weight': 0.0,
                    'average_weight': 0.0,
                    'total_buy_price': 0.0,
                    'average_each_buy_price': 0.0,
                    'losses_num': 0.0,
                    'losses_weight': 0.0,
                    'victim_num': 0.0,
                    'victim_weight': 0.0,
                    'total_num': 0.0,
                    'salughter_count': 0.0,
                    'salughter_count_dif': 0.0,
                    'fuel': 0.0,
                    'source_weight': 0.0,
                    'aviculture_avg_weight': 0.0,
                    'account_side': 0.0,
                    'drop_down': 0.0,
                    'rent': 0.0,

                },

                {

                    'car_weight': 0.0,
                    'car_final_weight': 0.0,
                    'weight': 0.0,
                    'average_weight': 0.0,
                    'total_buy_price': 0.0,
                    'average_each_buy_price': 0.0,
                    'losses_num': 0.0,
                    'losses_weight': 0.0,
                    'victim_num': 0.0,
                    'victim_weight': 0.0,
                    'total_num': 0.0,
                    'salughter_count': 0.0,
                    'salughter_count_dif': 0.0,
                    'fuel': 0.0,
                    'source_weight': 0.0,
                    'aviculture_avg_weight': 0.0,
                    'account_side': 0.0,
                    'drop_down': 0.0,
                    'rent': 0.0,


                },

            ]

            counter = 1
            for lwb in lwb_list:

                if lwb.product_category == 'C':
                    prod = 'chicken'

                    lwb_report[0]['car_weight'] += float(lwb.car_weight)
                    lwb_report[0]['car_final_weight'] += float(lwb.final_weight)
                    lwb_report[0]['weight'] += round(float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight, 2)
                    lwb_report[0]['average_weight'] += (float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight) / (int(lwb.cage_num * lwb.product_num_in_cage) - lwb.losses_num - lwb.victim_num)
                    lwb_report[0]['total_buy_price'] += round((float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight) * float(lwb.buy_price), 2)
                    lwb_report[0]['average_each_buy_price'] += round(((float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight) * float(lwb.buy_price)) / (int(lwb.cage_num * lwb.product_num_in_cage) - lwb.losses_num - lwb.victim_num), 2)
                    lwb_report[0]['losses_num'] += lwb.losses_num
                    lwb_report[0]['losses_weight'] += round(lwb.losses_weight, 2)
                    lwb_report[0]['victim_num'] += lwb.victim_num
                    lwb_report[0]['victim_weight'] += round(lwb.victim_weight, 2)
                    lwb_report[0]['total_num'] += lwb.cage_num * lwb.product_num_in_cage
                    lwb_report[0]['salughter_count'] += lwb.salughter_count
                    lwb_report[0]['salughter_count_dif'] += abs(lwb.salughter_count - int(lwb.cage_num * lwb.product_num_in_cage))
                    lwb_report[0]['fuel'] += lwb.fuel
                    lwb_report[0]['source_weight'] += lwb.source_weight
                    lwb_report[0]['aviculture_avg_weight'] += lwb.aviculture_avg_weight
                    lwb_report[0]['drop_down'] += ((float(lwb.final_weight) - float(lwb.car_weight) ) - lwb.source_weight) * -1 if ((float(lwb.final_weight) - float(lwb.car_weight) ) - lwb.source_weight)  > 0.0 else 0.0
                    lwb_report[0]['rent'] += lwb.driver_rent

                elif lwb.product_category == 'T':
                    prod = 'turkey'

                    lwb_report[1]['car_weight'] += float(lwb.car_weight)
                    lwb_report[1]['car_final_weight'] += float(lwb.final_weight)
                    lwb_report[1]['weight'] += round(float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight, 2)
                    lwb_report[1]['average_weight'] += (float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight) / (int(lwb.cage_num * lwb.product_num_in_cage) - lwb.losses_num - lwb.victim_num)
                    lwb_report[1]['total_buy_price'] += round((float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight) * float(lwb.buy_price), 2)
                    lwb_report[1]['average_each_buy_price'] += round(((float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight) * float(lwb.buy_price)) / (int(lwb.cage_num * lwb.product_num_in_cage) - lwb.losses_num - lwb.victim_num), 2)
                    lwb_report[1]['losses_num'] += lwb.losses_num
                    lwb_report[1]['losses_weight'] += round(lwb.losses_weight, 2)
                    lwb_report[1]['victim_num'] += lwb.victim_num
                    lwb_report[1]['victim_weight'] += round(lwb.victim_weight, 2)
                    lwb_report[1]['total_num'] += lwb.cage_num * lwb.product_num_in_cage
                    lwb_report[1]['salughter_count'] += lwb.salughter_count
                    lwb_report[1]['salughter_count_dif'] += abs(lwb.salughter_count - int(lwb.cage_num * lwb.product_num_in_cage))
                    lwb_report[1]['fuel'] += lwb.fuel
                    lwb_report[1]['source_weight'] += lwb.source_weight
                    lwb_report[1]['aviculture_avg_weight'] += lwb.aviculture_avg_weight
                    lwb_report[1]['drop_down'] += ((float(lwb.final_weight) - float(lwb.car_weight) ) - lwb.source_weight) * -1 if ((float(lwb.final_weight) - float(lwb.car_weight) ) - lwb.source_weight)  > 0.0 else 0.0
                    lwb_report[1]['rent'] += lwb.driver_rent

                elif lwb.product_category == 'Q':
                    prod = 'quail'

                    lwb_report[2]['car_weight'] += float(lwb.car_weight)
                    lwb_report[2]['car_final_weight'] += float(lwb.final_weight)
                    lwb_report[2]['weight'] += round(float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight, 2)
                    lwb_report[2]['average_weight'] += (float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight) / (int(lwb.cage_num * lwb.product_num_in_cage) - lwb.losses_num - lwb.victim_num)
                    lwb_report[2]['total_buy_price'] += round((float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight) * float(lwb.buy_price), 2)
                    lwb_report[2]['average_each_buy_price'] += round(((float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight) * float(lwb.buy_price)) / (int(lwb.cage_num * lwb.product_num_in_cage) - lwb.losses_num - lwb.victim_num), 2)
                    lwb_report[2]['losses_num'] += lwb.losses_num
                    lwb_report[2]['losses_weight'] += round(lwb.losses_weight, 2)
                    lwb_report[2]['victim_num'] += lwb.victim_num
                    lwb_report[2]['victim_weight'] += round(lwb.victim_weight, 2)
                    lwb_report[2]['total_num'] += lwb.cage_num * lwb.product_num_in_cage
                    lwb_report[2]['salughter_count'] += lwb.salughter_count
                    lwb_report[2]['salughter_count_dif'] += abs(lwb.salughter_count - int(lwb.cage_num * lwb.product_num_in_cage))
                    lwb_report[2]['fuel'] += lwb.fuel
                    lwb_report[2]['source_weight'] += lwb.source_weight
                    lwb_report[2]['aviculture_avg_weight'] += lwb.aviculture_avg_weight
                    lwb_report[2]['drop_down'] += ((float(lwb.final_weight) - float(lwb.car_weight) ) - lwb.source_weight) * -1 if ((float(lwb.final_weight) - float(lwb.car_weight) ) - lwb.source_weight)  > 0.0 else 0.0
                    lwb_report[2]['rent'] += lwb.driver_rent

                else:
                    prod = 'Nothing'

                lwb_list_final.append([

                    lwb.weighting_date_format,
                    lwb.final_weight,
                    lwb.car_weight,
                    round(float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight, 2),
                    round((float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight) / (int(lwb.cage_num * lwb.product_num_in_cage) - lwb.losses_num - lwb.victim_num),2),
                    lwb.order_weight,
                    round(lwb.losses_weight, 2),
                    lwb.losses_num,
                    round(lwb.victim_weight, 2),
                    lwb.victim_num,
                    lwb.cage_num,
                    lwb.product_num_in_cage,
                    (lwb.cage_num * lwb.product_num_in_cage) - lwb.losses_num - lwb.victim_num,
                    lwb.buy_price,
                    round((float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight) * float(lwb.buy_price), 2),
                    round(((float(lwb.final_weight) - float(lwb.car_weight) - lwb.losses_weight - lwb.victim_weight) * float(lwb.buy_price)) / (int(lwb.cage_num * lwb.product_num_in_cage) - lwb.losses_num - lwb.victim_num), 2),
                    lwb.slaughter_start_date_format if lwb.slaughter_start_date else '-',
                    lwb.slaughter_finish_date_format if lwb.slaughter_finish_date else '-',
                    prod,
                    lwb.driver.name + ' ' + lwb.driver.last_name,
                    str(lwb.car.car_number4) + ' ' + str(lwb.car.car_number3) + ' ' + str(lwb.car.car_number2) + ' ' + str(lwb.car.car_number1),
                    str(lwb.product_owner.name) + ' ' + str(lwb.product_owner.last_name),
                    lwb.avicultureـname,
                    lwb.avicultureـcity,
                    lwb.salughter_count,
                    abs(lwb.salughter_count - int(lwb.cage_num * lwb.product_num_in_cage) - lwb.losses_num - lwb.victim_num),
                    lwb.fuel,
                    lwb.source_weight,
                    lwb.aviculture_avg_weight,
                    lwb.account_side,
                    -1*((float(lwb.final_weight) - float(lwb.car_weight) ) - lwb.source_weight) if -1*((float(lwb.final_weight) - float(lwb.car_weight) ) - lwb.source_weight) > 0.0 else 0.0,
                    lwb.per_purchase,
                    lwb.per_sale,
                    lwb.sale_weight,
                    lwb.driver_rent,
                    counter,

                ])
                counter +=1

            for data in lwb_report:
                try:
                    data['average_weight'] /= len(lwb_list)
                    data['average_weight'] = round(data['average_weight'], 2)


                except:
                    pass

                data['total_buy_price'] = round(data['total_buy_price'], 2)

                try:
                    data['average_each_buy_price'] /= len(lwb_list)
                    data['average_each_buy_price'] = round(data['average_each_buy_price'], 2)

                except:
                    pass
            t = time.ctime(time.time() + information.time_dif).split()
            year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
            t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

            context = {

                "lwb_list": lwb_list_final,
                'report': lwb_report,
                'request': requests,
                'date' : t,
                'type': 'باسکول زنده (ورودی)'

            }

            return HttpResponse(lwb_temp.render(context))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def driver_list(requests, phone_number='0', product_category='0', model_type='0', year='0', month='0', day='0', deadline_year='0', deadline_month='0', deadline_day='0', output_type='0'):

    """
    show list of driver with filter
    """

    if requests.user.is_authenticated:

        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or requests.user.is_superuser:

            """ user have access """

            # check model type filter
            # if equal 0 we must return distribute and live weighbridge objects
            # if equal 1 we must return only live weighbridge objects
            # if equal 2 we must return only distribute objects
            # else we must return nothing
            if model_type == '0':

                dist_list = models.DistributedRoot.objects.all()
                lwb_list = models.LiveWeighbridge.objects.all()

            elif model_type == '1':

                dist_list = models.DistributedRoot.objects.all()
                lwb_list = models.LiveWeighbridge.objects.all().filter(car_weight=-5248.0)

            elif model_type == '2':

                dist_list = models.DistributedRoot.objects.all().filter(empty_weight=-5248.0)
                lwb_list = models.LiveWeighbridge.objects.all().filter()

            else:

                dist_list = models.DistributedRoot.objects.all().filter(empty_weight=-5248.0)
                lwb_list = models.LiveWeighbridge.objects.all().filter(car_weight=-5248.0)

            # we must add time filter . this filter help to see special time's objects
            # if all of them equal 0 we didn't add time filter
            # else we must add month and day and year filter
            if year != '0' and month != '0' and day != '0' and deadline_year != '0' and deadline_month != '0' and deadline_day != '0' :

                # convert solar time to ad time
                year, month, day = utils.solar2ad(int(year), int(month), int(day))
                deadline_year, deadline_month, deadline_day = utils.solar2ad(int(deadline_year), int(deadline_month), int(deadline_day))

                # add time filter
                string = '{0}/{1}/{2}'.format(str(day), str(month), str(year))
                time_filter = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())

                string = '{0}/{1}/{2}'.format(str(deadline_day), str(deadline_month), str(deadline_year))
                deadline_time_filter = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())

                lwb_list = lwb_list.filter(weighting_date__gte=time_filter).filter(weighting_date__lte=deadline_time_filter)
                dist_list = dist_list.filter(create_time__gte=time_filter).filter(create_time__lte=deadline_time_filter)

            # we must add driver phone number filter to return special driver objects
            # if equal 0 we didn't add filter
            # else we must add phone number filter
            if phone_number != '0':

                dist_list = dist_list.filter(driver__phone_number=phone_number)
                lwb_list = lwb_list.filter(driver__phone_number=phone_number)

            # we must add product category filter to return special product
            # if equal 1 we return only chicken objects
            # if equal 2 we return only turkey objects
            # if equal 3 we return only quail objects
            # else we didn't add filter
            if product_category == '1':

                # dist_list = dist_list.filter(product_category='C')
                lwb_list = lwb_list.filter(product_category='C')

            elif product_category == '2':

                # dist_list = dist_list.filter(product_category='T')
                lwb_list = lwb_list.filter(product_category='T')

            elif product_category == '3':

                # dist_list = dist_list.filter(product_category='Q')
                lwb_list = lwb_list.filter(product_category='Q')

            if output_type == '0':

                # load driver_list template
                driver_temp = loader.get_template('WareHouseApp/driver_list.html')

            else:

                driver_temp = loader.get_template('WareHouseApp/report_driver.html')

            # create list for store distribute data
            dist_final_list = []
            dist_final_report = [0.0, 0.0, 0.0]
            sub_dist_list = []
            sub_dist_report = []
            for dist in dist_list:

               dist_final_list.append([

                   dist.create_time_format,
                   dist.exit_time_format,
                   dist.empty_weight,
                   dist.full_weight,
                   dist.full_weight - dist.empty_weight,
                   dist.destination,
                   dist.driver.name + ' ' + dist.driver.lastname,
                   dist.driver.phone_number,
                   str(dist.car.car_number1) + ' ' + str(dist.car.car_number2) + ' ' + str(
                       dist.car.car_number3) + ' ' + str(dist.car.car_number4),

               ])

               dist_final_report[0] += dist.empty_weight
               dist_final_report[1] += dist.full_weight
               dist_final_report[2] += dist.full_weight - dist.empty_weight

               if prod_category == '1':

                    sub_dist = models.Distributed.objects.all().filter(distribute_root=dist).filter(product_category='C')

               elif prod_category == '2':

                    sub_dist = models.Distributed.objects.all().filter(distribute_root=dist).filter(product_category='T')

               elif prod_category == '3':

                    sub_dist = models.Distributed.objects.all().filter(distribute_root=dist).filter(product_category='Q')

               else:

                    sub_dist = models.Distributed.objects.all().filter(distribute_root=dist)

               for sub in sub_dist:

                    # change database product_category attribute from abbreviation to complete word
                    if sub.product_category == 'C':
                        prod_category = 'chicken'

                    elif sub.product_category == 'T':
                        prod_category = 'turkey'

                    elif sub.product_category == 'Q':
                        prod_category = 'quail'
                    else:
                        '-'

                    dist_final_list.append([

                        sub.distribute_root.driver.name + " " + sub.distribute_root.driver.last_name,
                        sub.distribute_root.driver.phone_number,
                        str(sub.distribute_root.car.car_number1) + ' ' + str(sub.distribute_root.car.car_number2) + ' ' + str(
                            sub.distribute_root.car.car_number3) + ' ' + str(sub.distribute_root.car.car_number4),

                        dist.driver.car.product_owner.name, dist.driver.car.product_owner.last_name,
                        dist.weight, dist.date_format, dist.sale_price, prod_category,
                        dist.bill_of_lading, dist.number_of_box

                    ])

            # create live weighbridge final list for change and store data
            lwb_final_list = []
            for lwb in lwb_list:

                # change database product_category attribute from abbreviation to complete word
                if lwb.product_category == 'C':
                    prod_category = 'Chicken'

                elif lwb.product_category == 'T':
                    prod_category = 'turkey'

                elif lwb.product_category == 'Q':
                    prod_category = 'Quail'

                lwb_final_list.append([

                    lwb.driver.name, lwb.driver.last_name, lwb.driver.phone_number,
                    lwb.driver.car.car_number,
                    lwb.driver.car.product_owner.name, lwb.driver.car.product_owner.last_name,
                    lwb.final_weight, lwb.car_weight, lwb.car_empty, lwb.weighting_date_format,
                    prod_category, lwb.slaughter_status,
                    lwb.slaughter_start_date_format if lwb.slaughter_start_date else '-',
                    lwb.slaughter_finish_date_format if lwb.slaughter_finish_date else '-',
                    lwb.buy_price, lwb.avicultureـname,lwb.avicultureـcity

                ])

            # return data
            context = {

                'dist_list': dist_final_list,
                'lwb_list': lwb_final_list,
                'request': requests

            }

            return HttpResponse(driver_temp.render(context))

    # user can't access to this page
    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def car_list(requests, car_number='0', product_category='0', model_type='0', year='0', month='0', day='0'):

    """
    show list of car with filter
    """

    if requests.user.is_authenticated:

        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or requests.user.is_superuser:

            """ user have access """

            # check model type filter
            # if equal 0 we must return distribute and live weighbridge objects
            # if equal 1 we must return only live weighbridge objects
            # if equal 2 we must return only distribute objects
            # else we must return nothing
            if model_type == '0':

                dist_list = models.Distributed.objects.all()
                lwb_list = models.LiveWeighbridge.objects.all()

            elif model_type == '1':

                dist_list = models.Distributed.objects.all()
                lwb_list = models.LiveWeighbridge.objects.all().filter(car_weight=-5248.0)

            elif model_type == '2':

                dist_list = models.Distributed.objects.all().filter(weight=-5248.0)
                lwb_list = models.LiveWeighbridge.objects.all().filter()

            else:

                dist_list = models.Distributed.objects.all().filter(weight=-5248.0)
                lwb_list = models.LiveWeighbridge.objects.all().filter(car_weight=-5248.0)

            # we must add time filter . this filter help to see special time's objects
            # if all of them equal 0 we didn't add time filter
            # else we must add month and day and year filter
            if year != '0' and month != '0' and day != '0':
                # add time filter
                string = '{0}/{1}/{2}'.format(str(day), str(month), str(year))
                time_filter = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())

                lwb_list = lwb_list.filter(weighting_date__gte=time_filter).filter(
                    weighting_date__lte=time_filter + (60 * 60 * 24))
                dist_list = dist_list.filter(date__gte=time_filter).filter(date__lte=time_filter + (60 * 60 * 24))

            # we must add car car_number filter to return special car objects
            # if equal 0 we didn't add filter
            # else we must add car number filter
            if car_number != '0':

                dist_list = dist_list.filter(driver__car__car_number=car_number)
                lwb_list = lwb_list.filter(driver__car__car_number=car_number)

            # we must add product category filter to return special product
            # if equal 1 we return only chicken objects
            # if equal 2 we return only turkey objects
            # if equal 3 we return only quail objects
            # else we didn't add filter
            if product_category == '1':

                dist_list = dist_list.filter(product_category='C')
                lwb_list = lwb_list.filter(product_category='C')

            elif product_category == '2':

                dist_list = dist_list.filter(product_category='T')
                lwb_list = lwb_list.filter(product_category='T')

            elif product_category == '3':

                dist_list = dist_list.filter(product_category='Q')
                lwb_list = lwb_list.filter(product_category='Q')

            # load car_list template
            car_temp = loader.get_template('WareHouseApp/car_list.html')

            # create list for store distribute data
            dist_final_list = []
            for dist in dist_list:

                # change database product_category attribute from abbreviation to complete word
                if dist.product_category == 'C':
                    prod_category = 'chicken'

                elif dist.product_category == 'T':
                    prod_category = 'turkey'

                elif dist.product_category == 'Q':
                    prod_category = 'quail'

                else:
                    '-'

                dist_final_list.append([

                    dist.driver.name, dist.driver.last_name, dist.driver.phone_number,
                    dist.driver.car.car_number,
                    dist.driver.car.product_owner.name, dist.driver.car.product_owner.last_name,
                    dist.weight, dist.date_format, dist.sale_price, prod_category,
                    dist.bill_of_lading, dist.number_of_box

                ])

            # create live weighbridge final list for change and store data
            lwb_final_list = []
            for lwb in lwb_list:

                # change database product_category attribute from abbreviation to complete word
                if lwb.product_category == 'C':
                    prod_category = 'Chicken'

                elif lwb.product_category == 'T':
                    prod_category = 'turkey'

                elif lwb.product_category == 'Q':
                    prod_category = 'Quail'

                lwb_final_list.append([

                    lwb.driver.name, lwb.driver.last_name, lwb.driver.phone_number,
                    lwb.driver.car.car_number,
                    lwb.driver.car.product_owner.name, lwb.driver.car.product_owner.last_name,
                    lwb.final_weight, lwb.car_weight, lwb.car_empty, lwb.weighting_date_format,
                    prod_category, lwb.slaughter_status,
                    lwb.slaughter_start_date_format if lwb.slaughter_start_date else '-',
                    lwb.slaughter_finish_date_format if lwb.slaughter_finish_date else '-',
                    lwb.buy_price, lwb.avicultureـname, lwb.avicultureـcity

                ])

            # return data
            context = {

                'dist_list': dist_final_list,
                'lwb_list': lwb_final_list,
                'request': requests

            }

            return HttpResponse(car_temp.render(context))

    # user can't access to this page
    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def product_owner_list(requests, po_name='0', po_lastname='0', product_category='0', model_type='0', year='0',
                       month='0', day='0', car_number='0'):

    """
    show list of product owner with filter
    """

    if requests.user.is_authenticated:

        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or requests.user.is_superuser:

            """ user have access """

            # check model type filter
            # if equal 0 we must return distribute and live weighbridge and pre-cold and freeze tunnel objects
            # if equal 1 we must return only live weighbridge objects
            # if equal 2 we must return only distribute objects
            # if equal 3 we must return only pre-cold objects
            # if equal 4 we must return only freeze tunnel objects
            # else we must return nothing
            if model_type == '0':

                dist_list = models.Distributed.objects.all()
                lwb_list = models.LiveWeighbridge.objects.all()
                pd_list = models.PreCold.objects.all()
                ft_list = models.FreezingTunnel.objects.all()

            elif model_type == '1':

                dist_list = models.Distributed.objects.all()
                lwb_list = models.LiveWeighbridge.objects.all().filter(car_weight=-5248.0)
                pd_list = models.PreCold.objects.all().filter(weight=-5)
                ft_list = models.FreezingTunnel.objects.all().filter(weight=-5)

            elif model_type == '2':

                dist_list = models.Distributed.objects.all().filter(weight=-5248.0)
                lwb_list = models.LiveWeighbridge.objects.all().filter()
                pd_list = models.PreCold.objects.all().filter(weight=-5)
                ft_list = models.FreezingTunnel.objects.all().filter(weight=-5)

            elif model_type == '3':

                dist_list = models.Distributed.objects.all().filter(weight=-5248.0)
                lwb_list = models.LiveWeighbridge.objects.all().filter(car_weight=-5)
                pd_list = models.PreCold.objects.all()
                ft_list = models.FreezingTunnel.objects.all().filter(weight=-5)

            elif model_type == '4':

                dist_list = models.Distributed.objects.all().filter(weight=-5248.0)
                lwb_list = models.LiveWeighbridge.objects.all().filter(car_weight=-5)
                pd_list = models.PreCold.objects.all().filter(weight=-5)
                ft_list = models.FreezingTunnel.objects.all()

            else:

                dist_list = models.Distributed.objects.all().filter(weight=-5248.0)
                lwb_list = models.LiveWeighbridge.objects.all().filter(car_weight=-5248.0)
                pd_list = models.PreCold.objects.all().filter(weight=-5)
                ft_list = models.FreezingTunnel.objects.all().filter(weight=-5)

            # we must add time filter . this filter help to see special time's objects
            # if all of them equal 0 we didn't add time filter
            # else we must add month and day and year filter
            if year != '0' and month != '0' and day != '0':

                # add time filter
                string = '{0}/{1}/{2}'.format(str(day), str(month), str(year))
                time_filter = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())

                lwb_list = lwb_list.filter(weighting_date__gte=time_filter).filter(
                    weighting_date__lte=time_filter + (60 * 60 * 24))

                dist_list = dist_list.filter(date__gte=time_filter).filter(date__lte=time_filter + (60 * 60 * 24))

                pd_list = pd_list.filter(entry_time__gte=time_filter).filter(
                    entry_time__lte=time_filter + (60 * 60 * 24))

                ft_list = ft_list.filter(entry_date__gte=time_filter).filter(entry_date__lte=time_filter + (60 * 60 * 24))

            # we must add car car_number filter to return special car objects
            # if equal 0 we didn't add filter
            # else we must add car number filter
            if po_name != '0' and po_lastname != '0':

                dist_list = dist_list.filter(driver__car__product_owner__name=po_name).filter(
                    driver__car__product_owner__last_name=po_lastname)

                lwb_list = lwb_list.filter(driver__car__product_owner__name=po_name).filter(
                    driver__car__product_owner__last_name=po_lastname)

                pd_list = pd_list.filter(
                    First_Weight_Lifting__Live_Weigh_Bridge__driver__car__product_owner__name=po_name).filter(
                    First_Weight_Lifting__Live_Weigh_Bridge__driver__car__product_owner__last_name=po_lastname
                )

                ft_list = ft_list.filter(
                    first_weight_lifting__Live_Weigh_Bridge__driver__car__product_owner__name=po_name).filter(
                    first_weight_lifting__Live_Weigh_Bridge__driver__car__product_owner__last_name=po_lastname
                )

            # car number filter
            if car_number != '0':

                dist_list = dist_list.filter(driver__car__car_number=car_number)
                lwb_list = lwb_list.filter(driver__car__car_number=car_number)
                pd_list = pd_list.filter(First_Weight_Lifting__Live_Weigh_Bridge__driver__car__car_number=car_number)
                ft_list = ft_list.filter(first_weight_lifting__Live_Weigh_Bridge__driver__car__car_number=car_number)

            # we must add product category filter to return special product
            # if equal 1 we return only chicken objects
            # if equal 2 we return only turkey objects
            # if equal 3 we return only quail objects
            # else we didn't add filter
            if product_category == '1':

                dist_list = dist_list.filter(product_category='C')
                lwb_list = lwb_list.filter(product_category='C')
                pd_list = pd_list.filter(product_category='C')
                ft_list = ft_list.filter(product_category='C')

            elif product_category == '2':

                dist_list = dist_list.filter(product_category='T')
                lwb_list = lwb_list.filter(product_category='T')
                pd_list = pd_list.filter(product_category='T')
                ft_list = ft_list.filter(product_category='T')

            elif product_category == '3':

                dist_list = dist_list.filter(product_category='Q')
                lwb_list = lwb_list.filter(product_category='Q')
                pd_list = pd_list.filter(product_category='Q')
                ft_list = ft_list.filter(product_category='Q')

            # load product_owner template
            po_temp = loader.get_template('WareHouseApp/product_owner_list.html')

            # create list for store distribute data
            dist_final_list = []
            for dist in dist_list:

                # change database product_category attribute from abbreviation to complete word
                if dist.product_category == 'C':
                    prod_category = 'chicken'

                elif dist.product_category == 'T':
                    prod_category = 'turkey'

                elif dist.product_category == 'Q':
                    prod_category = 'quail'
                else:
                    '-'

                dist_final_list.append([

                    dist.driver.name, dist.driver.last_name, dist.driver.phone_number,
                    dist.driver.car.car_number,
                    dist.driver.car.product_owner.name, dist.driver.car.product_owner.last_name,
                    dist.weight, dist.date_format, dist.sale_price, prod_category,
                    dist.bill_of_lading, dist.number_of_box

                ])

            # create live weighbridge final list for change and store data
            lwb_final_list = []
            for lwb in lwb_list:

                # change database product_category attribute from abbreviation to complete word
                if lwb.product_category == 'C':
                    prod_category = 'Chicken'

                elif lwb.product_category == 'T':
                    prod_category = 'turkey'

                elif lwb.product_category == 'Q':
                    prod_category = 'Quail'

                lwb_final_list.append([

                    lwb.driver.name, lwb.driver.last_name, lwb.driver.phone_number,
                    lwb.driver.car.car_number,
                    lwb.driver.car.product_owner.name, lwb.driver.car.product_owner.last_name,
                    lwb.final_weight, lwb.car_weight, lwb.car_empty, lwb.weighting_date_format,
                    prod_category, lwb.slaughter_status,
                    lwb.slaughter_start_date_format if lwb.slaughter_start_date else '-',
                    lwb.slaughter_finish_date_format if lwb.slaughter_finish_date else '-',
                    lwb.buy_price, lwb.avicultureـname, lwb.avicultureـcity

                ])

            # create pre-cold final list for change and store pre-cold model's data
            pd_final_list = []
            for pd in pd_list:

                # change database product_category attribute from abbreviation to complete word
                if pd.product_category == 'C':
                    prod_category = 'Chicken'

                elif pd.product_category == 'T':
                    prod_category = 'turkey'

                elif pd.product_category == 'Q':
                    prod_category = 'Quail'

                pd_final_list.append([

                    pd.First_Weight_Lifting.Live_Weigh_Bridge.driver.car.product_owner.name,
                    pd.First_Weight_Lifting.Live_Weigh_Bridge.driver.car.product_owner.last_name,
                    pd.First_Weight_Lifting.Live_Weigh_Bridge.driver.name,
                    pd.First_Weight_Lifting.Live_Weigh_Bridge.driver.last_name,
                    pd.First_Weight_Lifting.Live_Weigh_Bridge.driver.phone_number,
                    pd.First_Weight_Lifting.Live_Weigh_Bridge.driver.car.car_number,
                    pd.First_Weight_Lifting.weighting_time_format,
                    pd.First_Weight_Lifting.weight,
                    'pre-cold',
                    pd.pre_cold_id,
                    pd.pallet_id,
                    pd.product_pre_cold_status,
                    prod_category,
                    pd.weight,
                    pd.entry_time_format,
                    '-' if pd.product_pre_cold_status else pd.exit_time_format,

                ])

            # create pre-cold final list for change and store pre-cold model's data
            ft_final_list = []
            for ft in ft_list:

                # change database product_category attribute from abbreviation to complete word
                if ft.product_category == 'C':
                    prod_category = 'Chicken'

                elif ft.product_category == 'T':
                    prod_category = 'turkey'

                elif ft.product_category == 'Q':
                    prod_category = 'Quail'

                ft_final_list.append([

                    ft.first_weight_lifting.Live_Weigh_Bridge.driver.car.product_owner.name,
                    ft.first_weight_lifting.Live_Weigh_Bridge.driver.car.product_owner.last_name,
                    ft.first_weight_lifting.Live_Weigh_Bridge.driver.name,
                    ft.first_weight_lifting.Live_Weigh_Bridge.driver.last_name,
                    ft.first_weight_lifting.Live_Weigh_Bridge.driver.phone_number,
                    ft.first_weight_lifting.Live_Weigh_Bridge.driver.car.car_number,
                    ft.first_weight_lifting.weighting_time_format,
                    ft.first_weight_lifting.weight,
                    'freeze tunnel',
                    ft.entry_date_format,
                    '-' if ft.status else ft.exit_date_format,
                    ft.weight,
                    ft.tunnel_id,
                    ft.pallet_id,
                    prod_category,

                ])

            # return data
            context = {

                'dist_list': dist_final_list,
                'lwb_list': lwb_final_list,
                'ft_list': ft_final_list,
                'pd_list': pd_final_list,
                'request': requests

            }

            return HttpResponse(po_temp.render(context))

    # user can't access to this page
    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def weight_lifting_list(requests, product_category='0', model_type='0', year='0', month='0', day='0', deadline_year='0', deadline_month='0', deadline_day='0', output_type='0'):

    """
    show list of first weightlifting with filter
    """

    if requests.user.is_authenticated:

        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or requests.user.is_superuser:

            """ user have access """

            if model_type == '0':

                fwl_list = models.FirstWeightLifting.objects.all()

            elif model_type == '1':

                fwl_list = models.FirstWeightLifting.objects.all().filter(sales_category='P')

            elif model_type == '2':

                fwl_list = models.FirstWeightLifting.objects.all().filter(sales_category='D')

            elif model_type == '3':

                fwl_list = models.FirstWeightLifting.objects.all().filter(sales_category='F')

            elif model_type == '4':

                fwl_list = models.FirstWeightLifting.objects.all().filter(sales_category='G')

            else:

                fwl_list = models.FirstWeightLifting.objects.all().filter(sales_category='Z')

            # we must add time filter . this filter help to see special time's objects
            # if all of them equal 0 we didn't add time filter
            # else we must add month and day and year filter
            if year != '0' and month != '0' and day != '0':
                # add time filter
                # add time filter
                string = '{0}/{1}/{2}'.format(str(day), str(month), str(year))
                time_filter = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())

                string = '{0}/{1}/{2}'.format(str(deadline_day), str(deadline_month), str(deadline_year))
                deadline_time_filter = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())

                fwl_list = fwl_list.filter(weighting_time__gte=time_filter).filter(weighting_time__lte=deadline_time_filter)

            # we must add product category filter to return special product
            # if equal 1 we return only chicken objects
            # if equal 2 we return only turkey objects
            # if equal 3 we return only quail objects
            # else we didn't add filter
            if product_category == '1':

                fwl_list = fwl_list.filter(product_category='C')
            elif product_category == '2':

                fwl_list = fwl_list.filter(product_category='T')

            elif product_category == '3':

                fwl_list = fwl_list.filter(product_category='Q')
            if output_type == '0':

                # load product_owner template
                po_temp = loader.get_template('WareHouseApp/weight_lifting_list.html')
            else:
                po_temp = loader.get_template('WareHouseApp/report_fwl.html')

            # create list for store distribute data
            final_list = []
            total_list = [

                [0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0],

            ]
            counter = 0
            total__weight = 0
            total__weight_1 = 0

            for fwl in fwl_list:
                counter += 1

                # change database product_category attribute from abbreviation to complete word
                if fwl.product_category == 'C':
                    prod_category = 'مرغ'
                    row = 0

                elif fwl.product_category == 'T':
                    prod_category = 'بوقلمون'
                    row = 1

                elif fwl.product_category == 'Q':
                    prod_category = 'بلدرچین'
                    row = 2

                if fwl.sales_category == 'P' :
                    sale_cat = 'پیش سرد'
                    col = 0

                elif fwl.sales_category == 'D':
                    sale_cat = 'فروش گرم'
                    col = 1

                elif fwl.sales_category == 'F':
                    sale_cat = 'تونل انجماد'
                    col = 2

                elif fwl.sales_category == 'G':
                    sale_cat = 'قطعه بندی'
                    col = 3

                elif fwl.sales_category == 'Z':
                    sale_cat = 'پودر گوشت'
                    col = 4

                total_list[row][col] += fwl.weight
                total_list[-1][col] += fwl.weight

                final_list.append([

                    counter,
                    fwl.product_owner.name + ' '+ fwl.product_owner.last_name,
                    fwl.weighting_time_format,
                    fwl.weight,
                    'درجه یک' if fwl.class_product else 'درجه دو',
                    prod_category,
                    fwl.code,
                    sale_cat,
                    fwl.Weight_Lifting_Manager,

                ])

                total__weight += fwl.weight
                total__weight_1 += 0.0 if fwl.class_product else fwl.weight

            final_list.append([

                'مجموع',
                '-',
                '-',
                total__weight,
                total__weight_1,
                '-',
                '-',
                '-',
                '-',

            ])

            t = time.ctime(time.time() + information.time_dif).split()
            year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
            t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

            # return data
            context = {

                'request': requests,
                'fwl_list': final_list,
                'tl': total_list,
                'date': t,
                'type': 'گزارش وزن کشی مرحله اول',

            }

            return HttpResponse(po_temp.render(context))

    # user can't access to this page
    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def cold_house_list(requests, product_category='0', model_type='0', year='0', month='0', day='0', exist='0'):

    """
    show list of cold house and paper box objects with filter
    """

    if requests.user.is_authenticated:

        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or requests.user.is_superuser:

            """ user have access """

            # check model type filter
            # if equal 0 we must return cold house and paper box objects
            # if equal 1 we must return only cold house objects
            # if equal 2 we must return only paper box objects
            # else we must return nothing
            if model_type == '0':

                ch_list = models.ColdHouse.objects.all()
                pb_list = models.PaperBox.objects.all()

            elif model_type == '1':

                ch_list = models.ColdHouse.objects.all()
                pb_list = models.PaperBox.objects.all().filter(number_of_product=-5)

            elif model_type == '2':

                ch_list = models.ColdHouse.objects.all().filter(number_of_box=-5)
                pb_list = models.PaperBox.objects.all()

            else:

                ch_list = models.ColdHouse.objects.all().filter(number_of_box=-5)
                pb_list = models.PaperBox.objects.all().filter(number_of_product=-5)

            # we must add time filter . this filter help to see special time's objects
            # if all of them equal 0 we didn't add time filter
            # else we must add month and day and year filter
            if year != '0' and month != '0' and day != '0':
                # add time filter
                string = '{0}/{1}/{2}'.format(str(day), str(month), str(year))
                time_filter = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())

                pb_list = pb_list.filter(packing_time__gte=time_filter).filter(packing_time__lte=time_filter + (60 * 60 * 24))

                ch_list = ch_list.filter(entry_date__gte=time_filter).filter(
                    entry_date__lte=time_filter + (60 * 60 * 24))

            # check product exist in freeze tunnel and pre-cold or not
            # if equal 1 it will check all of exist
            # if equal 2 it will check didn't exist
            # else didn't apply filter
            if exist == '1':

                ch_list = ch_list.filter(pallet_status=True)
                pb_list = pb_list.filter(box_status=True)

            elif exist == '2':

                ch_list = ch_list.filter(pallet_status=False)
                pb_list = pb_list.filter(box_status=False)

            # we must add product category filter to return special product
            # if equal 1 we return only chicken objects
            # if equal 2 we return only turkey objects
            # if equal 3 we return only quail objects
            # else we didn't add filter
            if product_category == '1':

                pb_list = pb_list.filter(product_category='C')

            elif product_category == '2':

                pb_list = pb_list.filter(product_category='T')

            elif product_category == '3':

                pb_list = pb_list.filter(product_category='Q')

            # load coldHouse template
            ch_temp = loader.get_template('WareHouseApp/cold_house_list.html')

            # create coldHouse list
            ch_final_list = []
            for ch in ch_list:

                ch_final_list.append([

                    ch.entry_date_format,
                    '-' if ch.pallet_status else ch.exit_date_format,
                    ch.pallet_status,
                    ch.total_pallet_weight,
                    ch.pallet_weight_without_product,
                    ch.number_of_box,
                    ch.pallet_id,
                    ch.cold_house_id

                ])

            # create paper box objects
            pb_final_list = []
            for pb in pb_list:
                if pb.cold_house:

                    if pb.product_category == 'C':
                        prod_category = 'Chicken'

                    elif pb.product_category == 'T':
                        prod_category = 'turkey'

                    elif pb.product_category == 'Q':
                        prod_category = 'Quail'

                    else:
                        '-'
                    pack_time = pb.packing_time + (pb.expiration_time * 3600 * 24)
                    exp = int((time.time() - pack_time) / (3600 * 24))

                    if exp >= 0:
                        exp_state = False
                    else:
                        exp_state = True

                    pb_final_list.append([

                        prod_category,
                        pb.paper_box_weight,
                        pb.box_status,
                        pb.number_of_product,
                        pb.packing_time_format,
                        pb.box_id,
                        pb.cold_house.pallet_id,
                        pb.cold_house.cold_house_id,
                        pb.sub_product_category,
                        exp,
                        exp_state

                    ])

            # return data
            context = {

                'pb_list': pb_final_list,
                'ch_list': ch_final_list,
                'request': requests

            }

            return HttpResponse(ch_temp.render(context))

    # user can't access to this page
    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def lw_filter(requests):

    """
    filter view for live weighbridge list
    """

    return HttpResponseRedirect(reverse('Company_Live_WeighBridge_List', args=[

        requests.POST['year'],
        requests.POST['month'],
        requests.POST['day'],
        requests.POST['deadline_year'],
        requests.POST['deadline_month'],
        requests.POST['deadline_day'],
        requests.POST['output_status'],
        requests.POST['product_category'],
        requests.POST['slaughter_status'],

    ]))


@csrf_exempt
def driver_filter(requests):
    """
    filter view for driver list
    """

    return HttpResponseRedirect(reverse('Driver_List', args=[

        requests.POST['year'],
        requests.POST['month'],
        requests.POST['day'],
        requests.POST['phone_number'],
        requests.POST['product_category'],
        requests.POST['model_type'],

    ]))


@csrf_exempt
def car_filter(requests):
    """
    filter view for car list
    """

    return HttpResponseRedirect(reverse('Car_List', args=[

        requests.POST['year'],
        requests.POST['month'],
        requests.POST['day'],
        requests.POST['car_number'],
        requests.POST['product_category'],
        requests.POST['model_type'],

    ]))


@csrf_exempt
def po_filter(requests):
    """
    filter view for product owner list
    """

    return HttpResponseRedirect(reverse('Product_Owner_List', args=[

        requests.POST['year'],
        requests.POST['month'],
        requests.POST['day'],
        requests.POST['po_name'],
        requests.POST['po_lastname'],
        requests.POST['product_category'],
        requests.POST['model_type'],
        requests.POST['car_number'],

    ]))


@csrf_exempt
def wl_filter(requests):
    """
    filter view for weight lifting list
    """

    return HttpResponseRedirect(reverse('Weight_Lifting_List', args=[

        requests.POST['year'],
        requests.POST['month'],
        requests.POST['day'],
        requests.POST['deadline_year'],
        requests.POST['deadline_month'],
        requests.POST['deadline_day'],
        requests.POST['product_category'],
        requests.POST['model_type'],
        requests.POST['output_type'],

    ]))


@csrf_exempt
def ch_filter(requests):

    """
    filter view for cold house list
    """

    return HttpResponseRedirect(reverse('Cold_House_List', args=[

        requests.POST['year'],
        requests.POST['month'],
        requests.POST['day'],
        requests.POST['product_category'],
        requests.POST['model_type'],
        requests.POST['exist'],

    ]))


######################################
######################################
"""       Automation               """
######################################
######################################


def automation_file_create_form(requests):

    """
    create automation
    """

    if requests.user.is_authenticated:

        html_load = loader.get_template('WareHouseApp/automation_file.html')

        context = {

            'request': requests,
            'user_list' : User.objects.all(),
            'code' : random.randint(1000,9999)

        }

        return HttpResponse(html_load.render(context))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def automation_file_create(requests):

    """
    automation file create
    """

    if requests.user.is_authenticated:

        # get param
        subject = requests.POST['subject']
        code = requests.POST['code']
        file_obj = requests.FILES.get('file')

        print('file object :\n', file_obj)


        # create automation
        automation_obj = models.Automation()

        # set param
        automation_obj.automation_id = str(uuid1().int)
        automation_obj.automation_create_time = time.time() + information.time_dif
        t = time.ctime(time.time() + information.time_dif).split()
        year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
        t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

        automation_obj.automation_create_time_format = t
        automation_obj.code = str(code)
        automation_obj.automation_type = 'F'
        automation_obj.automation_create_user = requests.user

        # save
        automation_obj.save()

        # automation file
        automation_file = models.FileAutomation()

        # set param
        automation_file.file = file_obj
        automation_file.subject = subject
        automation_file.file_automation_id = str(uuid1().int)
        automation_file.automation = automation_obj

        # save
        automation_file.save()

        for key in requests.POST.keys():

            if key[0] == '@':

                # create user automation
                user_automation = models.UserAutomation()

                # set param
                user_automation.user = User.objects.get_by_natural_key(requests.POST[key])
                user_automation.automation_input_type = 'F'
                user_automation.automation_input_id = automation_file.file_automation_id

                # save
                user_automation.save()

        return HttpResponseRedirect(reverse('automation'))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def automation_message_create_form(requests):

    """
    automation message create form
    """
    if requests.user.is_authenticated:

        html_load = loader.get_template('WareHouseApp/automation_message.html')

        context = {

            'request': requests,
            'user_list': User.objects.all(),
            'code': random.randint(1000, 9999)

        }

        return HttpResponse(html_load.render(context))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def automation_message_create(requests):

    """
    automation file create
    """

    if requests.user.is_authenticated:

        # get param
        subject = requests.POST['subject']
        code = requests.POST['code']
        content = requests.POST['content']

        # create automation
        automation_obj = models.Automation()

        # set param
        automation_obj.automation_id = str(uuid1().int)
        automation_obj.automation_create_time = time.time() + information.time_dif
        t = time.ctime(time.time() + information.time_dif).split()
        year, month, day, week_day = utils.ad2solar(year=int(t[-1]), month=t[1], day=int(t[2]), week_day=t[0])
        t = '{0}/{1}/{2} {3} {4}'.format(str(year), str(month), str(day), str(week_day), str(t[3]))

        automation_obj.automation_create_time_format = t
        automation_obj.code = str(code)
        automation_obj.automation_type = 'M'
        automation_obj.automation_create_user = User.objects.get(username=requests.user.username)

        # save
        automation_obj.save()

        # automation message
        automation_msg = models.MessageAutomation()

        # set param
        automation_msg.content = content
        automation_msg.subject = subject
        automation_msg.message_id = str(uuid1().int)
        automation_msg.automation = automation_obj

        # save
        automation_msg.save()

        for key in requests.POST.keys():

            if key[0] == '@':

                # create user automation
                user_automation = models.UserAutomation()

                # set param
                user_automation.user = User.objects.get_by_natural_key(requests.POST[key])
                user_automation.automation_input_type = 'M'
                user_automation.automation_input_id = automation_msg.message_id

                # save
                user_automation.save()

        return HttpResponseRedirect(reverse('automation'))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def automation_view(requests, id):

    """
    view automation
    """

    if requests.user.is_authenticated:

        # get object
        automation_obj = models.Automation.objects.get(automation_id=id)
        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if automation_obj.automation_type == 'M':

            sub_automation = models.MessageAutomation.objects.get(automation__automation_id=id)

            if requests.user.is_superuser or len(ceo_list) > 0:
                user_view = models.UserAutomation.objects.all().filter(automation_input_id=sub_automation.message_id)

            else:
                user_view = models.UserAutomation.objects.all().filter(
                    user__username=requests.user.username).filter(automation_input_id=sub_automation.message_id)

            user_viewx = user_view[0]

            if len(user_view) > 0 or requests.user.is_superuser or ceo_list > 0 or automation_obj.automation_create_user.username == requests.user.username:

                user_viewx.view_status = True
                user_viewx.save()

                temp = loader.get_template('WareHouseApp/automation_view.html')

                context = {

                    'request': requests,
                    'automation': automation_obj,
                    'sub_automation': sub_automation,
                    'user_automation': models.UserAutomation.objects.all().filter(automation_input_id=sub_automation.message_id)

                }

                return HttpResponse(temp.render(context))

        elif automation_obj.automation_type == 'F':

            sub_automation = models.FileAutomation.objects.get(automation__automation_id=id)

            if requests.user.is_superuser or len(ceo_list) > 0 :
                user_view = models.UserAutomation.objects.all().filter(automation_input_id=sub_automation.file_automation_id)

            else:
                user_view = models.UserAutomation.objects.all().filter(
                    user__username=requests.user.username).filter(automation_input_id=sub_automation.file_automation_id)

            user_viewx = user_view[0]

            if len(user_view) > 0 or requests.user.is_superuser or ceo_list > 0 or automation_obj.automation_create_user.username == requests.user.username:

                user_viewx.view_status = True
                user_viewx.save()

                # read data
                data = open(sub_automation.file.path, 'rb' )
                mime_type, _ = mimetypes.guess_type(sub_automation.file.path)
                response = HttpResponse(data, content_type=mime_type)
                response['Content-Disposition'] = "attachment; filename=%s" % str(sub_automation.subject)

                if requests.user.is_superuser or len(ceo_list) > 0:
                    user_view = models.UserAutomation.objects.all().filter(
                        automation_input_id=sub_automation.file_automation_id)[0]

                else:
                    user_view = models.UserAutomation.objects.all().filter(
                        user__username=requests.user.username).filter(
                        automation_input_id=sub_automation.file_automation_id)[0]

                user_view.view_status = True

                user_view.save()
                return response

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def automation_delete(requests, id):

    """
    delete automation
    """

    if requests.user.is_authenticated:

        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or requests.user.is_superuser:

            automation_obj = models.Automation.objects.get(automation_id=id)

            if automation_obj.automation_type == 'M':

                sub_automation = models.MessageAutomation.objects.get(automation__automation_id=id)

                user_view = models.UserAutomation.objects.all().filter(automation_input_id=sub_automation.message_id)

                for user in user_view:

                    user.delete()

                sub_automation.delete()
                automation_obj.delete()

                return HttpResponseRedirect(reverse('automation'))

            elif automation_obj.automation_type == 'F':

                sub_automation = models.FileAutomation.objects.get(automation__automation_id=id)

                user_view = models.UserAutomation.objects.all().filter(automation_input_id=sub_automation.file_automation_id)

                for user in user_view:
                    user.delete()

                sub_automation.delete()

                automation_obj.delete()

                return HttpResponseRedirect(reverse('automation'))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def automation_send_list(requests, status):

    """
    show automation send list
    """

    if requests.user.is_authenticated:

        temp = loader.get_template('WareHouseApp/automation_send.html')

        if status == '1':

            file_list = []
            for file in models.FileAutomation.objects.all().filter(automation__automation_create_user__username=requests.user.username):

                usr = models.UserAutomation.objects.get(automation_input_id=file.file_automation_id)
                if usr.view_status == True:
                    file_list.append([usr, file])

            msg_list = []
            for msg in models.MessageAutomation.objects.all().filter(
                    automation__automation_create_user__username=requests.user.username):

                usr = models.UserAutomation.objects.get(automation_input_id= msg.message_id)
                if usr.view_status == True:
                    msg_list.append([usr, msg])

        elif status == '2':

            file_list = []
            for file in models.FileAutomation.objects.all().filter(
                    automation__automation_create_user__username=requests.user.username):

                usr = models.UserAutomation.objects.get(automation_input_id=file.file_automation_id)
                if usr.view_status == False :
                    file_list.append([usr, file])

            msg_list = []
            for msg in models.MessageAutomation.objects.all().filter(
                    automation__automation_create_user__username=requests.user.username):

                usr = models.UserAutomation.objects.get(automation_input_id=msg.message_id)
                if usr.view_status == False :
                    msg_list.append([usr, msg])
        else:

            file_list = []
            for file in models.FileAutomation.objects.all().filter(
                    automation__automation_create_user__username=requests.user.username):

                usr = models.UserAutomation.objects.get(automation_input_id=file.file_automation_id)
                file_list.append([usr, file])

            msg_list = []
            for msg in models.MessageAutomation.objects.all().filter(
                    automation__automation_create_user__username=requests.user.username):

                usr = models.UserAutomation.objects.get(automation_input_id=msg.message_id)
                msg_list.append([usr, msg])

        context = {

            'file_list': file_list,
            'msg_list': msg_list,
            'request': requests,

        }

        return HttpResponse(temp.render(context))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def automation_recv_list(requests, status):

    """
    show automation receive list
    """

    if requests.user.is_authenticated:

        temp = loader.get_template('WareHouseApp/automation_recv.html')

        if status == '1':

            file_automation_list = models.UserAutomation.objects.all().filter(automation_input_type='F').filter(
                user__username=requests.user.username
            ).filter(view_status=True)

            msg_automation_list = models.UserAutomation.objects.all().filter(automation_input_type='M').filter(
                user__username=requests.user.username
            ).filter(view_status=True)

        elif status == '2':

            file_automation_list = models.UserAutomation.objects.all().filter(automation_input_type='F').filter(
                user__username=requests.user.username
            ).filter(view_status=False)

            msg_automation_list = models.UserAutomation.objects.all().filter(automation_input_type='M').filter(
                user__username=requests.user.username
            ).filter(view_status=False)

        else:

            file_automation_list = models.UserAutomation.objects.all().filter(automation_input_type='F').filter(
                user__username=requests.user.username
            )

            msg_automation_list = models.UserAutomation.objects.all().filter(automation_input_type='M').filter(
                user__username=requests.user.username
            )

        file_list = []
        for usr in file_automation_list:

            # load file object
            file = models.FileAutomation.objects.get(file_automation_id=usr.automation_input_id)
            file_list.append([usr, file])

        msg_list = []
        for usr in msg_automation_list:

            # load file object
            msg = models.MessageAutomation.objects.get(message_id=usr.automation_input_id)
            msg_list.append([usr, msg])

        context = {

            'file_list': file_list,
            'msg_list': msg_list,
            'request': requests,

        }

        return HttpResponse(temp.render(context))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

