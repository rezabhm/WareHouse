from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse

from . import models
import time
from uuid import uuid1
import datetime

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

    return HttpResponse(main_template.render())


def main_url(request):

    """
    this is main & primary page
    """

    # load main.html for render
    main_template = loader.get_template('WareHouseApp/main.html')

    return HttpResponse(main_template.render())


def live_WeighBridge(request):

    """
    this is main & primary page
    """

    # load main.html for render
    main_template = loader.get_template('WareHouseApp/live_WeighBridge.html')

    return HttpResponse(main_template.render())


def monitor_data(request):

    """
    this is main & primary page
    """

    # load main.html for render
    main_template = loader.get_template('WareHouseApp/monitor_data.html')

    return HttpResponse(main_template.render())


def first_WeightLifting(request):

    """
    this is main & primary page
    """

    # load main.html for render
    main_template = loader.get_template('WareHouseApp/first_WeightLifting.html')

    return HttpResponse(main_template.render())


def user_url(request):

    """
    this is user page
    """

    # load main.html for render
    main_template = loader.get_template('WareHouseApp/user.html')


    context = {

        'user': request.user.username if request.user.is_authenticated else 'anonymouse'

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
            return HttpResponseRedirect(reverse("SignIn_Form", args=["نام كاربري يا رمز عبور اشتباه است "]))

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

            'error_text': error_text
        }

        return HttpResponse(change_password_form_page.render(context))

    else:
        # redirect to error page
        return HttpResponseRedirect(reverse('Error', args=['اجازه دسترسی ندارید']))


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

            # change pasword
            user_obj.set_password(password)
            user_obj.save()

            return HttpResponseRedirect(reverse('Main'))

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

            return HttpResponse(driver_temp.render())

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
            pro_obj_list = models.ProductOwner.objects.all().filter(name=product_owner_name).filter(
                last_name=product_owner_lastname
            )

            # check Create product owner object or select it
            if len(pro_obj_list) > 0:

                po_obj = pro_obj_list[0]

            else:

                po_obj = models.ProductOwner()
                po_obj.name = product_owner_name
                po_obj.last_name = product_owner_lastname
                po_obj.product_owner_id = str(uuid1().int)

                # save product owner object
                po_obj.save()

            # get car object list
            car_obj_list = models.Car.objects.all().filter(car_number=car_number)

            if len(car_obj_list) > 0:

                car_obj = car_obj_list[0]

            else:
                # create car object
                car_obj = models.Car()
                car_obj.car_number = car_number
                car_obj.car_id = str(uuid1().int)

            # set car object product owner relation
            car_obj.product_owner = po_obj

            # save car object
            car_obj.save()

            # get driver object list
            driver_obj_lis = models.Driver.objects.all().filter(name=driver_name).filter(last_name=driver_last_name).filter(
                phone_number=driver_phone_number
            )

            if len(driver_obj_lis) > 0:

                driver_obj = driver_obj_lis[0]

            else:

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
            lwb_obj.live_weighbridge_id = str(uuid1().int)
            lwb_obj.final_weight = car_weight
            lwb_obj.product_category = product_category
            lwb_obj.driver = driver_obj

            if len(lwb_user_list) > 0:
                lwb_obj.Live_Weighbridge_Manager = lwb_user_list[0]

            elif requests.user.is_superuser:
                lwb_obj.Live_Weighbridge_Manager = 'Admin'

            else:
                lwb_obj.Live_Weighbridge_Manager = 'CEO'

            # save live weighbridge
            lwb_obj.save()

            return HttpResponseRedirect(reverse('Main'))

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
                    weighting_date__gte=time.time()-(60*60*6)
                )

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
                lwb_obj.slaughter_start_date = time.time()

                # save changes
                lwb_obj.save()

                return HttpResponseRedirect(reverse('Main'))

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
                )

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
                lwb_obj.slaughter_finish_date = time.time()

                # save changes
                lwb_obj.save()

                return HttpResponseRedirect(reverse('Main'))

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

                'lwb_list': models.LiveWeighbridge.objects.all().filter(car_empty=False)
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

            # get liveWeighBridge list
            lwb_obj_list = models.LiveWeighbridge.objects.all().filter(live_weighbridge_id=lwb_id)

            if len(lwb_obj_list) > 0:

                # change object status to True and save current time
                lwb_obj = lwb_obj_list[0]

                # change information
                lwb_obj.car_empty = True

                # save changes
                lwb_obj.save()

                return HttpResponseRedirect(reverse('Main'))

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

                'lwb_list': models.LiveWeighbridge.objects.all().filter(slaughter_status=True)

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
            lwb_id = requests.POST['lwb_id']
            weight = requests.POST['weight']
            product_category = requests.POST['product_category']
            sales_category = requests.POST['sales_category']

            # create first_weightlifting objects
            fwl = models.FirstWeightLifting()
            fwl.weight = weight
            fwl.product_category = product_category
            fwl.sales_category = sales_category
            fwl.weight_lifting_id = str(uuid1().int)

            # get lwb list
            lwb_list = models.LiveWeighbridge.objects.all().filter(live_weighbridge_id=lwb_id)
            fwl.Live_Weigh_Bridge = lwb_list[0]

            if len(first_weightlifting_user_list) > 0:
                fwl.Weight_Lifting_Manager = first_weightlifting_user_list[0]

            # save objects
            fwl.save()

            return HttpResponseRedirect(reverse('Main'))

        else:

            # raised Error
            return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

    else:

        # raised Error
        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def pre_cdld_enter_form(requests):

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
                    weighting_time__gte=time.time() - (60*60*5)
                ).filter(choise_status=False)

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
            weight = requests.POST['weight']
            fwl_id = requests.POST['fwl_id']
            pc_id = int(requests.POST['pc_id'])
            pallet_id = requests.POST['pallet_id']
            product_category = requests.POST['product_category']

            # create pre-cold object
            pc = models.PreCold()

            # set param
            pc.weight = weight
            pc.product_category = product_category
            pc.pallet_id = pallet_id
            pc.pre_cold_id = pc_id

            # relation
            fwl_list = models.FirstWeightLifting.objects.all().filter(weight_lifting_id=fwl_id)
            pc.First_Weight_Lifting = fwl_list[0]
            fwl_obj = fwl_list[0]
            fwl_obj.choise_status = True
            fwl_obj.save()

            if len(first_pre_cold_user_list) > 0:
                pc.PreCold_Manager = first_pre_cold_user_list[0]

            # save
            pc.save()

            return HttpResponseRedirect(reverse('Main'))

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

                'pc_list': models.PreCold.objects.all().filter(product_pre_cold_status=True)

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

            # get object list
            pc_list = models.PreCold.objects.all().filter(pc_id=pc_id)

            if len(pc_list) > 0:

                # get object
                pc_obj = pc_list[0]

                # set param
                pc_obj.product_pre_cold_status = False
                pc_obj.exit_time = time.time()

                # save param
                pc_obj.save()

                return HttpResponseRedirect(reverse('Main'))

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

                "driver_list": models.Driver.objects.all(),
                "fwl_list": models.FirstWeightLifting.objects.all().filter(sales_category='D').filter(
                    weighting_time__gte=time.time() - (60*60*5)
                ).filter(choise_status=False),

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
            driver_id = requests.POST['driver_id']
            fwl_id = requests.POST['fwl_id']
            weight = requests.POST['weight']
            sale_price = requests.POST['sale_price']
            product_category = requests.POST['product_category']
            number_of_box = requests.POST['number_of_box']

            # create distribute object
            dist_obj = models.Distributed()

            # set param
            dist_obj.weight = weight
            dist_obj.sale_price = sale_price
            dist_obj.product_category = product_category
            dist_obj.number_of_box = number_of_box
            dist_obj.bill_of_lading = str(uuid1().int)

            # get driver list
            driver_list = models.Driver.objects.all().filter(driver_id=driver_id)

            dist_obj.driver = driver_list[0]

            # get firstWeightLifting object list
            fwl_list = models.FirstWeightLifting.objects.all().filter(weight_lifting_id=fwl_id)
            fwl_obj = fwl_list[0]
            fwl_obj.choise_status = True
            fwl_obj.save()

            dist_obj.first_weight_lifting = fwl_list[0]

            if len(dist_manager_list) > 0:
                dist_obj.sales_manager = dist_manager_list[0]

            # save model
            dist_obj.save()

            return HttpResponseRedirect(reverse('Main'))

        else:

            # raised Error
            return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

    else:

        # raised Error
        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def freeze_tunnel_enter_form(requests):

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
                    weighting_time__gte=time.time() - (60 * 60 *5)
                ).filter(choise_status=False)

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
        weight = float(requests.POST['weight'])
        tunnel_id = requests.POST['tunnel_id']
        pallet_id = requests.POST['pallet_id']
        prod_category = requests.POST['product_category']
        fwl_id = requests.POST['fwl_id']

        # create object
        ft_obj = models.FreezingTunnel()

        # set param
        ft_obj.weight = weight
        ft_obj.tunnel_id = tunnel_id
        ft_obj.pallet_id = pallet_id
        ft_obj.product_category = prod_category
        ft_obj.first_weight_lifting = models.FirstWeightLifting.objects.all().filter(weight_lifting_id=fwl_id)[0]
        ft_obj.freeze_tunnel_id = str(uuid1().int)

        fwl_obj = models.FirstWeightLifting.objects.all().filter(weight_lifting_id=fwl_id)[0]
        fwl_obj.choise_status = True
        fwl_obj.save()

        if len(freeze_tunnel_manager_list) > 0:

            ft_obj.freezing_tunnel_manager = freeze_tunnel_manager_list[0]

        # save object
        ft_obj.save()

        return HttpResponseRedirect(reverse('Main'))

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

                'ft_list': models.FreezingTunnel.objects.all().filter(status=True)

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

            # get model
            ft_obj = models.FreezingTunnel.objects.all().filter(freeze_tunnel_id=ft_id)[0]

            # set param
            ft_obj.exit_date = time.time()
            ft_obj.status = False

            # save
            ft_obj.save()

            return HttpResponseRedirect(reverse('Main'))

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

            return HttpResponse(paper_box_temp.render())

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
            weight = float(requests.POST['weight'])
            product_category = requests.POST['product_category']
            product_number = requests.POST['product_number']

            # create model
            paper_box_obj = models.PaperBox()

            # set param
            paper_box_obj.paper_box_weight = weight
            paper_box_obj.number_of_product = product_number
            paper_box_obj.product_category = product_category
            paper_box_obj.box_id = str(uuid1().int)

            # save model
            paper_box_obj.save()

            # load template to show paper_box_id
            paper_box_temp = loader.get_template('WareHouseApp/paper_box.html')

            context = {

                'id': paper_box_obj.box_id

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

                "paper_box_list": models.PaperBox.objects.all().filter(box_status=False)

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
            pallet_weight = requests.POST['pallet_weight_with_product']
            pallet_weight_empty = requests.POST['pallet_weight_with_product']
            number_of_box = requests.POST['number_of_box']
            cold_house_id = requests.POST['cold_house_id']
            pallet_id = requests.POST['pallet_id']

            # create cold_house obj
            cold_house_obj = models.ColdHouse()

            if len(coldHouse_manager) > 0:
                cold_house_obj.freezing_tunnel_manager = coldHouse_manager[0]

            # set param
            cold_house_obj.number_of_box = number_of_box
            cold_house_obj.total_pallet_weight = pallet_weight
            cold_house_obj.pallet_weight_without_product = pallet_weight_empty
            cold_house_obj.cold_house_id = cold_house_id
            cold_house_obj.pallet_id = pallet_id

            # save object
            cold_house_obj.save()

            for key in requests.POST.keys():

                if key not in ['pallet_weight_with_product', 'pallet_weight_without_product', 'number_of_box'
                               , 'cold_house_id', 'pallet_id']:

                    value = requests.POST[key]

                    paper_box_obj = models.PaperBox.objects.all().filter(box_id=value)[0]

                    paper_box_obj.cold_house = cold_house_obj
                    paper_box_obj.box_status = True

                    paper_box_obj.save()

            return HttpResponseRedirect(reverse("Main"))

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

                'cold_house_list': models.ColdHouse.objects.all().filter(pallet_status=True)

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
            pallet_id = requests.POST['pallet_id']

            print('pallet id = ',pallet_id)

            # get object
            cold_house_obj = models.ColdHouse.objects.all().filter(pallet_id=pallet_id)[0]

            # change param
            cold_house_obj.exit_time = time.time()
            cold_house_obj.pallet_status = False

            # save object
            cold_house_obj.save()

            return HttpResponseRedirect(reverse('Main'))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

    else:

        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def company_list(requests):

    """
    user can see company list
    """

    # load template
    company_list_temp = loader.get_template('WareHouseApp/company_list.html')

    context = {

        'company_list': models.Company.objects.all()

    }

    return HttpResponse(company_list_temp.render(context))


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

    }

    return HttpResponse(user_list_temp.render(context))


def company_live_weighbridge_list(requests, year=0, month=0, day=0, car_empty=0, product_category=0, slaughter_status=0):

    """
    show company live WeighBridge data with it filter
    """

    if requests.user.is_authenticated:

        ceo_list = models.CEO.objects.all().filter(username=requests.user.username)
        lwb_manager_list = models.LiveWeighbridgeManager.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or len(lwb_manager_list) > 0 or requests.user.is_superuser:

            # user have access to see data
            if year == '0' and month == '0' and day == '0':

                # get all of objects without time filter
                lwb_list = models.LiveWeighbridge.objects.all()

            else:

                # add time filter
                string = '{0}/{1}/{2}'.format(str(day), str(month), str(year))
                time_filter = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())
                lwb_list = models.LiveWeighbridge.objects.all().filter(weighting_date__gte=time_filter).filter(weighting_date__lte=time_filter + (60*60*24))

            if car_empty == '1':

                # add filter , if equal 1 it means return all of True car Empty
                lwb_list = lwb_list.filter(car_empty=True)

            elif car_empty == '2':

                # add filter , if equal 2 it means return all of False car Empty
                lwb_list = lwb_list.filter(car_empty=False)

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

            # load template
            lwb_temp = loader.get_template('WareHouseApp/live_WeighBridge_list.html')

            lwb_list_final = []
            for lwb in lwb_list:

                if lwb.product_category == 'C':
                    prod = 'chicken'

                elif lwb.product_category == 'T':
                    prod = 'turkey'

                elif lwb.product_category == 'Q':
                    prod = 'quail'

                else:
                    prod = 'Nothing'

                lwb_list_final.append([time.ctime(lwb.weighting_date), lwb.car_weight,
                        lwb.final_weight, lwb.car_empty, lwb.buy_price, lwb.slaughter_status,
                        lwb.slaughter_start_date, lwb.slaughter_finish_date, prod,
                        lwb.driver.name + ' ' + lwb.driver.last_name, lwb.driver.car.car_number,
                        lwb.driver.car.product_owner.name + ' '+lwb.driver.car.product_owner.last_name])

            context = {

                "lwb_list": lwb_list_final

            }

            return HttpResponse(lwb_temp.render(context))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def driver_list(requests, phone_number='0', product_category='0', model_type='0', year='0', month='0', day='0'):

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

                dist_list = models.Distributed.objects.all()
                lwb_list = models.LiveWeighbridge.objects.all()

            elif model_type == '1':

                dist_list = models.Distributed.objects.all()
                lwb_list = models.LiveWeighbridge.objects.all().filter(car_weight= -5248.0)

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

                lwb_list = lwb_list.filter(weighting_date__gte=time_filter).filter(weighting_date__lte=time_filter + (60*60*24))
                dist_list = dist_list.filter(date__gte=time_filter).filter(date__lte=time_filter + (60*60*24))

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

                dist_list = dist_list.filter(product_category='C')
                lwb_list = lwb_list.filter(product_category='C')

            elif product_category == '2':

                dist_list = dist_list.filter(product_category='T')
                lwb_list = lwb_list.filter(product_category='T')

            elif product_category == '3':

                dist_list = dist_list.filter(product_category='Q')
                lwb_list = lwb_list.filter(product_category='Q')

            # load driver_list template
            driver_temp = loader.get_template('WareHouseApp/driver_list.html')

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

                dist_final_list.append([

                    dist.driver.name, dist.driver.last_name, dist.driver.phone_number,
                    dist.driver.car.car_number,
                    dist.driver.car.product_owner.name, dist.driver.car.product_owner.last_name,
                    dist.weight, time.ctime(dist.date), dist.sale_price, prod_category,
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
                    lwb.final_weight, lwb.car_weight, lwb.car_empty, time.ctime(lwb.weighting_date),
                    prod_category, lwb.slaughter_status, lwb.slaughter_start_date, lwb.slaughter_finish_date,
                    lwb.buy_price

                ])

            # return data
            context = {

                'dist_list': dist_final_list,
                'lwb_list': lwb_final_list

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

                dist_final_list.append([

                    dist.driver.name, dist.driver.last_name, dist.driver.phone_number,
                    dist.driver.car.car_number,
                    dist.driver.car.product_owner.name, dist.driver.car.product_owner.last_name,
                    dist.weight, time.ctime(dist.date), dist.sale_price, prod_category,
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
                    lwb.final_weight, lwb.car_weight, lwb.car_empty, time.ctime(lwb.weighting_date),
                    prod_category, lwb.slaughter_status, lwb.slaughter_start_date, lwb.slaughter_finish_date,
                    lwb.buy_price

                ])

            # return data
            context = {

                'dist_list': dist_final_list,
                'lwb_list': lwb_final_list

            }

            return HttpResponse(car_temp.render(context))

    # user can't access to this page
    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def product_owner_list(requests, po_name='0', po_lastname='0', product_category='0', model_type='0', year='0', month='0', day='0'):

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

                dist_final_list.append([

                    dist.driver.name, dist.driver.last_name, dist.driver.phone_number,
                    dist.driver.car.car_number,
                    dist.driver.car.product_owner.name, dist.driver.car.product_owner.last_name,
                    dist.weight, time.ctime(dist.date), dist.sale_price, prod_category,
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
                    lwb.final_weight, lwb.car_weight, lwb.car_empty, time.ctime(lwb.weighting_date),
                    prod_category, lwb.slaughter_status, lwb.slaughter_start_date, lwb.slaughter_finish_date,
                    lwb.buy_price

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
                    time.ctime(pd.First_Weight_Lifting.weighting_time),
                    pd.First_Weight_Lifting.weight,
                    'pre-cold',
                    pd.pre_cold_id,
                    pd.pallet_id,
                    pd.product_pre_cold_status,
                    prod_category,
                    pd.weight,
                    time.ctime(pd.entry_time),
                    '-' if pd.product_pre_cold_status else time.ctime(pd.exit_time),

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
                    time.ctime(ft.first_weight_lifting.weighting_time),
                    ft.first_weight_lifting.weight,
                    'freeze tunnel',
                    time.ctime(ft.entry_date),
                    '-' if ft.status else time.ctime(ft.exit_date),
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
                'pd_list': pd_final_list

            }

            return HttpResponse(po_temp.render(context))

    # user can't access to this page
    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def weight_lifting_list(requests, product_category='0', model_type='0', year='0', month='0', day='0', exist='0'):

    """
    show list of first weightlifting with filter
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
                pd_list = models.PreCold.objects.all()
                ft_list = models.FreezingTunnel.objects.all()

            elif model_type == '1':

                dist_list = models.Distributed.objects.all()
                pd_list = models.PreCold.objects.all().filter(weight=-5)
                ft_list = models.FreezingTunnel.objects.all().filter(weight=-5)

            elif model_type == '2':

                dist_list = models.Distributed.objects.all().filter(weight=-5248.0)
                pd_list = models.PreCold.objects.all().filter(weight=-5)
                ft_list = models.FreezingTunnel.objects.all().filter(weight=-5)

            elif model_type == '3':

                dist_list = models.Distributed.objects.all().filter(weight=-5248.0)
                pd_list = models.PreCold.objects.all()
                ft_list = models.FreezingTunnel.objects.all().filter(weight=-5)

            elif model_type == '4':

                dist_list = models.Distributed.objects.all().filter(weight=-5248.0)
                pd_list = models.PreCold.objects.all().filter(weight=-5)
                ft_list = models.FreezingTunnel.objects.all()

            else:

                dist_list = models.Distributed.objects.all().filter(weight=-5248.0)
                pd_list = models.PreCold.objects.all().filter(weight=-5)
                ft_list = models.FreezingTunnel.objects.all().filter(weight=-5)

            # we must add time filter . this filter help to see special time's objects
            # if all of them equal 0 we didn't add time filter
            # else we must add month and day and year filter
            if year != '0' and month != '0' and day != '0':
                # add time filter
                string = '{0}/{1}/{2}'.format(str(day), str(month), str(year))
                time_filter = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())


                dist_list = dist_list.filter(date__gte=time_filter).filter(date__lte=time_filter + (60 * 60 * 24))

                pd_list = pd_list.filter(entry_time__gte=time_filter).filter(
                    entry_time__lte=time_filter + (60 * 60 * 24))

                ft_list = ft_list.filter(entry_date__gte=time_filter).filter(
                    entry_date__lte=time_filter + (60 * 60 * 24))

            # check product exist in freeze tunnel and pre-cold or not
            # if equal 1 it will check all of exist
            # if equal 2 it will check didn't exist
            # else didn't apply filter
            if exist == '1':

                pd_list = pd_list.filter(product_pre_cold_status=True)
                ft_list = ft_list.filter(status=True)

            elif exist == '2':

                pd_list = pd_list.filter(product_pre_cold_status=False)
                ft_list = ft_list.filter(status=False)

            # we must add product category filter to return special product
            # if equal 1 we return only chicken objects
            # if equal 2 we return only turkey objects
            # if equal 3 we return only quail objects
            # else we didn't add filter
            if product_category == '1':

                dist_list = dist_list.filter(product_category='C')
                pd_list = pd_list.filter(product_category='C')
                ft_list = ft_list.filter(product_category='C')

            elif product_category == '2':

                dist_list = dist_list.filter(product_category='T')
                pd_list = pd_list.filter(product_category='T')
                ft_list = ft_list.filter(product_category='T')

            elif product_category == '3':

                dist_list = dist_list.filter(product_category='Q')
                pd_list = pd_list.filter(product_category='Q')
                ft_list = ft_list.filter(product_category='Q')

            # load product_owner template
            po_temp = loader.get_template('WareHouseApp/weight_lifting_list.html')

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

                dist_final_list.append([

                    dist.driver.name, dist.driver.last_name, dist.driver.phone_number,
                    dist.driver.car.car_number,
                    dist.driver.car.product_owner.name, dist.driver.car.product_owner.last_name,
                    dist.weight, time.ctime(dist.date), dist.sale_price, prod_category,
                    dist.bill_of_lading, dist.number_of_box

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
                    time.ctime(pd.First_Weight_Lifting.weighting_time),
                    pd.First_Weight_Lifting.weight,
                    'pre-cold',
                    pd.pre_cold_id,
                    pd.pallet_id,
                    pd.product_pre_cold_status,
                    prod_category,
                    pd.weight,
                    time.ctime(pd.entry_time),
                    '-' if pd.product_pre_cold_status else time.ctime(pd.exit_time),

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
                    time.ctime(ft.first_weight_lifting.weighting_time),
                    ft.first_weight_lifting.weight,
                    'freeze tunnel',
                    time.ctime(ft.entry_date),
                    '-' if ft.status else time.ctime(ft.exit_date),
                    ft.weight,
                    ft.tunnel_id,
                    ft.pallet_id,
                    prod_category,

                ])

            # return data
            context = {

                'dist_list': dist_final_list,
                'ft_list': ft_final_list,
                'pd_list': pd_final_list

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

                    time.ctime(ch.entry_date),
                    '-' if ch.pallet_status else time.ctime(ch.exit_date),
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

                if pb.product_category == 'C':
                    prod_category = 'Chicken'

                elif pb.product_category == 'T':
                    prod_category = 'turkey'

                elif pb.product_category == 'Q':
                    prod_category = 'Quail'

                pb_final_list.append([

                    prod_category,
                    pb.paper_box_weight,
                    pb.box_status,
                    pb.number_of_product,
                    time.ctime(pb.packing_time),
                    pb.box_id,
                    pb.cold_house.pallet_id,
                    pb.cold_house.cold_house_id

                ])

            # return data
            context = {

                'pb_list': pb_final_list,
                'ch_list':ch_final_list

            }

            return HttpResponse(ch_temp.render(context))

    # user can't access to this page
    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))
