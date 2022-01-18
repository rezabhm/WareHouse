from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from . import models as dm_models
from WareHouseApp import models as wh_models
from django.template import loader, Context
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
import time
import datetime
from uuid import uuid1

# Create your views here.

def main(request):

    """
    this is main & primary page
    """

    # load main.html for render
    main_template = loader.get_template('DeviceMaintenance/main.html')

    return HttpResponse(main_template.render())


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
            task_structure_obj.task_structure_id = str(uuid1().int)

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
            sub_structure_obj.sub_task_structure_id = str(uuid1().int)

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


def task_create_form(requests):

    """
    create task
    """

    if requests.user.is_authenticated:

        ceo_list = wh_models.CEO.objects.all().filter(username=requests.user.username)
        task_user_list = dm_models.TaskUser.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or len(task_user_list) > 0 or requests.user.is_superuser:

            # load template
            task_create_temp = loader.get_template('DeviceMaintenance/task_create_form.html')

            context = {

                'task_structure_list': dm_models.TaskStructure.objects.all()

            }

            return HttpResponse(task_create_temp.render(context))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def task_create(requests):

    """
    create task
    """

    if requests.user.is_authenticated:

        ceo_list = wh_models.CEO.objects.all().filter(username=requests.user.username)
        task_user_list = dm_models.TaskUser.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or len(task_user_list) > 0 or requests.user.is_superuser:

            # get param

            start_time_year = requests.POST['start_time_year']
            start_time_month = requests.POST['start_time_month']
            start_time_day = requests.POST['start_time_day']
            deadline_year = requests.POST['deadline_year']
            deadline_month = requests.POST['deadline_month']
            deadline_day = requests.POST['deadline_day']
            task_id = requests.POST['task_id']

            # create start time and deadline time
            string = '{0}/{1}/{2}'.format(str(start_time_day), str(start_time_month), str(start_time_year))
            start_time = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())

            string = '{0}/{1}/{2}'.format(str(deadline_day), str(deadline_month), str(deadline_year))
            deadline_time = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())

            # create task
            task_obj = dm_models.Task()

            # set param
            task_obj.start_task_time = start_time
            task_obj.deadline = deadline_time
            task_obj.task_id = str(uuid1().int)

            task_structure_obj_list = dm_models.TaskStructure.objects.all().filter(task_structure_id=task_id)

            if len(task_structure_obj_list) > 0:
                task_obj.task_structure = task_structure_obj_list[0]

            else:
                return HttpResponseRedirect(reverse('Error', args=["your task selection is wrong"]))

            # save task obj
            task_obj.save()

            # create sub-task
            sub_structure_obj_list = dm_models.SubTaskStructure.objects.all().filter(task_structure__task_structure_id=task_id)

            for sub_task in sub_structure_obj_list:

                # create sub-task
                sub_task_obj = dm_models.SubTask()

                # set param
                sub_task_obj.task = task_obj
                sub_task_obj.sub_task_structure = sub_task
                sub_task_obj.sub_task_id = str(uuid1().int)

                sub_task_obj.save()

            return HttpResponseRedirect(reverse('Main'))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def task_list(requests, task_status='0', time_status='0', start_year='0000', start_month='00', start_day='00',
              deadline_year='0000', deadline_month='00', deadline_day='00'):

    """
    show all tasks list
    """

    if requests.user.is_authenticated:

        ceo_list = wh_models.CEO.objects.all().filter(username=requests.user.username)
        task_user_list = dm_models.TaskUser.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or len(task_user_list) > 0 or requests.user.is_superuser:

            # user have access
            # we must get object list and add filter

            # here we check task status that determine what kind of task we must return
            # if equal 1 we must get Done of sub-task
            # if equal 2 we must get Trouble sub-task
            # if equal 3 we must get Ignore sub-task
            # else we must get all of sub-task
            if task_status == '1':

                sub_task_obj_list = dm_models.SubTask.objects.all().filter(task_status='D')

            elif task_status == '2':

                sub_task_obj_list = dm_models.SubTask.objects.all().filter(task_status='T')

            elif task_status == '3':

                sub_task_obj_list = dm_models.SubTask.objects.all().filter(task_status='I')

            else:

                sub_task_obj_list = dm_models.SubTask.objects.all()

            # here we have 3 type of time_status
            # if equal 1 we must return all sub-tasks that current time are before the start time
            # if equal 2 we must return all sub-tasks that current time are between start time and deadline
            # if equal 3 we must return all sub-tasks that deadline time are before current time
            # else we must check if we have time filter we must add filter however we don't have
            # we can't add filter
            if time_status == '1':

                sub_task_obj_list = sub_task_obj_list.filter(task__start_task_time__gte=time.time())

            elif time_status == '2':

                sub_task_obj_list = sub_task_obj_list.filter(task__start_task_time__lte=time.time()).filter(
                    task__deadline__gte=time.time()
                )

            elif time_status == '3':

                sub_task_obj_list = sub_task_obj_list.filter(task__deadline__lte=time.time())

            else:

                if start_year != '0000' and start_month != '00' and start_day != '00' and deadline_year != '0000' and deadline_month != '00' and deadline_day != '00':

                    # we can add time filter
                    # create start time and deadline time
                    string = '{0}/{1}/{2}'.format(str(start_day), str(start_month), str(start_year))
                    start_time = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())

                    string = '{0}/{1}/{2}'.format(str(deadline_day), str(deadline_month), str(deadline_year))
                    deadline_time = time.mktime(datetime.datetime.strptime(string, "%d/%m/%Y").timetuple())

                    sub_task_obj_list = sub_task_obj_list.filter(task__start_task_time__lte=start_time).filter(
                        task__start_task_time_gte=deadline_time
                    )

            # create final data list
            final_list = []
            task_obj_list = dm_models.Task.objects.all()
            for task_obj in task_obj_list:

                sub_task = sub_task_obj_list.filter(task__task_id=task_obj.task_id)
                final_list.append([task_obj, time.ctime(task_obj.start_task_time), time.ctime(task_obj.deadline),
                                   sub_task])

            # load template
            task_temp = loader.get_template('DeviceMaintenance/sub_task_list.html')

            context = {

                'data_list': final_list

            }

            return HttpResponse(task_temp.render(context))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


def task_done_form(requests):

    """
    render task list
    """

    if requests.user.is_authenticated:

        ceo_list = wh_models.CEO.objects.all().filter(username=requests.user.username)
        user_list = dm_models.TaskUser.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or len(user_list) > 0 or requests.user.is_superuser:

            task_done_temp = loader.get_template('DeviceMaintenance/task_done.html')

            # add filter
            # return only tasks that current time are between start task time and deadline time
            data_list = []
            task_list_objs = dm_models.Task.objects.all().filter(start_task_time__lte=time.time()).filter(
                deadline__gte=time.time()
            )

            for task in task_list_objs:

                sub_task_objs = dm_models.SubTask.objects.all().filter(task__task_id=task.task_id)

                data_list.append([task, time.ctime(task.start_task_time), time.ctime(task.deadline), sub_task_objs])

            context = {

                'data_list': data_list

            }

            return HttpResponse(task_done_temp.render(context))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def task_done(requests):

    """
    change task status
    """

    if requests.user.is_authenticated:

        ceo_list = wh_models.CEO.objects.all().filter(username=requests.user.username)
        user_list = dm_models.TaskUser.objects.all().filter(username=requests.user.username)

        if len(ceo_list) > 0 or len(user_list) > 0 or requests.user.is_superuser:

            for key in requests.POST.keys():

                if key[:2] == 'ts':

                    sub_id = key[2:]
                    sub_task_object = dm_models.SubTask.objects.all().filter(sub_task_id=sub_id)[0]

                    sub_task_object.task_status = requests.POST[key]
                    sub_task_object.trouble_description = requests.POST['des'+sub_id]

                    sub_task_object.save()

            return HttpResponseRedirect(reverse('Main'))

    return HttpResponseRedirect(reverse('Error', args=["you can't access to this page"]))


@csrf_exempt
def filter(requests):

    """
    do filter for another views
    """

    return HttpResponseRedirect(reverse('Task_List', args=[

        requests.POST['task_status'],
        requests.POST['time_status'],
        requests.POST['start_year'],
        requests.POST['start_month'],
        requests.POST['start_day'],
        requests.POST['deadline_year'],
        requests.POST['deadline_month'],
        requests.POST['deadline_day'],

    ]))
