from django.urls import re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

My_app = 'DeviceMaintenance'

urlpatterns = [

    # task structure
    re_path(r'^structure/create/form/$', views.task_structure_create_form, name='Task_Structure_Create_Form'),
    re_path(r'^structure/create/$', views.task_structure_create, name='Task_Structure_Create'),
    re_path(r'^sub/structure/create/form/$', views.sub_structure_create_form, name='Sub_Structure_Create_Form'),
    re_path(r'^sub/structure/create/$', views.sub_structure_create, name='Sub_Structure_Create'),
    re_path(r'^structure/list/$', views.task_structure_list, name='Task_Structure_List'),

    # task
    re_path(r'^create/form/$', views.task_create_form, name='Task_Create_Form'),
    re_path(r'^create/$', views.task_create, name='Task_Create'),

    re_path(r'^list/(?P<task_status>[\d]{1})/(?P<time_status>[\d]{1})/(?P<start_year>[\d]{4})/(?P<start_month>[\d]{2})/(?P<start_day>[\d]{2})/(?P<deadline_year>[\d]{4})/(?P<deadline_month>[\d]{2})/(?P<deadline_day>[\d]{2})/$',
            views.task_list, name='Task_List'),

    re_path(r'^done/form/$', views.task_done_form, name='Task_Done_Form'),
    re_path(r'^done/$', views.task_done, name='Task_Done'),

    re_path(r'filter/', views.task_filter, name='Filter'),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
