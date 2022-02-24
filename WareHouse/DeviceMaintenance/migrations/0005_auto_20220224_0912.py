# Generated by Django 3.1.3 on 2022-02-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceMaintenance', '0004_auto_20220224_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='sub_task_id',
            field=models.CharField(default='317023811414368750596232768106418460591', max_length=250),
        ),
        migrations.AlterField(
            model_name='subtaskstructure',
            name='sub_task_structure_id',
            field=models.CharField(default='317023811255912425567704092919330559919', max_length=250),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.CharField(default='317023811335140588081968430512874510255', max_length=250),
        ),
        migrations.AlterField(
            model_name='taskstructure',
            name='task_structure_id',
            field=models.CharField(default='317023811176684263053439755325786609583', max_length=100),
        ),
    ]