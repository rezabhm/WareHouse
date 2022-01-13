from django.db import models
from uuid import uuid1
from django.contrib.auth.models import User

# Create your models here.
"""
in here we will define device maintenance models for store maintenance task.

models:
    
    1) TaskStructure
    2) SubTaskStructure
    3) Task
    4) SubTask
    5) TaskUser
    
"""


class TaskStructure(models.Model):

    """
    with this model we will define structure of our task.

    table's column name :

        1) id           ==> for every task structure we must have id to identify task
        2) title        ==> title for show task subject
        3) description  ==> a little description about current task and explain how do task
        4) cycle time   ==> define cycle time for show task time

    """

    # task structure id
    task_structure_id = models.CharField(default=str(uuid1().int), max_length=100)

    # title
    title = models.CharField(max_length=50)

    # description
    description = models.TextField()

    # cycle time description
    cycle_time = models.TextField()

    def __str__(self):
        return self.title


class SubTaskStructure(models.Model):

    """
    define sub-task for every task that user must do this task and change its status

    table's column name :

        1) title                    ==> show sub-task subject
        2) description              ==> sub-task description that explain task
        3) task_structure           ==> foreign key relation to task_structure
        4) sub_task_structure_id    ==> id for identify sub-task

    """

    # title
    title = models.CharField(max_length=25)

    # description
    description = models.TextField()

    # id
    sub_task_structure_id = models.CharField(default=str(uuid1().int), max_length=250)

    # relation to TaskStructure models
    task_structure = models.ForeignKey(TaskStructure, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Task(models.Model):

    """
    this table store all task that completely done

    table's column name:

        1) start_task_time  ==> this arg task time that user must do it
        2) deadline         ==> user must do this task before deadline
        3) task_structure   ==> foreign key relation with TaskStructure
        4) task_id          ==> id for identify task

    """

    # start task time
    start_task_time = models.FloatField()

    # task deadline
    deadline = models.FloatField()

    # id
    task_id = models.CharField(default=str(uuid1().int), max_length=250)

    # relation
    task_structure = models.ForeignKey(TaskStructure, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_structure.title


class SubTask(models.Model):

    """
    in this task we will determine task ha done or not

    table's column name:

        1) task_status          ==> determine task has done or not
        2) sub_task_id          ==> id for identify sub-task
        3) sub_task_structure   ==> foreign key with SubTaskStructure
        4) trouble_description  ==> if task have trouble with this arg user can explain it

    """

    # task status
    task_status_tuple = (

        ('D', 'Task Done'),
        ('T', 'Trouble'),
        ('I', 'Ignore task')

    )
    task_status = models.CharField(choices=task_status_tuple, max_length=1, default='I')

    # id
    sub_task_id = models.CharField(default=str(uuid1().int), max_length=250)

    # trouble description
    trouble_description = models.TextField(default='Nothing')

    # sub task structure
    sub_task_structure = models.ForeignKey(SubTaskStructure, on_delete=models.CASCADE)

    # task relation
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.task.title


class TaskUser(models.Model):

    """
    with this class we will create new user that can access to above model

    table's column name:

        1) username         ==> user's username
        2) name             ==> user's name
        3) last_name        ==> user's last_name
        4) phone_number     ==> user's phone_number
        5) user             ==> relation with django user model
        6) task_structure   ==> relation with TaskStructure to create access

    """

    # username
    username = models.CharField(max_length=50)

    # name
    name = models.CharField(max_length=50)

    # lastname
    last_name = models.CharField(max_length=50)

    # phone number
    phone_number = models.CharField(max_length=50)

    # user relation
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # task structure relation
    task_structure = models.ManyToManyField(TaskStructure)

    def __str__(self):
        return self.username
