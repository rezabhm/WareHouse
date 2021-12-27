from django.db import models
from django.contrib.auth.models import User
from uuid import uuid1
import time

# Create your models here.


class Company(models.Model):

    """
    this is company model

    Company model's column:

        1. company name
        2. company id

    """

    # company name
    name = models.CharField(max_length=15)

    # company uuid
    company_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)


class CEO(models.Model):

    """
    this is company ceo user

    CEO model's column :

        1. username
        2. name
        3. lastname
        4. phone number
        5. user uuid

    relation :

        1. Company      ==> Foreign Key
        2. django User  ==> Foreign Key

    """

    # username for ceo
    username = models.CharField(max_length=25)

    # ceo name and lastname
    name = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)

    # ceo phone number
    phone_number = models.CharField(max_length=12)

    # ceo uuid
    ceo_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)

    # relation
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)


class SalesManager(models.Model):

    """
    this is company Sales Manager user

    Sales Manager model's column :

        1. username
        2. name
        3. lastname
        4. phone number
        5. user uuid

    relation :

        1. Company      ==> Foreign Key
        2. django User  ==> Foreign Key

    """

    # username for Sales Manager
    username = models.CharField(max_length=25)

    # Sales Manager name and lastname
    name = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)

    # Sales Manager phone number
    phone_number = models.CharField(max_length=12)

    # Sales Manager uuid
    sales_manager_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)

    # relation
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)


class WeightLiftingManager(models.Model):

    """
    this is company Weight Lifting Manager user

    Weight Lifting Manager model's column :

        1. username
        2. name
        3. lastname
        4. phone number
        5. user uuid

    relation :

        1. Company      ==> Foreign Key
        2. django User  ==> Foreign Key

    """

    # username for Weight Lifting Manager
    username = models.CharField(max_length=25)

    # Weight Lifting Manager name and lastname
    name = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)

    # Weight Lifting Manager phone number
    phone_number = models.CharField(max_length=12)

    # Weight Lifting Manager uuid
    Weight_Lifting_Manager_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)

    # relation
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)


class FreezingTunnelManager(models.Model):

    """
    this is company Freezing tunnel Manager user

    Freezing tunnel Manager model's column :

        1. username
        2. name
        3. lastname
        4. phone number
        5. user uuid

    relation :

        1. Company      ==> Foreign Key
        2. django User  ==> Foreign Key

    """

    # username for Freezing tunnel Manager
    username = models.CharField(max_length=25)

    # Freezing tunnel Manager name and lastname
    name = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)

    # Freezing tunnel Manager phone number
    phone_number = models.CharField(max_length=12)

    # Freezing tunnel Manager uuid
    Freezing_tunnel_Manager_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)

    # relation
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)


class LiveWeighbridgeManager(models.Model):

    """
    this is company Live Weighbridge Manager user

    Live Weighbridge Manager model's column :

        1. username
        2. name
        3. lastname
        4. phone number
        5. user uuid

    relation :

        1. Company      ==> Foreign Key
        2. django User  ==> Foreign Key

    """

    # username for Live Weighbridge Manager
    username = models.CharField(max_length=25)

    # Live Weighbridge Manager name and lastname
    name = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)

    # Live Weighbridge Manager phone number
    phone_number = models.CharField(max_length=12)

    # Live Weighbridge Manager uuid
    Live_Weighbridge_Manager_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)

    # relation
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)


class PreColdManager(models.Model):

    """
    this is company Pre-Cold Manager user

    Pre-Cold Manager model's column :

        1. username
        2. name
        3. lastname
        4. phone number
        5. user uuid

    relation :

        1. Company      ==> Foreign Key
        2. django User  ==> Foreign Key

    """

    # username for Pre Cold Manager
    username = models.CharField(max_length=25)

    # Pre Cold Manager name and lastname
    name = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)

    # Pre Cold Manager phone number
    phone_number = models.CharField(max_length=12)

    # Pre Cold Manager uuid
    Pre_Cold_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)

    # relation
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)


class ProductOwner(models.Model):

    """
    define product owner

    ProductOwner table's column:

        1. name
        2. id

    """

    # product owner name
    name = models.CharField(max_length=25)

    # product owner last name
    last_name = models.CharField(max_length=25)

    # id
    product_owner_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)

    def __str__(self):
        return str(self.name)


class Car(models.Model):

    """
    car that carry product

    car table's column:

        1. car number
        2. live product status
        3. id

    relation :

        1. product owner ==> Foreign key

    """

    # car number
    car_number = models.CharField(max_length=20)

    # live product status that define our product is a live or not
    live_product = models.BooleanField(default=True)

    # Car id
    car_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)

    # relation
    product_owner = models.ForeignKey(ProductOwner, models.PROTECT)

    def __str__(self):
        return self.car_number


class Driver(models.Model):

    """
    for store car's driver data

    driver table's column:

        1. name
        2. last name
        3. phone number
        4. id

    relation :

        1. car ==> Foreign key
    """

    # driver name
    name = models.CharField(max_length=25)

    # driver lastname
    last_name = models.CharField(max_length=25)

    # phone number
    phone_number = models.CharField(max_length=12)

    # driver id
    driver_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)

    # relation
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + ' ' + str(self.last_name)


class LiveWeighbridge(models.Model):

    """
    Live Weighbridge for store initial weight lifting

    Live Weighbridge table's column :

        1.  id
        2.  final weight
        3.  car weight
        4.  car product status
        5.  weighting date
        6.  product category
        7.  slaughter status
        8.  slaughter start date
        9.  slaughter finish date
        10. buying price

    relation :

        1. LiveWeighbridgeManager ==> Foreign Key
        2. driver                 ==> OneToOne

    """

    # live weighbridge id
    live_weighbridge_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)

    # final weight
    final_weight = models.FloatField(null=True)

    # car weight
    car_weight = models.FloatField(null=True)

    # this param define car is empty or not if equal True it means car is empty
    car_empty = models.BooleanField(default=False)

    # weighting date
    weighting_date = models.FloatField(default=time.time())

    # product category
    type_of_gender = (('C', "chicken"),
                      ('T', "turkey"),
                      ('Q', "quail"))

    product_category = models.CharField(max_length=1, choices=type_of_gender)

    # slaughter status that if equal True slaughting has start
    slaughter_status = models.BooleanField(default=False)

    # slaughting start time
    slaughter_start_date = models.FloatField(null=True)

    # slaughting finish time
    slaughter_finish_date = models.FloatField(null=True)

    # buying price
    buy_price = models.IntegerField()

    # relation
    Live_Weighbridge_Manager = models.ForeignKey(LiveWeighbridgeManager, on_delete=models.PROTECT, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.driver.name) + ' : ' + str(self.final_weight)


class FirstWeightLifting(models.Model):

    """
    define first Weight Lifting Table

    FirstWeightLifting table's column name:

        1. weighting time
        2. weight
        3. product category
        4. id
        5. define sale category

    relation :

        1. LiveWeighBridge      ==> Foreign Key
        2. WeightLiftingManager ==> Foreign Key
    """

    # weighting time
    weighting_time = models.FloatField(default=time.time())

    # weight
    weight = models.FloatField()

    # product category
    type_of_gender = (('C', "chicken"),
                      ('T', "turkey"),
                      ('Q', "quail"))

    product_category = models.CharField(max_length=1, choices=type_of_gender)

    # id
    weight_lifting_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)

    # define sale category
    sale_cat = (
        ('P', 'pre-cold'),
        ('D', 'distribute'),
        ('F', 'freezing tunnel'),
    )
    sales_category = models.CharField(max_length=1, choices=sale_cat)

    # relation
    Live_Weigh_Bridge = models.ForeignKey(LiveWeighbridge, on_delete=models.PROTECT)
    Weight_Lifting_Manager = models.ForeignKey(WeightLiftingManager, on_delete=models.PROTECT)

    def __str__(self):
        return self.Weight_Lifting_Manager.username + ' ' + self.sales_category + ' ' + str(self.weight)


class PreCold(models.Model):

    """
    for store pre-cold product

    pre-cold table's column:

        1. entry date
        2. exit time
        3. weight
        4. product category
        5. pre-cold id
        6. pallet id
        7. exit status
        8. id

    relation:

        1. FirstWeightLifting ==> Foreign Key
        2. PreColdManager     ==> Foreign Key

    """

    # id
    pc_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)

    # entry time
    entry_time = models.FloatField(default=time.time())

    # exit time
    exit_time = models.FloatField(null=True)

    # weight
    weight = models.FloatField()

    # product category
    type_of_gender = (('C', "chicken"),
                      ('T', "turkey"),
                      ('Q', "quail"))
    product_category = models.CharField(max_length=1, choices=type_of_gender)

    # pre-cold id
    pre_cold_id = models.IntegerField()

    # pallet id
    pallet_id = models.CharField(max_length=25, null=True)

    # product in pre-cold status
    product_pre_cold_status = models.BooleanField(default=True)

    # relation
    First_Weight_Lifting = models.ForeignKey(FirstWeightLifting, on_delete=models.PROTECT)
    PreCold_Manager = models.ForeignKey(PreColdManager, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.weight) + ' ' + str(self.entry_time)


class Distributed(models.Model):

    """
     Quick sale after slaughter

    Distributed model's column:

        1. Date
        2. weight
        3. sale price
        4. product category
        5. Bill of lading
        6. number of box

    relation's:

        1. FirstWeightLifting  ==> foreignkey
        2. SalesManager  ==> foreignkey
        3. driver  ==> foreignkey

    """

    # date of weighting
    date = models.FloatField(default=time.time())

    # weight of product
    weight = models.FloatField()

    # product price
    sale_price = models.IntegerField()

    # product category
    type_of_gender = (('C', "chicken"),
                      ('T', "turkey"),
                      ('Q', "quail"))
    product_category = models.CharField(choices=type_of_gender, max_length=1)

    # bill of lading
    bill_of_lading = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)

    # number of box
    number_of_box = models.IntegerField(null=True)

    # relation
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    first_weight_lifting = models.ForeignKey(FirstWeightLifting, on_delete=models.CASCADE)
    sales_manager = models.ForeignKey(SalesManager, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.weight) + " " + time.ctime(self.date) + ' ' + str(self.bill_of_lading)


class FreezingTunnel(models.Model):

    """
     a cold place for Short-term care of chickens

    FreezingTunnel model's column:

        1. Entry Date
        2. Exit date
        3. Product Type
        4. pallet id
        5. tunnel id
        6. status
        7. weight
        8. id

    relation's:

        1.FirstWeightLifting  ==> foreignkey
        1.FreezingTunnelManager  ==> foreignkey

    """

    # id
    freeze_tunnel_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)

    # exit and entry date
    entry_date = models.FloatField(default=time.time())
    exit_date = models.FloatField(null=True)

    # product category
    type_of_gender = (('C', "chicken"),
                      ('T', "turkey"),
                      ('Q', "quail"))
    product_category = models.CharField(choices=type_of_gender, max_length=1)

    # weight of product
    weight = models.FloatField()

    # tunnel id that product freeze in it
    tunnel_id = models.IntegerField()

    # pallet id that include product
    pallet_id = models.CharField(max_length=15, null=True)

    # this param determine that product is in the tunnel or not if equal True it mean it still in the tunnel
    status = models.BooleanField(default=True, verbose_name="آیا خارج شده یا نه")

    # relation
    first_weight_lifting = models.ForeignKey(FirstWeightLifting, on_delete=models.CASCADE)
    freezing_tunnel_manager = models.ForeignKey(FreezingTunnelManager, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.weight) + ' ' + str(self.tunnel_id)


class ColdHouse(models.Model):

    """
     a cold place for keeping chicken

    ColdHouse model's column:

        1. Entry date
        2. Exit date
        3. Total pallet weight
        4. Pallet weight with product
        5. number of carton
        6. pallet id
        7. keeping id
        8. status
        9. id

    relation's:

        1.FreezingTunnelManager  ==> foreignkey

    """

    # entry and exit time
    entry_date = models.FloatField(default=time.time())
    exit_date = models.FloatField(null=True)

    # determine pallet is in coldHouse or not
    pallet_status = models.BooleanField(default=True)

    # pallet weight
    total_pallet_weight = models.FloatField()
    pallet_weight_without_product = models.FloatField(null=True)

    # number of paper box that exist in pallet
    number_of_box = models.IntegerField()

    # pallet id and coldHouse id
    pallet_id = models.CharField(max_length=15)
    cold_house_id = models.IntegerField(max_length=15)

    # relation
    freezing_tunnel_manager = models.ForeignKey(FreezingTunnelManager, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pallet_id) + ' & ' + str(self.cold_house_id)


class PaperBox(models.Model):

    """
    this is a paper box for chicken

    paperBox model's column:

        1. product category
        2. paperBox Weight
        3. number of product
        4. Packing time
        5. box id

    relation's:

        1.ColdHouse  ==> foreignkey

    """

    # product category
    type_of_gender = (('C', "chicken"),
                      ('T', "turkey"),
                      ('Q', "quail"))
    product_category = models.CharField(choices=type_of_gender, max_length=1)

    # paper box weight
    paper_box_weight = models.FloatField()

    # if it equal True it means paper is in the cold House and or exit from it and if equal False it mean
    # it didn't enter to coldHouse
    box_status = models.BooleanField(default=False)

    # number of product in box
    number_of_product = models.IntegerField()

    # packing time
    packing_time = models.FloatField(default=time.time())

    # box id
    box_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)

    # relation
    cold_house = models.ForeignKey(ColdHouse, models.CASCADE, null=True)

    def __str__(self):
        return str(self.box_id)
