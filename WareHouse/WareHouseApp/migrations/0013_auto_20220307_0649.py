# Generated by Django 3.1.3 on 2022-03-07 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WareHouseApp', '0012_auto_20220306_0802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distributed',
            name='sales_input_id',
        ),
        migrations.AddField(
            model_name='distributed',
            name='product_category',
            field=models.CharField(choices=[('C', 'chicken'), ('T', 'turkey'), ('Q', 'quail')], default='C', max_length=1),
        ),
        migrations.AddField(
            model_name='distributed',
            name='sales_input_idistd',
            field=models.CharField(default='229425742108920808823181241697747016909', max_length=200),
        ),
        migrations.AddField(
            model_name='distributedroot',
            name='create_time',
            field=models.FloatField(default=1646635742.5691938),
        ),
        migrations.AddField(
            model_name='distributedroot',
            name='create_time_format',
            field=models.CharField(default='Mon Mar  7 06:49:02 2022', max_length=50),
        ),
        migrations.AddField(
            model_name='distributedroot',
            name='exit_time',
            field=models.FloatField(default=1646635742.5692394),
        ),
        migrations.AddField(
            model_name='distributedroot',
            name='exit_time_format',
            field=models.CharField(default='Mon Mar  7 06:49:02 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='automation',
            name='code',
            field=models.CharField(default=2331, max_length=10),
        ),
        migrations.AlterField(
            model_name='aviculture',
            name='aviculture_id',
            field=models.CharField(default='229425741633551833737595216136483314893', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.CharField(default='229425741475095508709066540949395414221', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ceo',
            name='ceo_id',
            field=models.CharField(default='229425740841270208594951840201043811533', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='cold_house_primary_key',
            field=models.CharField(default='229425742346605296365974254478378867917', max_length=150),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date',
            field=models.FloatField(default=1646635742.5720537),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date_format',
            field=models.CharField(default='Mon Mar  7 06:49:02 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='exit_date_format',
            field=models.CharField(default='Mon Mar  7 06:49:02 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(default='229425740762042046080687502607499861197', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='bill_of_lading',
            field=models.CharField(default='229425742029692646308916904104203066573', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date',
            field=models.FloatField(default=1646635742.5700035),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date_format',
            field=models.CharField(default='Mon Mar  7 06:49:02 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='dist_id',
            field=models.CharField(default='229425741950464483794652566510659116237', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_id',
            field=models.CharField(default='229425741554323671223330878542939364557', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weight_lifting_id',
            field=models.CharField(default='229425741792008158766123891323571215565', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time',
            field=models.FloatField(default=1646635742.5673032),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time_format',
            field=models.CharField(default='Mon Mar  7 06:49:02 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date',
            field=models.FloatField(default=1646635742.5710218),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date_format',
            field=models.CharField(default='Mon Mar  7 06:49:02 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='exit_date_format',
            field=models.CharField(default='Mon Mar  7 06:49:02 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='freeze_tunnel_id',
            field=models.CharField(default='229425742188148971337445579291290967245', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='input_id',
            field=models.CharField(default='229425742267377133851709916884834917581', max_length=200),
        ),
        migrations.AlterField(
            model_name='freezingtunnelmanager',
            name='Freezing_tunnel_Manager_id',
            field=models.CharField(default='229425741078954696137744852981675662541', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='live_weighbridge_id',
            field=models.CharField(default='229425741712779996251859553730027265229', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date',
            field=models.FloatField(default=1646635742.5656297, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date_format',
            field=models.CharField(default='Mon Mar  7 06:49:02 2022', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridgemanager',
            name='Live_Weighbridge_Manager_id',
            field=models.CharField(default='229425741158182858652009190575219612877', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='box_id',
            field=models.CharField(default='229425742425833458880238592071922818253', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='exit_time',
            field=models.FloatField(default=1646635742.573303, null=True),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time',
            field=models.FloatField(default=1646635742.5732627),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time_format',
            field=models.CharField(default='Mon Mar  7 06:49:02 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='precold',
            name='entry_time',
            field=models.FloatField(default=1646635742.5682602),
        ),
        migrations.AlterField(
            model_name='precold',
            name='entry_time_format',
            field=models.CharField(default='Mon Mar  7 06:49:02 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='precold',
            name='pc_id',
            field=models.CharField(default='229425741871236321280388228917115165901', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='precoldmanager',
            name='Pre_Cold_id',
            field=models.CharField(default='229425741237411021166273528168763563213', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productowner',
            name='product_owner_id',
            field=models.CharField(default='229425741395867346194802203355851463885', max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salesmanager',
            name='sales_manager_id',
            field=models.CharField(default='229425740920498371109216177794587761869', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='slaughteremployee',
            name='Slaughter_Employee_id',
            field=models.CharField(default='229425741316639183680537865762307513549', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='weightliftingmanager',
            name='Weight_Lifting_Manager_id',
            field=models.CharField(default='229425740999726533623480515388131712205', max_length=250, primary_key=True, serialize=False),
        ),
    ]