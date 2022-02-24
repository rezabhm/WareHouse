from django.urls import re_path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

My_app = 'WareHouseApp'


"""
this file include warehouse urls .

main's url:
    
    1. main page url
    2. contact us url
    3. about us url
    4. error page url
    
User's url :
    
    1.  sign-up form url for register all kind of user
    2.  sign-up url for register
    3.  sign-in form url
    4.  sign-in url
    5.  logout url 
    6.  user profile url
    7.  change password form
    8.  change password

live weighbridge :

    1.  create or select driver form
    2.  create or select car
    3.  create or select product owner
    4.  live weighbridge form
    5.  create live weighbridge
    6.  start slaughter form for select object
    7.  start slaughter
    8.  finish slaughter form for select object
    9.  finish slaughter
    10. change car capability to empty form
    11. change car capability to empty 

first weighbridge :
    
    1.  first weight lifting form
    2.  first weight lifting
    3.  pre-cold enter form
    4.  pre-cold enter
    5.  pre-cold exit form
    6.  pre-cold exit
    7.  distribute form
    8.  distribute
    9.  freezing tunnel enter form
    10. freezing tunnel enter
    11. freezing tunnel exit form
    12. freezing tunnel exit

coldHouse :
    
    1. create paperBox form
    2. create paperBox
    3. coldHouse enter form
    4. coldHouse enter
    5. coldHouse exit form
    6. coldHouse exit

visualize data:

    1.  see company list
    2.  see all of company user's
    3.  see all of company live weighbridge (it's filter)
    7.  see all of company weight lifting with it's type filter
    8.  see all of driver weight lifting
    9.  see all of car weight lifting
    10. see all of product owner weight lifting
    11. see pre-cold with (pre-cold_id and product_category and pallet_id and product_pre_cold_status)
    12. see pre-cold with entry time filter and above filter
    13. see pre-cold with exit time filter and above filter
    14. see freezing tunnel with (status and product_type and pallet_id and tunnel_id ) filter
    15. see freezing tunnel with entry time and above filter
    16. see freezing tunnel with exit time and above filter
    17. see cold-house with (status and product category and pallet id and coldHouse id) filter
    18. see cold-house with entry
    19. see cold-house with exit time and above filter
    20. see all of paperBox with (product_type and status and product_owner and )
    21. see all of paperBox with packing time
    22. delete live weighbridge and first_weight_lifting and pre-cold and freezing tunnel and coldHouse and distribute
    23. delete driver and car and product_owner
    24. delete user

"""

urlpatterns = [

    # static page url
    re_path(r'^$', views.main, name='Main'),
    re_path(r'^main/$', views.main_url, name='Main_URL'),
    re_path(r'^about_us/$', views.about, name='About'),
    re_path(r'^contact_us/$', views.contact, name='Contact'),
    re_path(r'^User_url/$', views.user_url, name='User_url'),
    re_path(r'^live_WeighBridge/$', views.live_weighbridge_main, name='live_WeighBridge'),
    re_path(r'^first_WeightLifting/$', views.first_weightlifting_main, name='first_WeightLifting'),
    re_path(r'^monitor_data/$', views.monitor_data, name='monitor_data'),
    re_path(r'^task/$', views.task, name='task'),
    re_path(r'^automation/$', views.automation, name='automation'),
    re_path(r'^error/(?P<error_text>.*)', views.error, name='Error'),

    # user url
    re_path(r'^sign_up/form/$', views.signup_form, name='SignUp_Form'),
    re_path(r'^sign_up/$', views.signup, name='SignUp'),
    re_path(r'^sign_in/form/$', views.sign_in_form, name='SignIn_Form'),
    re_path(r'^sign_in/$', views.sign_in, name='SignIn'),
    re_path(r'^change_password/form/$', views.change_password_form, name='Change_Password_Form'),
    re_path(r'^change_password$', views.change_password, name='Change_Password'),
    re_path(r'^logout/$', LogoutView.as_view(), {'next_page': 'Main'}, name='LogOut'),
    re_path(r'^user/(?P<username>[\w]+)/$', views.user_profile, name='User_Profile'),

    # live WeighBridge
    re_path(r'^live_WeighBridge/ordering/form/$', views.lwb_order_form, name='Live_WeighBridge_Order_Form'),
    re_path(r'^live_WeighBridge/ordering/$', views.lwb_order, name='Live_WeighBridge_Order'),
    re_path(r'^live_WeighBridge/reject/$', views.lwb_reject, name='Reject'),
    re_path(r'^live_WeighBridge/driver/create/lwb/$', views.lwb_driver, name='Driver_Create_LWB'),
    re_path(r'^live_WeighBridge/Car/create/lwb/$', views.lwb_car, name='Car_Create_LWB'),
    re_path(r'^live_WeighBridge/PO/create/lwb/$', views.lwb_product_owner, name='Product_Owner_Create_LWB'),
    re_path(r'^live_WeighBridge/Aviculture/create/lwb/$', views.lwb_aviculture, name='Aviculture_Create_LWB'),
    re_path(r'^live_WeighBridge/create/form/$', views.lwb_create_form, name='Live_WeighBridge_Create_Form'),
    re_path(r'^live_WeighBridge/create/$', views.lwb_create, name='Live_WeighBridge_Create'),
    re_path(r'^slaughter/start/form/$', views.lwb_start_slaughter_form, name='Start_Slaughter_Form'),
    re_path(r'^slaughter/start/$', views.lwb_start_slaughter, name='Start_Slaughter'),
    re_path(r'^slaughter/finish/form/$', views.lwb_finish_slaughter_form, name='Finish_Slaughter_Form'),
    re_path(r'^slaughter/finish/$', views.lwb_finish_slaughter, name='Finish_Slaughter'),
    re_path(r'^slaughter/capability/form/$', views.lwb_capability_form, name='Capability_Form'),
    re_path(r'^slaughter/capability/$', views.lwb_capability, name='Capability_Slaughter'),

    # first WeightLifting
    re_path(r'^first/WeightLifting/form/$', views.first_weightlifting_form, name='First_WeightLifting_Form'),
    re_path(r'^first/WeightLifting/$', views.first_weightlifting, name='First_WeightLifting'),
    re_path(r'^pre/cold/enter/form/$', views.pre_cold_enter_form, name='Pre_Cold_Enter_Form'),
    re_path(r'^pre/cold/enter/$', views.pre_cold_enter, name='Pre_Cold_Enter'),
    re_path(r'^pre/cold/exit/form/$', views.pre_cold_exit_form, name='Pre_Cold_Exit_Form'),
    re_path(r'^pre/cold/exit/$', views.pre_cold_exit, name='Pre_Cold_Exit'),
    re_path(r'^distribute/form/$', views.distribute_form, name='Distribute_Form'),
    re_path(r'^distribute/$', views.distribute, name='Distribute'),
    re_path(r'^distribute/root/empty/$', views.distribute_root_empty, name='Distribute_Root_Empty'),
    re_path(r'^distribute/root/full/$', views.distribute_root_full, name='Distribute_Root_Full'),
    re_path(r'^distribute/driver/create/$', views.distribute_driver_create, name='Driver_Create_Distribute'),
    re_path(r'^freeze/tunnel/enter/form/$', views.freeze_tunnel_enter_form, name="Freeze_Tunnel_Enter_Form"),
    re_path(r'^freeze/tunnel/enter/$', views.freeze_tunnel_enter, name="Freeze_Tunnel_Enter"),
    re_path(r'^freeze/tunnel/exit/form/$', views.freeze_tunnel_exit_form, name="Freeze_Tunnel_Exit_Form"),
    re_path(r'^freeze/tunnel/exit/$', views.freeze_tunnel_exit, name="Freeze_Tunnel_Exit"),
    re_path(r'^paperBox/create/form/$', views.paper_box_create_form, name='PaperBox_Create_Form'),
    re_path(r'^paperBox/create/$', views.paper_box_create, name='PaperBox_Create'),
    re_path(r'^coldHouse/enter/form/$', views.cold_house_enter_form, name='ColdHouse_Enter_Form'),
    re_path(r'^coldHouse/enter/$', views.cold_house_enter, name='ColdHouse_Enter'),
    re_path(r'^coldHouse/exit/form/$', views.cold_house_exit_form, name='ColdHouse_Exit_Form'),
    re_path(r'^coldHouse/exit/$', views.cold_house_exit, name='ColdHouse_Exit'),
    re_path(r'^segmentation/form/$', views.segmentation_form, name='Segmentation_Form'),
    re_path(r'^segmentation/$', views.segmentation, name='Segmentation'),
    re_path(r'^fwl/finish/(?P<fwl_id>[\w]+)/$', views.fwl_finish, name='Fwl_finish'),

    # monitor data
    re_path(r'^company/list/$', views.company_list, name='Company_List'),
    re_path(r'^company/user/list/$', views.company_user_list, name='Company_User_List'),
    re_path(r'^live/weighbridge/list/(?P<year>[\d]{1,4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/(?P<car_empty>[\d]{1})/(?P<product_category>[\d]{1})/(?P<slaughter_status>[\d]{1})/$',
            views.company_live_weighbridge_list, name='Company_Live_WeighBridge_List'),

    re_path(r'lw/filter/$', views.lw_filter, name='LW_Filter'),

    re_path(r'^driver/list/(?P<year>[\d]{1,4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/(?P<phone_number>[\w]+)/(?P<product_category>[\d]{1})/(?P<model_type>[\d]{1})/$',
            views.driver_list, name='Driver_List'),

    re_path(r'driver/filter/$', views.driver_filter, name='Driver_Filter'),

    re_path(r'^car/list/(?P<year>[\d]{1,4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/(?P<car_number>[\w]+)/(?P<product_category>[\d]{1})/(?P<model_type>[\d]{1})/$',
            views.car_list, name='Car_List'),

    re_path(r'car/filter/$', views.car_filter, name='Car_Filter'),

    re_path(r'^product_owner/list/(?P<year>[\d]{1,4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/(?P<po_name>[\w]+)/(?P<po_lastname>[\w]+)/(?P<product_category>[\d]{1})/(?P<model_type>[\d]{1})/(?P<car_number>.*)/$', views.product_owner_list,
            name='Product_Owner_List'),

    re_path(r'po/filter/$', views.po_filter, name='PO_Filter'),

    re_path(r'^weight/lifting/list/(?P<year>[\d]{1,4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/(?P<product_category>[\d]{1})/(?P<model_type>[\d]{1})/(?P<exist>[\d]{1,2})/$',
            views.weight_lifting_list, name='Weight_Lifting_List'),

    re_path(r'wl/filter/$', views.wl_filter, name='WL_Filter'),

    re_path(r'^cold/house/list/(?P<year>[\d]{1,4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/(?P<product_category>[\d]{1})/(?P<model_type>[\d]{1})/(?P<exist>[\d]{1,2})/$',
            views.cold_house_list, name='Cold_House_List'),

    re_path(r'ch/filter/$', views.ch_filter, name='CH_Filter'),

    # automations
    re_path(r'^automation/file/create/form/$', views.automation_file_create_form, name='Automation_File_Create_Form'),
    re_path(r'^automation/file/create/$', views.automation_file_create, name='Automation_File_Create'),
    re_path(r'^automation/message/create/form/$', views.automation_message_create_form,
            name='Automation_Message_Create_Form'),

    re_path(r'^automation/message/create/$', views.automation_message_create, name='Automation_Message_Create'),
    re_path(r'^automation/view/(?P<id>[\w]+)/$', views.automation_view, name='Automation_view'),
    re_path(r'^automation/send/list/(?P<status>[\d]{1})/$', views.automation_send_list, name='Automation_Send_List'),
    re_path(r'^automation/recv/list/(?P<status>[\d]{1})/$', views.automation_recv_list, name='Automation_Recv_List'),
    re_path(r'^automation/delete/(?P<id>[\w]+)/$', views.automation_delete, name='Automation_delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
