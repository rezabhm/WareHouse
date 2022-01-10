from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . import models as dm_models
from WareHouse.WareHouseApp import models as wh_models
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse

# Create your views here.


def task_structure_create_form(requests):

    """
    render create task structure form
    """

    if requests.user.is_authenticated:

        # get user_list
        ceo_list = wh_models.CEO.objects.all().filter(username=requests.user.username)
        task_user_list = dm_models.TaskUser.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or len(task_user_list) > 0 or requests.user.is_superuser:

            # user have access
            task_structure_temp = loader.get_template('DeviceMaintenance/task_structure.html')

            return HttpResponse(task_structure_temp.render())

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def task_structure_create(requests):

    """
    create task structure
    """

    if requests.user.is_authenticated:

        # get user_list
        ceo_list = wh_models.CEO.objects.all().filter(username=requests.user.username)
        task_user_list = dm_models.TaskUser.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or len(task_user_list) > 0 or requests.user.is_superuser:

            # get data
            title = requests.POST['title']
            description = requests.POST['description']
            cycle_time = requests.POST['cycle_time']

            # create task structure objects
            task_structure_obj = dm_models.TaskStructure()

            # set param
            task_structure_obj.title = title
            task_structure_obj.description = description
            task_structure_obj.cycle_time = cycle_time

            # save
            task_structure_obj.save()

            return HttpResponseRedirect(reverse('Main'))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def sub_structure_create_form(requests):
    """
    render create sub structure form
    """

    if requests.user.is_authenticated:

        # get user_list
        ceo_list = wh_models.CEO.objects.all().filter(username=requests.user.username)
        task_user_list = dm_models.TaskUser.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or len(task_user_list) > 0 or requests.user.is_superuser:

            # user have access
            sub_structure_temp = loader.get_template('DeviceMaintenance/sub_structure.html')

            context = {

                "task_structure_list": dm_models.TaskStructure.objects.all()

            }

            return HttpResponse(sub_structure_temp.render(context))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def sub_structure_create(requests):

    """
    create sub structure
    """

    if requests.user.is_authenticated:

        # get user_list
        ceo_list = wh_models.CEO.objects.all().filter(username=requests.user.username)
        task_user_list = dm_models.TaskUser.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or len(task_user_list) > 0 or requests.user.is_superuser:

            # get data
            title = requests.POST['title']
            description = requests.POST['description']
            task_id = requests.POST['task_id']

            # create task structure objects
            sub_structure_obj = dm_models.SubTaskStructure()

            # set param
            sub_structure_obj.title = title
            sub_structure_obj.description = description

            # get task structure list
            task_structure_object_list = dm_models.TaskStructure.objects.all().filter(task_structure_id=task_id)

            if len(task_structure_object_list) > 0:
                sub_structure_obj.task_structure = task_structure_object_list[0]

            # save
            sub_structure_obj.save()

            return HttpResponseRedirect(reverse('Main'))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def task_structure_list(requests):

    """
    task structure list
    """

    if requests.user.is_authenticated:

        ceo_list = wh_models.CEO.objects.all().filter(username=requests.user.username)
        task_user_list = dm_models.TaskUser.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or len(task_user_list) > 0 or requests.user.is_superuser:

            # load template
            task_list = loader.get_template('DeviceMaintenance/task_list.html')

            task_structure_objects_list = dm_models.TaskStructure.objects.all()
            final_list = []

            for ts in task_structure_objects_list:

                sub_structure_object_list = dm_models.SubTaskStructure.objects.all().filter(
                    task_structure__task_structure_id=ts.task_structure_id)

                final_list.append([ts, sub_structure_object_list])

            context = {

                'data_list': final_list

            }

            return HttpResponse(task_list.render(context))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))

