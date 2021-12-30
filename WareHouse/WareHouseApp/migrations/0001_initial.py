# Generated by Django 3.1.3 on 2021-12-28 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_number', models.CharField(max_length=20)),
                ('live_product', models.BooleanField(default=True)),
                ('car_id', models.CharField(default='28779867591414251811368090861805491432', max_length=250, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ColdHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.FloatField(default=1640671927.4923098)),
                ('exit_date', models.FloatField(null=True)),
                ('pallet_status', models.BooleanField(default=True)),
                ('total_pallet_weight', models.FloatField()),
                ('pallet_weight_without_product', models.FloatField(null=True)),
                ('number_of_box', models.IntegerField()),
                ('pallet_id', models.CharField(max_length=15)),
                ('cold_house_id', models.IntegerField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(max_length=15)),
                ('company_id', models.CharField(default='28779866957588951697253390113453888744', max_length=250, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=12)),
                ('driver_id', models.CharField(default='28779867670642414325632428455349441768', max_length=250, primary_key=True, serialize=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.car')),
            ],
        ),
        migrations.CreateModel(
            name='FirstWeightLifting',
            fields=[
                ('weighting_time', models.FloatField(default=1640671927.3942478)),
                ('weight', models.FloatField()),
                ('product_category', models.CharField(choices=[('C', 'chicken'), ('T', 'turkey'), ('Q', 'quail')], max_length=1)),
                ('weight_lifting_id', models.CharField(default='28779867829098739354161103642437342440', max_length=250, primary_key=True, serialize=False)),
                ('sales_category', models.CharField(choices=[('P', 'pre-cold'), ('D', 'distribute'), ('F', 'freezing tunnel')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOwner',
            fields=[
                ('name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('product_owner_id', models.CharField(default='28779867512186089297103753268261541096', max_length=250, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='WeightLiftingManager',
            fields=[
                ('username', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=12)),
                ('Weight_Lifting_Manager_id', models.CharField(default='28779867195273439240046402894085739752', max_length=250, primary_key=True, serialize=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalesManager',
            fields=[
                ('username', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=12)),
                ('sales_manager_id', models.CharField(default='28779867116045276725782065300541789416', max_length=250, primary_key=True, serialize=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PreColdManager',
            fields=[
                ('username', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=12)),
                ('Pre_Cold_id', models.CharField(default='28779867432957926782839415674717590760', max_length=250, primary_key=True, serialize=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PreCold',
            fields=[
                ('pc_id', models.CharField(default='28779867908326901868425441235981292776', max_length=250, primary_key=True, serialize=False)),
                ('entry_time', models.FloatField(default=1640671927.4175756)),
                ('exit_time', models.FloatField(null=True)),
                ('weight', models.FloatField()),
                ('product_category', models.CharField(choices=[('C', 'chicken'), ('T', 'turkey'), ('Q', 'quail')], max_length=1)),
                ('pre_cold_id', models.IntegerField()),
                ('pallet_id', models.CharField(max_length=25, null=True)),
                ('product_pre_cold_status', models.BooleanField(default=True)),
                ('First_Weight_Lifting', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='WareHouseApp.firstweightlifting')),
                ('PreCold_Manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='WareHouseApp.precoldmanager')),
            ],
        ),
        migrations.CreateModel(
            name='PaperBox',
            fields=[
                ('product_category', models.CharField(choices=[('C', 'chicken'), ('T', 'turkey'), ('Q', 'quail')], max_length=1)),
                ('paper_box_weight', models.FloatField()),
                ('box_status', models.BooleanField(default=False)),
                ('number_of_product', models.IntegerField()),
                ('packing_time', models.FloatField(default=1640671927.5062249)),
                ('box_id', models.CharField(default='28779868146011389411218454016613143784', max_length=250, primary_key=True, serialize=False)),
                ('cold_house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.coldhouse')),
            ],
        ),
        migrations.CreateModel(
            name='LiveWeighbridgeManager',
            fields=[
                ('username', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=12)),
                ('Live_Weighbridge_Manager_id', models.CharField(default='28779867353729764268575078081173640424', max_length=250, primary_key=True, serialize=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LiveWeighbridge',
            fields=[
                ('live_weighbridge_id', models.CharField(default='28779867749870576839896766048893392104', max_length=250, primary_key=True, serialize=False)),
                ('final_weight', models.FloatField(null=True)),
                ('car_weight', models.FloatField(null=True)),
                ('car_empty', models.BooleanField(default=False)),
                ('weighting_date', models.FloatField(default=1640671927.3846526)),
                ('product_category', models.CharField(choices=[('C', 'chicken'), ('T', 'turkey'), ('Q', 'quail')], max_length=1)),
                ('slaughter_status', models.BooleanField(default=False)),
                ('slaughter_start_date', models.FloatField(null=True)),
                ('slaughter_finish_date', models.FloatField(null=True)),
                ('buy_price', models.IntegerField()),
                ('Live_Weighbridge_Manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='WareHouseApp.liveweighbridgemanager')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='WareHouseApp.driver')),
            ],
        ),
        migrations.CreateModel(
            name='FreezingTunnelManager',
            fields=[
                ('username', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=12)),
                ('Freezing_tunnel_Manager_id', models.CharField(default='28779867274501601754310740487629690088', max_length=250, primary_key=True, serialize=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FreezingTunnel',
            fields=[
                ('freeze_tunnel_id', models.CharField(default='28779868066783226896954116423069193448', max_length=250, primary_key=True, serialize=False)),
                ('entry_date', models.FloatField(default=1640671927.4668825)),
                ('exit_date', models.FloatField(null=True)),
                ('product_category', models.CharField(choices=[('C', 'chicken'), ('T', 'turkey'), ('Q', 'quail')], max_length=1)),
                ('weight', models.FloatField()),
                ('tunnel_id', models.IntegerField()),
                ('pallet_id', models.CharField(max_length=15, null=True)),
                ('status', models.BooleanField(default=True, verbose_name='آیا خارج شده یا نه')),
                ('first_weight_lifting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.firstweightlifting')),
                ('freezing_tunnel_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.freezingtunnelmanager')),
            ],
        ),
        migrations.AddField(
            model_name='firstweightlifting',
            name='Live_Weigh_Bridge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='WareHouseApp.liveweighbridge'),
        ),
        migrations.AddField(
            model_name='firstweightlifting',
            name='Weight_Lifting_Manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='WareHouseApp.weightliftingmanager'),
        ),
        migrations.CreateModel(
            name='Distributed',
            fields=[
                ('date', models.FloatField(default=1640671927.4367518)),
                ('weight', models.FloatField()),
                ('sale_price', models.IntegerField()),
                ('product_category', models.CharField(choices=[('C', 'chicken'), ('T', 'turkey'), ('Q', 'quail')], max_length=1)),
                ('bill_of_lading', models.CharField(default='28779867987555064382689778829525243112', max_length=250, primary_key=True, serialize=False)),
                ('number_of_box', models.IntegerField(null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.driver')),
                ('first_weight_lifting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.firstweightlifting')),
                ('sales_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.salesmanager')),
            ],
        ),
        migrations.AddField(
            model_name='coldhouse',
            name='freezing_tunnel_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.freezingtunnelmanager'),
        ),
        migrations.CreateModel(
            name='CEO',
            fields=[
                ('username', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=12)),
                ('ceo_id', models.CharField(default='28779867036817114211517727706997839080', max_length=250, primary_key=True, serialize=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='product_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='WareHouseApp.productowner'),
        ),
    ]
