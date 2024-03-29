# Generated by Django 3.1.3 on 2022-02-27 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceMaintenance', '0007_auto_20220224_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='sub_task_id',
            field=models.CharField(default='51735707720355505466024541961594792311', max_length=250),
        ),
        migrations.AlterField(
            model_name='subtaskstructure',
            name='sub_task_structure_id',
            field=models.CharField(default='51735707561899180437495866774506891639', max_length=250),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.CharField(default='51735707641127342951760204368050841975', max_length=250),
        ),
        migrations.AlterField(
            model_name='taskstructure',
            name='task_structure_id',
            field=models.CharField(default='51735707482671017923231529180962941303', max_length=100),
        ),
    ]
