# Generated by Django 3.1.3 on 2022-02-23 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WareHouseApp', '0004_auto_20220221_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('automation_id', models.CharField(max_length=150)),
                ('automation_create_time', models.FloatField()),
                ('automation_create_time_format', models.CharField(max_length=50)),
                ('automation_create_username', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='aviculture',
            name='aviculture_id',
            field=models.CharField(default='48418399835708860807160486029317284535', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.CharField(default='48418399677252535778631810842229383863', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ceo',
            name='ceo_id',
            field=models.CharField(default='48418399043427235664517110093877781175', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='cold_house_primary_key',
            field=models.CharField(default='48418400548762323435539524371212837559', max_length=150),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date',
            field=models.FloatField(default=1645601715.511062),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date_format',
            field=models.CharField(default='Wed Feb 23 07:35:15 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='exit_date_format',
            field=models.CharField(default='Wed Feb 23 07:35:15 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(default='48418398964199073150252772500333830839', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='bill_of_lading',
            field=models.CharField(default='48418400231849673378482173997037036215', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date',
            field=models.FloatField(default=1645601715.503545),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date_format',
            field=models.CharField(default='Wed Feb 23 07:35:15 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='sales_input_id',
            field=models.CharField(default='48418400311077835892746511590580986551', max_length=200),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='dist_id',
            field=models.CharField(default='48418400152621510864217836403493085879', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_id',
            field=models.CharField(default='48418399756480698292896148435773334199', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weight_lifting_id',
            field=models.CharField(default='48418399994165185835689161216405185207', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time',
            field=models.FloatField(default=1645601715.4997916),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time_format',
            field=models.CharField(default='Wed Feb 23 07:35:15 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date',
            field=models.FloatField(default=1645601715.5092754),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date_format',
            field=models.CharField(default='Wed Feb 23 07:35:15 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='exit_date_format',
            field=models.CharField(default='Wed Feb 23 07:35:15 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='freeze_tunnel_id',
            field=models.CharField(default='48418400390305998407010849184124936887', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='input_id',
            field=models.CharField(default='48418400469534160921275186777668887223', max_length=200),
        ),
        migrations.AlterField(
            model_name='freezingtunnelmanager',
            name='Freezing_tunnel_Manager_id',
            field=models.CharField(default='48418399281111723207310122874509632183', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='live_weighbridge_id',
            field=models.CharField(default='48418399914937023321424823622861234871', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date',
            field=models.FloatField(default=1645601715.4851387, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date_format',
            field=models.CharField(default='Wed Feb 23 07:35:15 2022', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridgemanager',
            name='Live_Weighbridge_Manager_id',
            field=models.CharField(default='48418399360339885721574460468053582519', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='box_id',
            field=models.CharField(default='48418400627990485949803861964756787895', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='exit_time',
            field=models.FloatField(default=1645601715.5128965, null=True),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time',
            field=models.FloatField(default=1645601715.512836),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time_format',
            field=models.CharField(default='Wed Feb 23 07:35:15 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='precold',
            name='entry_time',
            field=models.FloatField(default=1645601715.5012467),
        ),
        migrations.AlterField(
            model_name='precold',
            name='entry_time_format',
            field=models.CharField(default='Wed Feb 23 07:35:15 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='precold',
            name='pc_id',
            field=models.CharField(default='48418400073393348349953498809949135543', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='precoldmanager',
            name='Pre_Cold_id',
            field=models.CharField(default='48418399439568048235838798061597532855', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productowner',
            name='product_owner_id',
            field=models.CharField(default='48418399598024373264367473248685433527', max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salesmanager',
            name='sales_manager_id',
            field=models.CharField(default='48418399122655398178781447687421731511', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='weightliftingmanager',
            name='Weight_Lifting_Manager_id',
            field=models.CharField(default='48418399201883560693045785280965681847', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='UserAutomation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('automation_input_type', models.CharField(choices=[('F', 'File'), ('M', 'Message')], max_length=1)),
                ('automation_input_id', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SlaughterEmployee',
            fields=[
                ('username', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=12)),
                ('Slaughter_Employee_id', models.CharField(default='48418399518796210750103135655141483191', max_length=250, primary_key=True, serialize=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MessageAutomation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('automation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.automation')),
            ],
        ),
        migrations.CreateModel(
            name='FileAutomation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_automation_id', models.CharField(max_length=150)),
                ('file', models.FileField(upload_to='WareHouseApp/file/')),
                ('automation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.automation')),
            ],
        ),
    ]
