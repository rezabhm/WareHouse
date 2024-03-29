# Generated by Django 3.1.3 on 2022-03-09 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WareHouseApp', '0016_auto_20220309_0627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firstweightlifting',
            name='Live_Weigh_Bridge',
        ),
        migrations.AddField(
            model_name='firstweightlifting',
            name='product_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='WareHouseApp.productowner'),
        ),
        migrations.AlterField(
            model_name='automation',
            name='code',
            field=models.CharField(default=3866, max_length=10),
        ),
        migrations.AlterField(
            model_name='aviculture',
            name='aviculture_id',
            field=models.CharField(default='104472324976492537819555016159709633105', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.CharField(default='104472324818036212791026340972621732433', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ceo',
            name='ceo_id',
            field=models.CharField(default='104472324184210912676911640224270129745', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='cold_house_primary_key',
            field=models.CharField(default='104472325689546000447934054501605186129', max_length=150),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date',
            field=models.FloatField(default=1646840025.305215),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date_format',
            field=models.CharField(default='Wed Mar  9 15:33:45 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='exit_date_format',
            field=models.CharField(default='Wed Mar  9 15:33:45 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(default='104472324104982750162647302630726179409', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='bill_of_lading',
            field=models.CharField(default='104472325372633350390876704127429384785', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date',
            field=models.FloatField(default=1646840025.3028646),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date_format',
            field=models.CharField(default='Wed Mar  9 15:33:45 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='sales_input_idistd',
            field=models.CharField(default='104472325451861512905141041720973335121', max_length=200),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='create_time',
            field=models.FloatField(default=1646840025.301929),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='create_time_format',
            field=models.CharField(default='Wed Mar  9 15:33:45 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='dist_id',
            field=models.CharField(default='104472325293405187876612366533885434449', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='exit_time',
            field=models.FloatField(default=1646840025.3019934),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='exit_time_format',
            field=models.CharField(default='Wed Mar  9 15:33:45 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_id',
            field=models.CharField(default='104472324897264375305290678566165682769', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='Weight_Lifting_Manager',
            field=models.CharField(default='admin', max_length=20),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='sales_category',
            field=models.CharField(choices=[('P', 'pre-cold'), ('D', 'distribute'), ('F', 'freezing tunnel'), ('G', 'gate_bandi'), ('P', 'podr_gosht')], max_length=1),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weight_lifting_id',
            field=models.CharField(default='104472325134948862848083691346797533777', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time',
            field=models.FloatField(default=1646840025.2996137),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time_format',
            field=models.CharField(default='Wed Mar  9 15:33:45 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date',
            field=models.FloatField(default=1646840025.3041024),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date_format',
            field=models.CharField(default='Wed Mar  9 15:33:45 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='exit_date_format',
            field=models.CharField(default='Wed Mar  9 15:33:45 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='freeze_tunnel_id',
            field=models.CharField(default='104472325531089675419405379314517285457', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='input_id',
            field=models.CharField(default='104472325610317837933669716908061235793', max_length=200),
        ),
        migrations.AlterField(
            model_name='freezingtunnelmanager',
            name='Freezing_tunnel_Manager_id',
            field=models.CharField(default='104472324421895400219704653004901980753', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='live_weighbridge_id',
            field=models.CharField(default='104472325055720700333819353753253583441', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date',
            field=models.FloatField(default=1646840025.2974346, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date_format',
            field=models.CharField(default='Wed Mar  9 15:33:45 2022', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridgemanager',
            name='Live_Weighbridge_Manager_id',
            field=models.CharField(default='104472324501123562733968990598445931089', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='box_id',
            field=models.CharField(default='104472325768774162962198392095149136465', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='exit_time',
            field=models.FloatField(default=1646840025.3066468, null=True),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time',
            field=models.FloatField(default=1646840025.3066),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time_format',
            field=models.CharField(default='Wed Mar  9 15:33:45 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='precold',
            name='entry_time',
            field=models.FloatField(default=1646840025.3007014),
        ),
        migrations.AlterField(
            model_name='precold',
            name='entry_time_format',
            field=models.CharField(default='Wed Mar  9 15:33:45 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='precold',
            name='pc_id',
            field=models.CharField(default='104472325214177025362348028940341484113', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='precoldmanager',
            name='Pre_Cold_id',
            field=models.CharField(default='104472324580351725248233328191989881425', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productowner',
            name='product_owner_id',
            field=models.CharField(default='104472324738808050276762003379077782097', max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salesmanager',
            name='sales_manager_id',
            field=models.CharField(default='104472324263439075191175977817814080081', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='slaughteremployee',
            name='Slaughter_Employee_id',
            field=models.CharField(default='104472324659579887762497665785533831761', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='weightliftingmanager',
            name='Weight_Lifting_Manager_id',
            field=models.CharField(default='104472324342667237705440315411358030417', max_length=250, primary_key=True, serialize=False),
        ),
    ]
