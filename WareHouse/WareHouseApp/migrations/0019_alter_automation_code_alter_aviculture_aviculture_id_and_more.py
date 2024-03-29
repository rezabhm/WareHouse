# Generated by Django 4.0.3 on 2022-03-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WareHouseApp', '0018_auto_20220309_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automation',
            name='code',
            field=models.CharField(default=3189, max_length=10),
        ),
        migrations.AlterField(
            model_name='aviculture',
            name='aviculture_id',
            field=models.CharField(default='324988666212204866791467044811543309759', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.CharField(default='324987068180166954079777783030065032639', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ceo',
            name='ceo_id',
            field=models.CharField(default='324983615416844582439945456384709389759', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='cold_house_primary_key',
            field=models.CharField(default='324992525416000936607351226337364176319', max_length=150),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date',
            field=models.FloatField(default=1647168868.6209555),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date_format',
            field=models.CharField(default='Sun Mar 13 10:54:28 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='exit_date_format',
            field=models.CharField(default='Sun Mar 13 10:54:28 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(default='324982754998999677529239190497408740799', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='bill_of_lading',
            field=models.CharField(default='324991439990174491185926194785244573119', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date',
            field=models.FloatField(default=1647168868.6194823),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date_format',
            field=models.CharField(default='Sun Mar 13 10:54:28 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='sales_input_idistd',
            field=models.CharField(default='324991495449888251170962510266009808319', max_length=200),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='create_time',
            field=models.FloatField(default=1647168868.6189356),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='create_time_format',
            field=models.CharField(default='Sun Mar 13 10:54:28 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='dist_id',
            field=models.CharField(default='324990921837991647897158333007809375679', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='exit_time',
            field=models.FloatField(default=1647168868.6189675),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='exit_time_format',
            field=models.CharField(default='Sun Mar 13 10:54:28 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_id',
            field=models.CharField(default='324987448475347022548598232041026645439', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weight_lifting_id',
            field=models.CharField(default='324989907717511465313637135645245074879', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time',
            field=models.FloatField(default=1647168868.617525),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time_format',
            field=models.CharField(default='Sun Mar 13 10:54:28 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date',
            field=models.FloatField(default=1647168868.620157),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date_format',
            field=models.CharField(default='Sun Mar 13 10:54:28 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='exit_date_format',
            field=models.CharField(default='Sun Mar 13 10:54:28 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='freeze_tunnel_id',
            field=models.CharField(default='324991892382982447635293853921200991679', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='input_id',
            field=models.CharField(default='324992053216152351591899168815420173759', max_length=200),
        ),
        migrations.AlterField(
            model_name='freezingtunnelmanager',
            name='Freezing_tunnel_Manager_id',
            field=models.CharField(default='324984989233182579783559328436808215999', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='live_weighbridge_id',
            field=models.CharField(default='324988897558439408443332817959878290879', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date',
            field=models.FloatField(default=1647168868.616416, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date_format',
            field=models.CharField(default='Sun Mar 13 10:54:28 2022', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridgemanager',
            name='Live_Weighbridge_Manager_id',
            field=models.CharField(default='324985418649823407096269085445019037119', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='box_id',
            field=models.CharField(default='324993295513740575256712635584561442239', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='exit_time',
            field=models.FloatField(default=1647168868.621856, null=True),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time',
            field=models.FloatField(default=1647168868.621825),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time_format',
            field=models.CharField(default='Sun Mar 13 10:54:28 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='precold',
            name='entry_time',
            field=models.FloatField(default=1647168868.6182985),
        ),
        migrations.AlterField(
            model_name='precold',
            name='entry_time_format',
            field=models.CharField(default='Sun Mar 13 10:54:28 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='precold',
            name='pc_id',
            field=models.CharField(default='324990416362314806890684486197406231999', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='precoldmanager',
            name='Pre_Cold_id',
            field=models.CharField(default='324985943932540876668827330641409764799', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productowner',
            name='product_owner_id',
            field=models.CharField(default='324986752852080147307714160725142695359', max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salesmanager',
            name='sales_manager_id',
            field=models.CharField(default='324984122477084673731706055065991540159', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='slaughteremployee',
            name='Slaughter_Employee_id',
            field=models.CharField(default='324986362257238951984529824553467538879', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='weightliftingmanager',
            name='Weight_Lifting_Manager_id',
            field=models.CharField(default='324984556647415251900276067686839381439', max_length=250, primary_key=True, serialize=False),
        ),
    ]
