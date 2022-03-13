# Generated by Django 4.0.3 on 2022-03-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WareHouseApp', '0020_rename_product_pre_cold_status_precold_product_object_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distributedroot',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='distributedroot',
            name='create_time_format',
        ),
        migrations.AddField(
            model_name='distributedroot',
            name='empty_time',
            field=models.FloatField(default=1647179692.9407043),
        ),
        migrations.AddField(
            model_name='distributedroot',
            name='empty_time_format',
            field=models.CharField(default='Sun Mar 13 13:54:52 2022', max_length=50),
        ),
        migrations.AddField(
            model_name='distributedroot',
            name='enter_time',
            field=models.FloatField(default=1647179692.9407318),
        ),
        migrations.AddField(
            model_name='distributedroot',
            name='enter_time_format',
            field=models.CharField(default='Sun Mar 13 13:54:52 2022', max_length=50),
        ),
        migrations.AddField(
            model_name='distributedroot',
            name='enter_user',
            field=models.CharField(default='Admin', max_length=50),
        ),
        migrations.AddField(
            model_name='distributedroot',
            name='exit_user',
            field=models.CharField(default='Admin', max_length=50),
        ),
        migrations.AddField(
            model_name='distributedroot',
            name='finish_user',
            field=models.CharField(default='Admin', max_length=50),
        ),
        migrations.AddField(
            model_name='distributedroot',
            name='weighting_time',
            field=models.FloatField(default=1647179692.9406698),
        ),
        migrations.AddField(
            model_name='distributedroot',
            name='weighting_time_format',
            field=models.CharField(default='Sun Mar 13 13:54:52 2022', max_length=50),
        ),
        migrations.AddField(
            model_name='distributedroot',
            name='weighting_user',
            field=models.CharField(default='Admin', max_length=50),
        ),
        migrations.AlterField(
            model_name='automation',
            name='code',
            field=models.CharField(default=5193, max_length=10),
        ),
        migrations.AlterField(
            model_name='aviculture',
            name='aviculture_id',
            field=models.CharField(default='53558311433771662886414782001321555636', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.CharField(default='53556643680950737622108437901166982836', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ceo',
            name='ceo_id',
            field=models.CharField(default='53553034838148212881531051974229178036', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='cold_house_primary_key',
            field=models.CharField(default='53562408322055275495311744158993430196', max_length=150),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date',
            field=models.FloatField(default=1647179692.9429517),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date_format',
            field=models.CharField(default='Sun Mar 13 13:54:52 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='exit_date_format',
            field=models.CharField(default='Sun Mar 13 13:54:52 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(default='53552113414618171987284839058086770356', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='bill_of_lading',
            field=models.CharField(default='53561291204963824368151675189293692596', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date',
            field=models.FloatField(default=1647179692.9414368),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date_format',
            field=models.CharField(default='Sun Mar 13 13:54:52 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='sales_input_idistd',
            field=models.CharField(default='53561348249240834638474742540937934516', max_length=200),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='dist_id',
            field=models.CharField(default='53560600335386699983127859486046762676', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='exit_time',
            field=models.FloatField(default=1647179692.9407532),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='exit_time_format',
            field=models.CharField(default='Sun Mar 13 13:54:52 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_id',
            field=models.CharField(default='53557046160016310084943413104434689716', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weight_lifting_id',
            field=models.CharField(default='53559599683694144824544053025954018996', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time',
            field=models.FloatField(default=1647179692.93928),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time_format',
            field=models.CharField(default='Sun Mar 13 13:54:52 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date',
            field=models.FloatField(default=1647179692.9421139),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date_format',
            field=models.CharField(default='Sun Mar 13 13:54:52 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='exit_date_format',
            field=models.CharField(default='Sun Mar 13 13:54:52 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='freeze_tunnel_id',
            field=models.CharField(default='53561743597771780817519334325250111156', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='input_id',
            field=models.CharField(default='53561994751046951035469505859572676276', max_length=200),
        ),
        migrations.AlterField(
            model_name='freezingtunnelmanager',
            name='Freezing_tunnel_Manager_id',
            field=models.CharField(default='53554460152791844496964359829895722676', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='live_weighbridge_id',
            field=models.CharField(default='53558536441753203397133547666140509876', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date',
            field=models.FloatField(default=1647179692.9381056, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date_format',
            field=models.CharField(default='Sun Mar 13 13:54:52 2022', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridgemanager',
            name='Live_Weighbridge_Manager_id',
            field=models.CharField(default='53554906207346799805185011482336114356', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='box_id',
            field=models.CharField(default='53563192680864166712253920244101756596', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='exit_time',
            field=models.FloatField(default=1647179692.9438674, null=True),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time',
            field=models.FloatField(default=1647179692.9438381),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time_format',
            field=models.CharField(default='Sun Mar 13 13:54:52 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='precold',
            name='pc_id',
            field=models.CharField(default='53560110705342361829521531384433686196', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='precold',
            name='time_format',
            field=models.CharField(default='Sun Mar 13 13:54:52 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='precold',
            name='time_obj',
            field=models.FloatField(default=1647179692.9400556),
        ),
        migrations.AlterField(
            model_name='precoldmanager',
            name='Pre_Cold_id',
            field=models.CharField(default='53555456843076273942331286612790949556', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productowner',
            name='product_owner_id',
            field=models.CharField(default='53556322806892554851541184048168122036', max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salesmanager',
            name='sales_manager_id',
            field=models.CharField(default='53553560120865682454089297170619905716', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='slaughteremployee',
            name='Slaughter_Employee_id',
            field=models.CharField(default='53555898143941478394691682652594321076', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='weightliftingmanager',
            name='Weight_Lifting_Manager_id',
            field=models.CharField(default='53554018851926640044603963790092351156', max_length=250, primary_key=True, serialize=False),
        ),
    ]