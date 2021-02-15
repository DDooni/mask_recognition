# Generated by Django 3.1.3 on 2020-11-07 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20201107_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='father',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='surname',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Warning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('image', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('cam_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.camera')),
            ],
        ),
    ]