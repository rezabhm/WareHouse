# Generated by Django 3.1.3 on 2022-02-08 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceMaintenance', '0002_auto_20220207_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='sub_task_id',
            field=models.CharField(default='246535948855105500767628906327881788400', max_length=250),
        ),
        migrations.AlterField(
            model_name='subtaskstructure',
            name='sub_task_structure_id',
            field=models.CharField(default='246535948696649175739100231140793887728', max_length=250),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.CharField(default='246535948775877338253364568734337838064', max_length=250),
        ),
        migrations.AlterField(
            model_name='taskstructure',
            name='task_structure_id',
            field=models.CharField(default='246535948617421013224835893547249937392', max_length=100),
        ),
    ]
