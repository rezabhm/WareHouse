from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse

from . import models
import time

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


@csrf_exempt
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


def user_profile(request, ussername):

    user_profile_page = loader.get_template('WareHouseApp/user_profile.html')

    context = {
        "user": request.user
    }

    if request.user.is_authenticate:

        return HttpResponse(user_profile_page.render(context))

    else:

        return HttpResponseRedirect(reverse('sign_in'))


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
            pro_obj_list = models.ProductOwner.objects.all().filter(name=product_owner_name).fliter(
                last_name=product_owner_lastname
            )

            # check Create product owner object or select it
            if len(pro_obj_list) > 0:

                po_obj = pro_obj_list[0]

            else:

                po_obj = models.ProductOwner()
                po_obj.name = product_owner_name
                po_obj.last_name = product_owner_lastname

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

    if requests.user.is_authenticate:

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

    if requests.user.is_authenticate:

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

    if requests.user.is_authenticate:

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

    if requests.user.is_authenticate:

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

    if requests.user.is_authenticate:

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

    if requests.user.is_authenticate:

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

    if requests.user.is_authenticate:

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

    if requests.user.is_authenticate:

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

            # get lwb list
            lwb_list = models.LiveWeighbridge.objects.all().filter(live_weighbridge_id=lwb_id)
            fwl.Live_Weigh_Bridge = lwb_list[0]

            if len(first_weightlifting_user_list) > 0:
                fwl.Weight_Lifting_Manager = first_weightlifting_user_list[0]

            elif requests.user.is_superuser:
                fwl.Weight_Lifting_Manager = 'Admin'

            else:
                fwl.Weight_Lifting_Manager = 'CEO'

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

    if requests.user.is_authenticate:

        # get user's list
        first_pre_cold_user_list = models.PreColdManager.objects.all().filter(
            username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_user_list) > 0 or len(first_pre_cold_user_list) > 0 or requests.user.is_superuser:

            # render form
            pre_cold_temp = loader.get_template('WareHouseApp/pre_cold_enter_form.html')

            context = {

                "fwl_list": models.FirstWeightLifting.objects.all().filter(salse_category='P').filter(
                    weighting_time__gte=time.time() - (60*60*5)
                )

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

    if requests.user.is_authenticate:

        # get user's list
        first_pre_cold_user_list = models.PreColdManager.objects.all().filter(
            username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_user_list) > 0 or len(first_pre_cold_user_list) > 0 or requests.user.is_superuser:

            # get data
            weight = requests.POST['weight']
            fwl_id = requests.POST['fwl_id']
            pc_id = requests.POST['pc_id']
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

            if len(first_pre_cold_user_list) > 0:
                pc.PreCold_Manager = first_pre_cold_user_list[0]

            elif requests.user.is_superuser:
                pc.PreCold_Manager = "Admin"

            else:
                pc.PreCold_Manager = 'CEO'

            # save
            pc.save()

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

    if requests.user.is_authenticate:

        # get user's list
        first_pre_cold_user_list = models.PreColdManager.objects.all().filter(
            username=requests.user.username)
        ceo_user_list = models.CEO.objects.all().filter(username=requests.user.username)

        if len(ceo_user_list) > 0 or len(first_pre_cold_user_list) > 0 or requests.user.is_superuser:

            # load template
            exit_temp = loader.get_template('WareHouseApp/pre_cold_exit_form.html')

            context = {

                'pc_list': models.PreCold.objcets.all().filter(product_pre_cold_status=True)

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

    if requests.user.is_authenticate:

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

            else:

                # raised error
                return HttpResponseRedirect(reverse('Error', args=['you entry pre-cold id is incorrect']))

        else:

            # raised error
            return HttpResponseRedirect(reverse('Error', args=["you cant access to this page"]))

    else:
        # raised error
        return HttpResponseRedirect(reverse('Error', args=["you cant access to this page"]))
