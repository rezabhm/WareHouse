# Generated by Django 3.1.3 on 2021-12-29 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WareHouseApp', '0005_auto_20211229_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstweightlifting',
            name='choise_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.CharField(default='22564818027743016261069297379381056744', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ceo',
            name='ceo_id',
            field=models.CharField(default='22564817473145878661218934224573404392', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date',
            field=models.FloatField(default=1640765979.3127477),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(default='22564817393917716146954596631029454056', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='bill_of_lading',
            field=models.CharField(default='22564818423883828832390985347100808424', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date',
            field=models.FloatField(default=1640765979.2902575),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_id',
            field=models.CharField(default='22564818106971178775333634972925007080', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weight_lifting_id',
            field=models.CharField(default='22564818265427503803862310160012907752', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time',
            field=models.FloatField(default=1640765979.2627814),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date',
            field=models.FloatField(default=1640765979.304215),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='freeze_tunnel_id',
            field=models.CharField(default='22564818503111991346655322940644758760', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='freezingtunnelmanager',
            name='Freezing_tunnel_Manager_id',
            field=models.CharField(default='22564817710830366204011947005205255400', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='live_weighbridge_id',
            field=models.CharField(default='22564818186199341289597972566468957416', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date',
            field=models.FloatField(default=1640765979.2379174),
        ),
        migrations.AlterField(
            model_name='liveweighbridgemanager',
            name='Live_Weighbridge_Manager_id',
            field=models.CharField(default='22564817790058528718276284598749205736', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='box_id',
            field=models.CharField(default='22564818582340153860919660534188709096', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time',
            field=models.FloatField(default=1640765979.3298109),
        ),
        migrations.AlterField(
            model_name='precold',
            name='entry_time',
            field=models.FloatField(default=1640765979.2765205),
        ),
        migrations.AlterField(
            model_name='precold',
            name='pc_id',
            field=models.CharField(default='22564818344655666318126647753556858088', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='precoldmanager',
            name='Pre_Cold_id',
            field=models.CharField(default='22564817869286691232540622192293156072', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productowner',
            name='product_owner_id',
            field=models.CharField(default='22564817948514853746804959785837106408', max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salesmanager',
            name='sales_manager_id',
            field=models.CharField(default='22564817552374041175483271818117354728', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='weightliftingmanager',
            name='Weight_Lifting_Manager_id',
            field=models.CharField(default='22564817631602203689747609411661305064', max_length=250, primary_key=True, serialize=False),
        ),
    ]
