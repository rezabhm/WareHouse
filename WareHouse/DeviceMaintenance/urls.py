from django.urls import re_path
from . import views

My_app = 'DeviceMaintenance'

urlpatterns = [

    # task structure
    re_path(r'^task/structure/create/form/$', views.task_structure_create_form, name='Task_Structure_Create_Form'),
    re_path(r'^task/structure/create/$', views.task_structure_create, name='Task_Structure_Create'),
    re_path(r'^task/sub/structure/create/form/$', views.sub_structure_create_form, name='Sub_Structure_Create_Form'),
    re_path(r'^task/sub/structure/create/$', views.sub_structure_create, name='Sub_Structure_Create'),
    re_path(r'^task/structure/list/$', views.task_structure_list, name='Task_Structure_List'),

    # task
    re_path(r'^task/create/form/$', views.task_create_form, name='Task_Create_Form'),
    re_path(r'^task/create/$', views.task_create, name='Task_Create'),
    re_path(r'^task/list/$', views.task_list, name='Task_List'),

]
