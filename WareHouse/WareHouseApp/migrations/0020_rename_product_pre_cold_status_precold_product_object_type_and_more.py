# Generated by Django 4.0.3 on 2022-03-13 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WareHouseApp', '0019_alter_automation_code_alter_aviculture_aviculture_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='precold',
            old_name='product_pre_cold_status',
            new_name='product_object_type',
        ),
        migrations.RemoveField(
            model_name='precold',
            name='First_Weight_Lifting',
        ),
        migrations.RemoveField(
            model_name='precold',
            name='entry_time',
        ),
        migrations.RemoveField(
            model_name='precold',
            name='entry_time_format',
        ),
        migrations.RemoveField(
            model_name='precold',
            name='exit_time',
        ),
        migrations.RemoveField(
            model_name='precold',
            name='exit_time_format',
        ),
        migrations.RemoveField(
            model_name='precold',
            name='out_status',
        ),
        migrations.AddField(
            model_name='precold',
            name='product_category',
            field=models.CharField(choices=[('C', 'chicken'), ('T', 'turkey'), ('Q', 'quail')], default='C', max_length=1),
        ),
        migrations.AddField(
            model_name='precold',
            name='product_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='WareHouseApp.productowner'),
        ),
        migrations.AddField(
            model_name='precold',
            name='sub_product_category',
            field=models.CharField(choices=[('W', 'wing'), ('N', 'neck'), ('E', 'leg'), ('H', 'heart'), ('L', 'liver'), ('K', 'kidney'), ('S', 'sangdan'), ('B', 'body'), ('O', 'other')], default='B', max_length=1),
        ),
        migrations.AddField(
            model_name='precold',
            name='time_format',
            field=models.CharField(default='Sun Mar 13 12:07:31 2022', max_length=30),
        ),
        migrations.AddField(
            model_name='precold',
            name='time_obj',
            field=models.FloatField(default=1647173251.6082504),
        ),
        migrations.AddField(
            model_name='precold',
            name='weight',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='automation',
            name='code',
            field=models.CharField(default=2071, max_length=10),
        ),
        migrations.AlterField(
            model_name='aviculture',
            name='aviculture_id',
            field=models.CharField(default='54445048081964053176453604018849780461', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.CharField(default='54443383498269628482720763660453221101', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ceo',
            name='ceo_id',
            field=models.CharField(default='54439912512469878562090790499989000941', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='cold_house_primary_key',
            field=models.CharField(default='54448889063282744711540139029562069741', max_length=150),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date',
            field=models.FloatField(default=1647173251.6109056),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='entry_date_format',
            field=models.CharField(default='Sun Mar 13 12:07:31 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='coldhouse',
            name='exit_date_format',
            field=models.CharField(default='Sun Mar 13 12:07:31 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.CharField(default='54439052094624973651384524612688351981', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='bill_of_lading',
            field=models.CharField(default='54447798883766548434254851864805446381', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date',
            field=models.FloatField(default=1647173251.6094227),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='date_format',
            field=models.CharField(default='Sun Mar 13 12:07:31 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='distributed',
            name='sales_input_idistd',
            field=models.CharField(default='54447854343480308419291167345570681581', max_length=200),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='create_time',
            field=models.FloatField(default=1647173251.6088629),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='create_time_format',
            field=models.CharField(default='Sun Mar 13 12:07:31 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='dist_id',
            field=models.CharField(default='54447268847359328005836351055777698541', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='exit_time',
            field=models.FloatField(default=1647173251.6088948),
        ),
        migrations.AlterField(
            model_name='distributedroot',
            name='exit_time_format',
            field=models.CharField(default='Sun Mar 13 12:07:31 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_id',
            field=models.CharField(default='54443775677674074091191851703007384301', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weight_lifting_id',
            field=models.CharField(default='54446287210425776270693567046233035501', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time',
            field=models.FloatField(default=1647173251.6074867),
        ),
        migrations.AlterField(
            model_name='firstweightlifting',
            name='weighting_time_format',
            field=models.CharField(default='Sun Mar 13 12:07:31 2022', max_length=30),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date',
            field=models.FloatField(default=1647173251.6100938),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='entry_date_format',
            field=models.CharField(default='Sun Mar 13 12:07:31 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='exit_date_format',
            field=models.CharField(default='Sun Mar 13 12:07:31 2022', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='freeze_tunnel_id',
            field=models.CharField(default='54448247315166379170405631323564348141', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='freezingtunnel',
            name='input_id',
            field=models.CharField(default='54448412109744408840227825894981047021', max_length=200),
        ),
        migrations.AlterField(
            model_name='freezingtunnelmanager',
            name='Freezing_tunnel_Manager_id',
            field=models.CharField(default='54441307720411754757075812808954417901', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='live_weighbridge_id',
            field=models.CharField(default='54445269920819093116598865941910721261', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date',
            field=models.FloatField(default=1647173251.6063747, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridge',
            name='weighting_date_format',
            field=models.CharField(default='Sun Mar 13 12:07:31 2022', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='liveweighbridgemanager',
            name='Live_Weighbridge_Manager_id',
            field=models.CharField(default='54441733967926081499212066075407225581', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='box_id',
            field=models.CharField(default='54449658368740758218258172341319832301', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='exit_time',
            field=models.FloatField(default=1647173251.6118023, null=True),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time',
            field=models.FloatField(default=1647173251.6117716),
        ),
        migrations.AlterField(
            model_name='paperbox',
            name='packing_time_format',
            field=models.CharField(default='Sun Mar 13 12:07:31 2022', max_length=50),
        ),
        migrations.AlterField(
            model_name='precold',
            name='PreCold_Manager',
            field=models.CharField(default='Admin', max_length=150),
        ),
        migrations.AlterField(
            model_name='precold',
            name='box_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='precold',
            name='out_category',
            field=models.CharField(choices=[('D', 'distribute'), ('F', 'freezing_tunnel'), ('G', 'gate_bandi'), ('I', 'inside')], default='G', max_length=1),
        ),
        migrations.AlterField(
            model_name='precold',
            name='pc_id',
            field=models.CharField(default='54446763371682486999362504245374554861', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='precoldmanager',
            name='Pre_Cold_id',
            field=models.CharField(default='54442254496953800215910055659160933101', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productowner',
            name='product_owner_id',
            field=models.CharField(default='54443068962464446853300517290970387181', max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salesmanager',
            name='sales_manager_id',
            field=models.CharField(default='54440405311640717286270622343360090861', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='slaughteremployee',
            name='Slaughter_Employee_id',
            field=models.CharField(default='54442670444807000103682421764900197101', max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='weightliftingmanager',
            name='Weight_Lifting_Manager_id',
            field=models.CharField(default='54440866419546550304715416769151046381', max_length=250, primary_key=True, serialize=False),
        ),
    ]
