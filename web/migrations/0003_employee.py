# Generated by Django 3.1.3 on 2020-11-07 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_area_camera_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('father', models.CharField(max_length=20)),
                ('birth', models.DateField()),
                ('phone', models.CharField(max_length=17)),
                ('org_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.organization')),
                ('sched_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.schedule')),
            ],
        ),
    ]
