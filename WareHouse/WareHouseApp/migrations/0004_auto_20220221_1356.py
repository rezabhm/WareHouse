# Generated by Django 3.1.3 on 2022-02-21 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WareHouseApp', '0003_auto_20220221_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aviculture',
            name='aviculture_id',
            field=models.CharField(default='24771446913626131175907025794836787976', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.CharField(default='24771446755169806147378350607748887304', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ceo',
            name='ceo_id',
            field=models.CharField(default='24771446200572668547527987452941234952', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='cold_house_primary_key',
            field=models.CharField(default='24771447626679593804286064136732341000', max_length=150),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date',
            field=models.FloatField(default=1645451791.2740595),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date_format',
            field=models.CharField(default='Mon Feb 21 13:56:31 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='exit_date_format',
            field=models.CharField(default='Mon Feb 21 13:56:31 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(default='24771446121344506033263649859397284616', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='bill_of_lading',
            field=models.CharField(default='24771447309766943747228713762556539656', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date',
            field=models.FloatField(default=1645451791.272103),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date_format',
            field=models.CharField(default='Mon Feb 21 13:56:31 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='sales_input_id',
            field=models.CharField(default='24771447388995106261493051356100489992', max_length=200),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='dist_id',
            field=models.CharField(default='24771447230538781232964376169012589320', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_id',
            field=models.CharField(default='24771446834397968661642688201292837640', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weight_lifting_id',
            field=models.CharField(default='24771447072082456204435700981924688648', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time',
            field=models.FloatField(default=1645451791.269394),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time_format',
            field=models.CharField(default='Mon Feb 21 13:56:31 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date',
            field=models.FloatField(default=1645451791.272973),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date_format',
            field=models.CharField(default='Mon Feb 21 13:56:31 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='exit_date_format',
            field=models.CharField(default='Mon Feb 21 13:56:31 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='freeze_tunnel_id',
            field=models.CharField(default='24771447468223268775757388949644440328', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='input_id',
            field=models.CharField(default='24771447547451431290021726543188390664', max_length=200),
        ),
        migrations.AlterField(
            model_name='freezingtunnelmanager',
            name='Freezing_tunnel_Manager_id',
            field=models.CharField(default='24771446438257156090321000233573085960', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='live_weighbridge_id',
            field=models.CharField(default='24771446992854293690171363388380738312', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date',
            field=models.FloatField(default=1645451791.2678816, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date_format',
            field=models.CharField(default='Mon Feb 21 13:56:31 2022', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridgemanager',
            name='Live_Weighbridge_Manager_id',
            field=models.CharField(default='24771446517485318604585337827117036296', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='box_id',
            field=models.CharField(default='24771447705907756318550401730276291336', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='exit_time',
            field=models.FloatField(default=1645451791.2752926, null=True),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time',
            field=models.FloatField(default=1645451791.2752469),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time_format',
            field=models.CharField(default='Mon Feb 21 13:56:31 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='precold',
            name='entry_time',
            field=models.FloatField(default=1645451791.270367),
        ),
        migrations.AlterField(
            model_name='precold',
            name='entry_time_format',
            field=models.CharField(default='Mon Feb 21 13:56:31 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='precold',
            name='pc_id',
            field=models.CharField(default='24771447151310618718700038575468638984', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='precoldmanager',
            name='Pre_Cold_id',
            field=models.CharField(default='24771446596713481118849675420660986632', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productowner',
            name='product_owner_id',
            field=models.CharField(default='24771446675941643633114013014204936968', max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salesmanager',
            name='sales_manager_id',
            field=models.CharField(default='24771446279800831061792325046485185288', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='segmentation',
            name='first_weight_lifting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='WareHouseApp.firstweightlifting'),
        ),
        migrations.AlterField(
            model_name='weightliftingmanager',
            name='Weight_Lifting_Manager_id',
            field=models.CharField(default='24771446359028993576056662640029135624', max_length=250, primary_key=True, serialize=False),
        ),
    ]
