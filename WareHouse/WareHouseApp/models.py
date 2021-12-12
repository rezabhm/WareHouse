from django.db import models
from uuid import uuid1

# Create your models here.


class Distributed(models.Model):

    """
     Quick sale after slaughter

    Distributed model's column:

        1. Date
        2. weight
        3. sale price
        4. Driver name
        5. Driver license plate number
        6. Name of the owner of the bar
        7. type of gender
        8. Bill of lading
        9. number of box

    relation's:

        1.FirstWeightLifting  ==> foreignkey
        1.SalesManager  ==> foreignkey

    """

    date = models.FloatField()
    weight = models.FloatField()
    saleprice = models.IntegerField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    firstweightlifting = models.ForeignKey(FirstWeightLifting, on_delete=models.CASCADE)
    salesmanager = models.ForeignKey(SalesManager, on_delete=models.CASCADE)
    chicken = 1
    turkey = 2
    quail = 3
    type_of_gender = (('chicken', "C"),
                      ('turkey', "T"),
                      ('quail', "Q"))
    type_of_gender = models.CharField(choices=type_of_gender, max_length=1)
    billoflading = models.IntegerField()
    numberofbox = models.IntegerField()

    def __str__(self):
        return self.type_of_gender


class FreezingTunnel(models.Model):

    """
     a cold place for Short-term care of chickens

    FreezingTunnel model's column:

        1. Date of arrival
        2. Exit date
        3. Product Type
        4. pallet id
        5. tunnel id
        6. status
        7. weight

    relation's:

        1.FirstWeightLifting  ==> foreignkey
        1.FreezingTunnelManager  ==> foreignkey

    """

    dateofarrival = models.FloatField()
    exitdate = models.FloatField()
    chicken = 1
    turkey = 2
    quail = 3
    type_of_gender = (('chicken', "C"),
                      ('turkey', "T"),
                      ('quail', "Q"))
    type_of_gender = models.CharField(choices=type_of_gender, max_length=1)
    weight = models.FloatField()
    tunnel_id = models.IntegerField(max_length=15)
    pallet_id = models.CharField(max_length=15)
    status = models.BooleanField(default=True, verbose_name="آیا خارج شده یا نه")

    def __str__(self):
        return self.type_of_gender



class ColdHouse(models.Model):

    """
     a cold place for keepingchicken

    ColdHouse model's column:

        1. Date of arrival
        2. Exit date
        3. Total pallet weight
        4. Pallet weight with product
        5. number of carton
        6. pallet id
        7. keeping id

    relation's:

        1.FreezingTunnelManager  ==> foreignkey

    """

    dateofarrival = models.FloatField()
    exitdate = models.FloatField()
    totalpalletweight = models.FloatField()
    palletweightwhitproduct = models.FloatField()
    numberofcarton = models.IntegerField()
    pallet_id = models.CharField(max_length=15)
    coldhouse_id = models.CharField(max_length=15)
    freezingtunnelmanager = models.ForeignKey(FreezingTunnelManager, on_delete=models.CASCADE)

    def __str__(self):
        return "dateofarrival:{}  exitdate:{}   pallet_id:{}".format(self.dateofarrival, self.exitdate, self.pallet_id)




class PaperBox(models.Model):

    """
    this's a paper box for chicken

    paperBox model's column:

        1. Type of gender
        2. carton Weight
        3. number of gender
        4. Packing time
        5. carton id

    relation's:

        1.Cold_house  ==> foreignkey

    """
    chicken = 1
    turkey = 2
    quail = 3
    type_of_gender = (('chicken', "C"),
                      ('turkey', "T"),
                      ('quail', "Q"))
    type_of_gender = models.CharField(choices=type_of_gender, max_length=1)
    carton_Weight = models.FloatField()
    number_of_gender = models.IntegerField()
    packing_time = models.FloatField()
    box_id = models.CharField(default=str(uuid1().int), max_length=250, primary_key=True)
    cold_house = models.ForeignKey(ColdHouse, models.CASCADE)


    def __str__(self):
        return self.type_of_gender



















