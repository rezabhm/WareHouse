# Generated by Django 3.1.3 on 2022-02-24 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WareHouseApp', '0007_auto_20220224_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automation',
            name='automation_create_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='automation',
            name='code',
            field=models.CharField(default=7634, max_length=10),
        ),
        migrations.AlterField(
            model_name='aviculture',
            name='aviculture_id',
            field=models.CharField(default='317023810305174475396532041796803155887', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.CharField(default='317023810146718150368003366609715255215', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ceo',
            name='ceo_id',
            field=models.CharField(default='317023809512892850253888665861363652527', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='cold_house_primary_key',
            field=models.CharField(default='317023811018227938024911080138698708911', max_length=150),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date',
            field=models.FloatField(default=1645693966.8078263),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date_format',
            field=models.CharField(default='Thu Feb 24 09:12:46 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='exit_date_format',
            field=models.CharField(default='Thu Feb 24 09:12:46 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(default='317023809433664687739624328267819702191', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='bill_of_lading',
            field=models.CharField(default='317023810701315287967853729764522907567', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date',
            field=models.FloatField(default=1645693966.8058963),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date_format',
            field=models.CharField(default='Thu Feb 24 09:12:46 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='sales_input_id',
            field=models.CharField(default='317023810780543450482118067358066857903', max_length=200),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='dist_id',
            field=models.CharField(default='317023810622087125453589392170978957231', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_id',
            field=models.CharField(default='317023810225946312882267704203259205551', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weight_lifting_id',
            field=models.CharField(default='317023810463630800425060716983891056559', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time',
            field=models.FloatField(default=1645693966.80335),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time_format',
            field=models.CharField(default='Thu Feb 24 09:12:46 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date',
            field=models.FloatField(default=1645693966.806825),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date_format',
            field=models.CharField(default='Thu Feb 24 09:12:46 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='exit_date_format',
            field=models.CharField(default='Thu Feb 24 09:12:46 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='freeze_tunnel_id',
            field=models.CharField(default='317023810859771612996382404951610808239', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='input_id',
            field=models.CharField(default='317023810938999775510646742545154758575', max_length=200),
        ),
        migrations.AlterField(
            model_name='freezingtunnelmanager',
            name='Freezing_tunnel_Manager_id',
            field=models.CharField(default='317023809750577337796681678641995503535', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='live_weighbridge_id',
            field=models.CharField(default='317023810384402637910796379390347106223', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date',
            field=models.FloatField(default=1645693966.8016984, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date_format',
            field=models.CharField(default='Thu Feb 24 09:12:46 2022', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridgemanager',
            name='Live_Weighbridge_Manager_id',
            field=models.CharField(default='317023809829805500310946016235539453871', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='box_id',
            field=models.CharField(default='317023811097456100539175417732242659247', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='exit_time',
            field=models.FloatField(default=1645693966.8090155, null=True),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time',
            field=models.FloatField(default=1645693966.8089774),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time_format',
            field=models.CharField(default='Thu Feb 24 09:12:46 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='precold',
            name='entry_time',
            field=models.FloatField(default=1645693966.8042932),
        ),
        migrations.AlterField(
            model_name='precold',
            name='entry_time_format',
            field=models.CharField(default='Thu Feb 24 09:12:46 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='precold',
            name='pc_id',
            field=models.CharField(default='317023810542858962939325054577435006895', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='precoldmanager',
            name='Pre_Cold_id',
            field=models.CharField(default='317023809909033662825210353829083404207', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productowner',
            name='product_owner_id',
            field=models.CharField(default='317023810067489987853739029016171304879', max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salesmanager',
            name='sales_manager_id',
            field=models.CharField(default='317023809592121012768153003454907602863', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='slaughteremployee',
            name='Slaughter_Employee_id',
            field=models.CharField(default='317023809988261825339474691422627354543', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='weightliftingmanager',
            name='Weight_Lifting_Manager_id',
            field=models.CharField(default='317023809671349175282417341048451553199', max_length=250, primary_key=True, serialize=False),
        ),
    ]
