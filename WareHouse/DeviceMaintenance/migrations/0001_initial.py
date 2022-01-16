# Generated by Django 3.1.3 on 2022-01-15 06:19

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
            name='TaskStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_structure_id', models.CharField(default='50463706612010441660283649204093181631', max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('cycle_time', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TaskUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('task_structure', models.ManyToManyField(to='DeviceMaintenance.TaskStructure')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_task_time', models.FloatField()),
                ('deadline', models.FloatField()),
                ('task_id', models.CharField(default='50463706770466766688812324391181082303', max_length=250)),
                ('task_structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DeviceMaintenance.taskstructure')),
            ],
        ),
        migrations.CreateModel(
            name='SubTaskStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('sub_task_structure_id', models.CharField(default='50463706691238604174547986797637131967', max_length=250)),
                ('task_structure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DeviceMaintenance.taskstructure')),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_status', models.CharField(choices=[('D', 'Task Done'), ('T', 'Trouble'), ('I', 'Ignore task')], default='I', max_length=1)),
                ('sub_task_id', models.CharField(default='50463706849694929203076661984725032639', max_length=250)),
                ('trouble_description', models.TextField(default='Nothing')),
                ('sub_task_structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DeviceMaintenance.subtaskstructure')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DeviceMaintenance.task')),
            ],
        ),
    ]
