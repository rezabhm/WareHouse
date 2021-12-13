from django.urls import re_path

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
    7.  edit form url
    8.  edit url
    9.  change password form
    10. change password

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
    12. edit live weighbridge form
    13. edit live weighbridge
    
first weighbridge :
    
    1.  first weight lifting form 
    2.  first weight lifting
    3.  pre-cold enter form
    4.  pre-cold enter
    5.  pre-cold
    6.  pre-cold exit form
    7. pre-cold exit
    8.  distribute form
    9.  distribute 
    10. freezing tunnel form
    11. freezing tunnel
    12. freezing tunnel exit form
    13. freezing tunnel exit

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
    4.  see all of live weighbridge that manager create with it's filter
    5.  ceo edit live weighbridge form
    6.  ceo edit live weighbridge
    7.  see all of company weight lifting with 'tis type filter
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
    18. see cold-house with entry time and above filter
    19. see cold-house with exit time d above filter
    20. see all of paperBox with (product_type and status and product_owner and )
    21. see all of paperBox with packing time
    22. delete live weighbridge and first_weight_lifting and pre-cold and freezing tunnel and coldHouse and distribute
    23. delete drive and car and product_owner 
    24. delete user 

"""

urlpatterns = [

]
