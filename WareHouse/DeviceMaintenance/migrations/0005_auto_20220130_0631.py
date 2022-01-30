# Generated by Django 3.1.3 on 2022-01-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceMaintenance', '0004_auto_20220130_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='sub_task_id',
            field=models.CharField(default='97085967991632331531464911459474068300', max_length=250),
        ),
        migrations.AlterField(
            model_name='subtaskstructure',
            name='sub_task_structure_id',
            field=models.CharField(default='97085967833176006502936236272386167628', max_length=250),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.CharField(default='97085967912404169017200573865930117964', max_length=250),
        ),
        migrations.AlterField(
            model_name='taskstructure',
            name='task_structure_id',
            field=models.CharField(default='97085967753947843988671898678842217292', max_length=100),
        ),
    ]
