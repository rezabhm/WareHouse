# Generated by Django 3.1.3 on 2022-02-07 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WareHouseApp', '0002_auto_20220207_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aviculture',
            name='aviculture_id',
            field=models.CharField(default='235069811015968250232065201752562929007', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.CharField(default='235069810857511925203536526565475028335', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='product_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='WareHouseApp.productowner'),
        ),
        migrations.AlterField(
            model_name='ceo',
            name='ceo_id',
            field=models.CharField(default='235069810302914787603686163410667375983', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date',
            field=models.FloatField(default=1644223266.6309202),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(default='235069810223686625089421825817123425647', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='bill_of_lading',
            field=models.CharField(default='235069811332880900289122552126738730351', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date',
            field=models.FloatField(default=1644223266.6181695),
        ),
        migrations.AlterField(
            model_name='driver',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WareHouseApp.car'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_id',
            field=models.CharField(default='235069810936740087717800864159018978671', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weight_lifting_id',
            field=models.CharField(default='235069811174424575260593876939650829679', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time',
            field=models.FloatField(default=1644223266.6078277),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date',
            field=models.FloatField(default=1644223266.6241598),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='freeze_tunnel_id',
            field=models.CharField(default='235069811412109062803386889720282680687', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='freezingtunnelmanager',
            name='Freezing_tunnel_Manager_id',
            field=models.CharField(default='235069810540599275146479176191299226991', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='live_weighbridge_id',
            field=models.CharField(default='235069811095196412746329539346106879343', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date',
            field=models.FloatField(default=1644223266.598055, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridgemanager',
            name='Live_Weighbridge_Manager_id',
            field=models.CharField(default='235069810619827437660743513784843177327', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='box_id',
            field=models.CharField(default='235069811491337225317651227313826631023', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time',
            field=models.FloatField(default=1644223266.6366723),
        ),
        migrations.AlterField(
            model_name='precold',
            name='entry_time',
            field=models.FloatField(default=1644223266.6130786),
        ),
        migrations.AlterField(
            model_name='precold',
            name='pc_id',
            field=models.CharField(default='235069811253652737774858214533194780015', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='precoldmanager',
            name='Pre_Cold_id',
            field=models.CharField(default='235069810699055600175007851378387127663', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productowner',
            name='product_owner_id',
            field=models.CharField(default='235069810778283762689272188971931077999', max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salesmanager',
            name='sales_manager_id',
            field=models.CharField(default='235069810382142950117950501004211326319', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='weightliftingmanager',
            name='Weight_Lifting_Manager_id',
            field=models.CharField(default='235069810461371112632214838597755276655', max_length=250, primary_key=True, serialize=False),
        ),
    ]
